import arcpy
from arcpy.sa import *

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_3/"
arcpy.env.workspace= dir + 'Output/'

##### PROCESS #####
arcpy.CheckOutExtension("Spatial")
# Archivo raster
in_raster = dir + "Output/Oconia_DEM_cut.tif"

# Archivo raster salida
out_raster = dir + "Output/Oconia_aspect.tif"

# Aspect => Mapa de orientaciones
outAspect = Aspect(in_raster)
outAspect.save(out_raster)
