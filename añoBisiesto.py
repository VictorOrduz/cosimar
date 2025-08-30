"""
como saber si un año es bisiesto
"""
year = int(input("Introduce un año: "))

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f" el año {year} es bisiesto")
        
    else:
        print(f"el año {year} no es bisiesto")
        
es_bisiesto(year)

