import arcpy # si se trabaja en arcmap, no es necesario llamar

##### INPUT #####
Output = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_2/Output"
arcpy.env.workspace= Output

Source_File = "TEM_HIDRO_CUENCAS_HIDROGRAFICAS"
var = 'NOMBRE'
query_value = 'Cuenca Ocoña'

##### PROCESS #####
mxd = arcpy.mapping.MapDocument('CURRENT') # mxd temporal

# Seleccionar cuenca
Attribute = "{} = '{}'".format(var, query_value)
arcpy.MakeFeatureLayer_management(Source_File, 'basin_mold', Attribute)

##### OUTPUT #####
# Shapefile
#arcpy.FeatureClassToShapefile_conversion('basin_mold', Output)

# layer file
arcpy.SaveToLayerFile_management('basin_mold', "basin_mold.lyr")
# KML
arcpy.LayerToKML_conversion('basin_mold.lyr', "basin_mold.kmz")

del mxd
