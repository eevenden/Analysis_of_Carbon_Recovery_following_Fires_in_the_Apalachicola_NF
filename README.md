# Analysis of Carbon Recovery following Fires in the Appalachicola National Forest

The purpose of this script to to use advanced Python packages to create a dataframe from multiple geospatial raster layers. 
The dataframe will then be used for data visualization and regression analysis. The aim of this analysis is to see how
fire severity impacts net ecosystem productivity recovery and aboveground biomass regrowth following fire disturbances.

The raster layers come from the 'Forest Carbon Stocks and Fluxes After Disturbance, Southeastern USA, 1990-2010' dataset available 
through the Oak Ridge National Laboratory. Specifically, the purpose of this script to create a dataframe from 8 raster layers 
inclduing: Aboveground Biomass (Kg C m-2) at 1990, 2000, and 2010; Net Ecosystem Productivity (g C m-2) at 1990, 2000, and 2010; 
Forest Type; and Year of Fire Disturbance.

The raster layer were preprocessed using TerrSet prior to using them in this script. All layers have a have an AlbersUS83 projection
and have a 30m resolution.


![FL_Data_Screenshot](https://user-images.githubusercontent.com/54719919/84538971-9dd67f80-acc0-11ea-8d72-a9695f375f3d.png)

Figure 1. shows the frequency of moderate and high-severity burned pixels by year of fire disturbance. Notice there are no observations for the years 2001-2003.
![Histogram_Severity](https://user-images.githubusercontent.com/54719919/84538480-b6926580-acbf-11ea-8483-f2072d5e7ed9.png)

![Scatterplot_AGB_NEP](https://user-images.githubusercontent.com/54719919/84538629-f9ecd400-acbf-11ea-9b05-47327d0c5541.png)

![FacetGrid_AGB_Raw](https://user-images.githubusercontent.com/54719919/84539151-e42bde80-acc0-11ea-8c91-6b51d7c6ff2e.png)

![FacetGrid_AGB_Mean](https://user-images.githubusercontent.com/54719919/84539159-e857fc00-acc0-11ea-86e0-2519fe9f1313.png)

![FacetGrid_NEP_Raw](https://user-images.githubusercontent.com/54719919/84539296-23f2c600-acc1-11ea-9b2a-5ae87d8a2c99.png)

![FacetGrid_NEP_Mean](https://user-images.githubusercontent.com/54719919/84539280-1e957b80-acc1-11ea-8487-c63688ec1fa0.png)

![MOD_AGB](https://user-images.githubusercontent.com/54719919/84541010-84373700-acc4-11ea-907c-6098c3cc61d7.png)
![MOD_AGB_Quad](https://user-images.githubusercontent.com/54719919/84541011-84373700-acc4-11ea-8aa4-6234b7e3d349.png)
![MOD_NEP](https://user-images.githubusercontent.com/54719919/84541012-84cfcd80-acc4-11ea-8561-f1afb823aaa2.png)
![MOD_NEP_Quad](https://user-images.githubusercontent.com/54719919/84541013-84cfcd80-acc4-11ea-843c-427f66798d2d.png)

![SEV_AGB](https://user-images.githubusercontent.com/54719919/84541025-89948180-acc4-11ea-99df-9d5aef485481.png)
![SEV_AGB_Quad](https://user-images.githubusercontent.com/54719919/84541026-89948180-acc4-11ea-98c1-434bc46c605b.png)
![SEV_NEP](https://user-images.githubusercontent.com/54719919/84541027-8a2d1800-acc4-11ea-8b86-71c9ffd02dd8.png)
![SEV_NEP_Quad](https://user-images.githubusercontent.com/54719919/84541028-8a2d1800-acc4-11ea-9885-dc0ec1bf43be.png)

![F_Stat_Mod_NEP](https://user-images.githubusercontent.com/54719919/84541023-89948180-acc4-11ea-8058-696b55d432fe.png)
![F_Stat_Sev_NEP](https://user-images.githubusercontent.com/54719919/84541024-89948180-acc4-11ea-852b-3294fa0081c8.png)
