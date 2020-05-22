#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Title: Creating and Cleaning A Pandas Dataframe made of Multiple Geospatial Raster Layers - Florida Fire Study
#Author: Emily Evenden
#Date: May 22, 2020

'''
The purpose of this script to to use advanced Python packages to create a dataframe from multiple geospatial raster layers. 
The dataframe will then be used for data visualization and regression analysis. The aim of this analysis is to see how
fire severity impacts net ecosystem productivity recovery and aboveground biomass regrowth following fire disturbances.

The raster layers come from the 'Forest Carbon Stocks and Fluxes After Disturbance, Southeastern USA, 1990-2010' dataset available 
through the Oak Ridge National Laboratory. Specifically, the purpose of this script to create a dataframe from 8 raster layers 
inclduing: Aboveground Biomass (Kg C m-2) at 1990, 2000, and 2010; Net Ecosystem Productivity (g C m-2) at 1990, 2000, and 2010; 
Forest Type; and Year of Fire Disturbance.

The raster layer were preprocessed using TerrSet prior to using them in this script. All layers have a have an AlbersUS83 projection
and have a 30m resolution.
''''

#Import packages
#Numpy is used to make arrays
import numpy as np
#Pandas can used Numpy arrays to create dataframes
import pandas as pd
#PIL is used to open image files to obtain pixel values
from PIL import Image
#OS allows the user to set the working folder
import os


# In[ ]:


#Set working directory
dir = os.chdir("C:\\Users\\Emily\\Documents\\Summer_2020\\Py_DataScience_and_MachineLearning\\original\\FL_Script\\Python_FL_Project\\Python_FL_Project")


# In[3]:


#This line deactivates the zip bomb safety in Python 3. Because I am working with large files, I want to deactivate the size limit imposed by the zip bomb check.
Image.MAX_IMAGE_PIXELS = None

#This section opens each TIFF as an array and assigns them to a variable. Because I already preprocessed the spatial data the images are all the same size.
#AGB = Aboveground Biomass
#NEP = Net Ecosystem Productivity
#Forest Type = Numeric Code for Forest Type
#Burn Year = # of Years after 1970 when the area was burned

AGB_2010 = np.asarray(Image.open('Smaller_FL_agb_2010.tif'))
AGB_2000 = np.asarray(Image.open('Smaller_FL_agb_2000.tif'))
AGB_1990 = np.asarray(Image.open('Smaller_FL_agb_1990.tif'))
Forest_Type = np.asarray(Image.open('Smaller_FL_forest_group_NAFD.tif'))
NEP_1990 = np.asarray(Image.open('Smaller_FL_nep_1990.tif'))
NEP_2000 = np.asarray(Image.open('Smaller_FL_nep_2000.tif'))
NEP_2010 = np.asarray(Image.open('Smaller_FL_nep_2010.tif'))
Burn_Year = np.asarray(Image.open('Smaller_FL_years_disturb_MTSB.tif'))

#Check point to make sure it works 
print('Ok')


# In[4]:


#This section flattens each array so the 2D data is converted to 1D data. This allows each raster layer to become a column in the dataframe.

FL_AGB_1990 = AGB_1990.flatten()
FL_AGB_2000 = AGB_2000.flatten()
FL_AGB_2010 = AGB_2010.flatten()
FL_Forest_Type = Forest_Type.flatten()
FL_NEP_1990 = NEP_1990.flatten()
FL_NEP_2000 = NEP_2000.flatten()
FL_NEP_2010 = NEP_2010.flatten()
FL_Burn_Year = Burn_Year.flatten()

#Check point
print('Ok')


# In[5]:


#Here I stack all of the flattened arrays and transpose them into vertical columns. This creates a larger 2D array, FL_arr, from the multiple 1D arrays.
FL_arr = np.vstack([FL_AGB_1990, FL_AGB_2000, FL_AGB_2010, FL_Forest_Type, FL_NEP_1990, FL_NEP_2000, FL_NEP_2010, FL_Burn_Year]).T


# In[6]:


#I created a Pandas dataframe from the vertically stacked 2D array, FL_arr, and assigned column names.
FL_Data = pd.DataFrame(FL_arr, columns=['AGB_1990', 'AGB_2000','AGB_2010', 'Forest_Type', 'NEP_1990', 'NEP_2000', 'NEP_2010', 'Burn_Year'])
#Check point
print (FL_Data)


# In[8]:


#Now that the dataframe is created, I want to remove rows that are not necessary for the analysis.
#First, I want to remove pixels which did not experience fire, or had fires which occured before or at 1990 and at 2010. 
#This will leave only pixels which burned between 1991 - 2009.

#First, I identified all unique values for Burn_Year to see whether there are pixels that occured outside of my target time interval.
FL_Data['Burn_Year'].unique()
#The only years outside of my target time interval are 0 (No fire), 16 (1986), 20 (1990), and 40 (2010).
FL_Data = FL_Data[(FL_Data.Burn_Year != 0) & (FL_Data.Burn_Year != 16) & (FL_Data.Burn_Year != 20) & (FL_Data.Burn_Year != 40)]
#Check that pixels with unwanted years were removed
FL_Data['Burn_Year'].unique()


# In[31]:


'''
Now I want to limit th dataframe to pixels which have less aboveground following a fire event. Though this is not necessarily
scientifically sound decision, my professor and I realized there may be a lot of edge pixels which are considered burned but don't
follow expected trends when looking at the AGB and NEP layers.
'''

#Here, I create two columns to find the difference in AGB between 1990 & 2000 and 2000 & 2010.
FL_Data['Minus_90_00'] = FL_Data['AGB_1990'] - FL_Data['AGB_2000']
FL_Data['Minus_00_10'] = FL_Data['AGB_2000'] - FL_Data['AGB_2010']
#I only select pixels here the net change in AGB between 1990 - 2000 or 2000 - 2010 is positive. (This means there's less AGB in the second time point).
FL_Data = FL_Data[(FL_Data.Minus_90_00 > 0) | (FL_Data.Minus_00_10 > 0)]

#Here, I created two more columns to show the date of the fire and it's age at 2010.
FL_Data['Date'] = 1970 + FL_Data['Burn_Year'] 
FL_Data['Burn_Scar_Age'] = 40 - FL_Data['Burn_Year']

#Check
print (FL_Data)


# In[10]:


#I want to create categorize the pixel as having a burn severity of High, Medium, and Low. I decided the assign these labels based on the percent of aboveground biomass lost by a pixel following a fire.
#First, I created a new column calculating the percent aboveground biomass lost. For pixel burned before 2001, I calculated this using AGB_1990 and AGB_2000.
FL_Data['Burn_Severity'] = ((FL_Data['AGB_1990']-FL_Data['AGB_2000'])/FL_Data['AGB_1990']*100)
#However, for pixels burned from 2001 - 2009, I want to calculate the percent of AGB lost using the AGB 2000 and AGB 2010 columns. In this case, I replaced the values in 'Burn_Severity' for select rows based on their date.
FL_Data.loc[(FL_Data.Date>2000), 'Burn_Severity'] = ((FL_Data['AGB_2000']-FL_Data['AGB_2010'])/FL_Data['AGB_2000']*100)
#Check point
print (FL_Data)


# In[11]:


#After creating a numeric variable to measure burn severity, I want to place pixels into categorical bins.
#First I create list of categorical bins
bs_labels = ['Low', 'Moderate', 'Severe']
#Then I assign custom bounds for the intervals.
cut_bins = [0, 30, 70, 100]
#I used the pd.cut function to create a new variable which places each pixel into a categorical bin based on it 'Burn_Severity' value.
FL_Data['Severity_Label'] = pd.cut(FL_Data['Burn_Severity'], bins=cut_bins, labels=bs_labels)
#Check point
print (FL_Data)


# In[29]:


#Finally, I want to replace the numeric codes signifying 'Forest_Type' with descriptive str labels because it's more intuitive to read.
#First I create a list of the str forest type names
forest_type_list = ['White/Red/Jack Pine', 'Spruce/Fir', 'Longleaf/Slash Pine', 'Loblolly/Shortleaf Pine', 'Pinyon/Juniper', 'Oak/Pine', 'Oak/Hickory', 'Oak/Gum/Cypress', 'Elm/Ash/Cottonwood', 'Maple/Beech/Birch', 'Tropical Hardwoods', 'Exotic Hardwoods']
#Then, I create a list of the values associated with each name
code_list = [100, 120, 140, 160, 180, 400, 500, 600, 700, 800, 980, 990]
#Finally, I create a dictionary which associates each value with a str label.
forest_dict = dict(zip(code_list, forest_type_list))
# To rplace the numeric code Forest Type with the str label, I used the .replace function.
FL_Data['Forest_Type'].replace(forest_dict, inplace=True)
#Check point
print (FL_Data)

#Now my dataframe is ready for further analysis.


# In[ ]:




