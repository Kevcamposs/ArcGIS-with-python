import arcpy

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_3/"
arcpy.env.workspace= dir + 'Output/' # carpeta con curvas de nivel

##### PROCESS #####
arcpy.CheckOutExtension("3D")

# Archivo TIN
input_tin = "Oconia_tin"

# Archivo Raster
output_raster = "Oconia_DEM.tif"

# Recorte
arcpy.TinRaster_3d(input_tin, output_raster, "INT", "LINEAR", "OBSERVATIONS 250")
