
"""
dibujar un circulo usando el simbolo #
"""

# radio del circulo = 4
r = 4

for x in range(-r, r + 1): # recorre las coordenadas desde -4 hasta 4
    for y in range(-r, r + 1): # recorre las coordenadas desde -4 hasta 4

        # condicion matematica; formula del circulo
        if x * x + y * y <= r * r:
            print(" # ", end = "") # si cummple la condicion matematica, imprime # dentro y en el limte del circulo
        else:
            print("   ", end = "") # si no cumple la condicion matematica, imprime espacio fuera del circulo
            
    print()
