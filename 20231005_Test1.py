#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importamos el módulo para obtener la fecha y hora actual
import datetime

# Obtenemos la hora actual
hora_actual = datetime.datetime.now()

# Comparamos la hora actual para determinar si es "buenos días", "buenas tardes" o "buenas noches"
if hora_actual.hour < 12:
    saludo = "Buenos días"
elif hora_actual.hour < 18:
    saludo = "Buenas tardes"
else:
    saludo = "Buenas noches"

# Imprimimos el saludo
print(f"{saludo}, ¡Hola!")



#Per executar l'escript, hem d'obrir una nova terminal i crear un
#nou fitxer amb el contingut de l'escript, el guardem i despres li donem
#privilegis d'execució amb chmod +x nomScript.py, finalment l'executem amb
#./nomScript.py