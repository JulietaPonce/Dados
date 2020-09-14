import random

def suma_dados():
    #Función para tirar los dados y sumarlos.
    a = int((random.random()*10)%6+1)
    b = int((random.random()*10)%6+1)
    resultado = a + b
    print("El primer dado tiró el número ",a,\
        " y el segundo dado tiró el número ",b,". El resultado es: ",resultado)
    return


def tirar_nuevamente(prompt):
    #Función para preguntar por una nueva tirada
    while True:
        ok = input(prompt)
        if ok in ("Sí", "SI", "sí"):   
            return True
        print(suma_dados())
        if ok in ("No", "no", "NO"):
            print("¡Gracias por utilizar mi programa!")
            return False


print(suma_dados())
tirar_nuevamente("¿Desea tirar nuevamente los dados?")