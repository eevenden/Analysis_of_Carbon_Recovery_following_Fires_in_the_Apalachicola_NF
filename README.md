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

![Histogram_Severity](https://user-images.githubusercontent.com/54719919/84538480-b6926580-acbf-11ea-8483-f2072d5e7ed9.png)

![Scatterplot_AGB_NEP](https://user-images.githubusercontent.com/54719919/84538629-f9ecd400-acbf-11ea-9b05-47327d0c5541.png)
