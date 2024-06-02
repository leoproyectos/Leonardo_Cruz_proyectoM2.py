#funcion para conocer la longitud de la palabra y saber si cumple la condicion.
def longitud_palabra(palabra):
    longitud = len(palabra)
    
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")
longitud_palabra(palabra)

#La definicion de las cordenadas con verificacion si una cordenada tiene 0
def cuadrante(x, y):
    if x == 0 or y == 0:
        return "Error: Una o ambas coordenadas son cero. Por favor ingresa coordenadas válidas."
    elif x > 0 and y > 0:
        return "El punto se encuentra en el primer cuadrante."
    elif x < 0 and y > 0:
        return "El punto se encuentra en el segundo cuadrante."
    elif x < 0 and y < 0:
        return "El punto se encuentra en el tercer cuadrante."
    elif x > 0 and y < 0:
        return "El punto se encuentra en el cuarto cuadrante."

# Solicitar al usuario que ingrese las coordenadas (x, y)
x = float(input("Ingresa la coordenada x: "))
y = float(input("Ingresa la coordenada y: "))

print(cuadrante(x, y))
