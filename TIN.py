import arcpy

##### INPUT #####
dir = r"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_3/"
arcpy.env.workspace= dir + 'Output/' # carpeta con curvas de nivel

##### PROCESS #####
arcpy.CheckOutExtension("3D")

# Archivo TIN
out_tin = "Oconia_basin"

# Sistema de coordenadas de referencia
#SCR = arcpy.Describe(in_features).spatialReference # Utilizar SCR del entorno
SCR = 'WGS_1984_UTM_Zone_18S'

# Molde: "Archivo Parámetro_de_altura Método"
in_features = "Curva_de_Nivel.shp shape.ALTITUD masspoints"

# Recorte
arcpy.CreateTin_3d(out_tin, SCR, in_features)
