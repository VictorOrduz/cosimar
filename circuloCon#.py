
"""
dibujar un circulo usando el simbolo #
"""

r = 4

for x in range(-r, r + 1):
    for y in range(-r, r + 1):
        
        if x * x + y * y <= r * r:
            print(" # ", end = "")
        else:
            print(" . ", end = "")
            
    print()