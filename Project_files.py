import arcpy
import os

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_2/"
arcpy.env.workspace= Output + 'Input/Cartas/' # carpeta con archivos a proyectar
os.makedirs(dir + 'Output/Projection') # crear carpeta para proyecciones
files = arcpy.ListFeatureClasses() # Leer carpeta de archivos
mxd = arcpy.mapping.MapDocument(dir + 'Lab_2.mxd') # mxd de trabajo
##### PROCESS #####
# Archivo a prooyectar - WGS 1984
for i in files:
    input_features = i

    # Archivo proyectado
    output_feature_class = dir + 'Output/Projection/' + i

    # Sistema a proyectar
    out_coordinate_system = arcpy.SpatialReference('WGS 1984 UTM Zone 18S')
    # Proyección
    arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)
# https://desktop.arcgis.com/es/arcmap/latest/analyze/python/pdf/projected_coordinate_systems.pdf
# https://desktop.arcgis.com/es/arcmap/latest/tools/data-management-toolbox/project.htm
