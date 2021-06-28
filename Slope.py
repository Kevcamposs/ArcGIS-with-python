import arcpy
from arcpy.sa import *

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_3/"
arcpy.env.workspace= dir + 'Output/'

##### PROCESS #####
# Archivo raster
in_raster = dir + "Output/Oconia_DEM_cut.tif"

# Archivo raster salida
out_raster = dir + "Output/Oconia_Slope.tif"

# Aspect => Mapa de orientaciones
outSlope = Slope(in_raster, "DEGREE")
outSlope.save(out_raster)
