import arcpy
from arcpy.sa import *

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_3/"
arcpy.env.workspace= dir + 'Output/'

##### PROCESS #####
# Archivo a realizar corte
in_raster = dir + "Output/Oconia_DEM.tif"

# Molde
mask_shp = dir + 'Input/basin_mold.shp'

# Archivo recortado
out_raster = dir + "Output/Oconia_DEM_cut.tif"

# Recorte
outExtractByMask = ExtractByMask(in_raster, mask_shp)
outExtractByMask.save(out_raster)
