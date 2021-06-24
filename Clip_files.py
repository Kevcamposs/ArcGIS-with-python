import arcpy
import os

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_2/"
arcpy.env.workspace= dir + 'Output/Projection' # carpeta con archivos a clip
files = arcpy.ListFeatureClasses() # Leer carpeta de archivos
os.makedirs(dir + 'Output/Clip') # crear carpeta para clips
mxd = arcpy.mapping.MapDocument(dir + 'Lab_2.mxd') # mxd de trabajo
##### PROCESS #####
# Archivo a realizar clip
for i in files:
    in_features = i

    # Molde
    clip_features = dir + 'Output/Basin_mold.shp'

    # Archivo recortado
    out_feature_class = dir + 'Output/Clip/' + i

    # Recorte
    arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
