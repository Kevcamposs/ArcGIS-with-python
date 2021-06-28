import arcpy
from arcpy.sa import *

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_3/"
arcpy.env.workspace= dir + 'Output/'

##### PROCESS #####
# Archivo raster
in_raster = dir + "Output/Oconia_DEM_cut.tif"

# Archivo raster salida
out_raster = dir + "Output/Oconia_Hillshade.tif"

# Aspect => Mapa de orientaciones
outHillshade = Hillshade(in_raster, 135, 45, "NO_SHADOWS", 1)
#outHillshade.save(out_raster)
