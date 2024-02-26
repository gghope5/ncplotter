# ncplotter
Python: custom plotter for netCDF data
Uses libraries:
*numpy
*matplotlib
*cartopy
*netCDF4
# example usage of function
ncplotter(ccrs.PlateCarree(),'/Users/gghope/PycharmProjects/KonradLearningPython/rel_humid.nc','r',6,6,'RH %','Average Relative Humidity in Summer 2020', False)

Coordinate Reference System (cartopy)*, file name*, dependent variable name in data*, width of frame, height of frame,
title for colorbar, title for plot, true/false if dependent variable is a temperature value

variables with * denote that they are mandatory to run the function. All others are optional.
