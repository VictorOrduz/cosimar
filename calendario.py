"""
Calendario
"""
# importamos 2 librerias 
import calendar
from datetime import datetime

# funcion para crear el calendario 
def calendario():
    hoy = datetime.now()
    dia = hoy.day
    mes = hoy.month
    año = hoy.year
    
    calendario = calendar.month(año, mes)
    
    cal_col = calendario.replace(f"{dia:2}", f"\033[91m{dia:2}\033[0m") # cambiamos el color por medio del codigo 'ansi escape'
    
    print(cal_col)
    
calendario()
