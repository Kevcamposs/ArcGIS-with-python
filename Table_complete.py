def parameter(ALTITUD):
    return str(round(ALTITUD)*10 % 5000)
    # En SQL, mod(round("ALTITUDE",0)*10,5000)=0
    # función mod calcula el módulo (resto) de una división. mod(x,y) <> x % y
    # función round redondea un float o double al número de decimales indicado.

parameter(!ALTITUD!)

def Type(parameter):
    if parameter == 0:
        return "Primaria"
    else:
        return "Secundario"

Type( !Parameter!)
