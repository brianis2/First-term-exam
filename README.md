# CRUD de Usuarios + Prueba controlada de fuerza bruta contra API propia

## Descripción
Este proyecto usa una API REST con FastAPI para gestionar usuarios con operaciones CRUD y autenticación básica con login. Se agrega un script hecho en Python para realizar una prueba de fuerza bruta contra el endpoint /login de la propia API.

## Objetivo
Comprender cómo funcionan los endpoints CRUD en una API REST, cómo se realiza un proceso de autenticación simple y cómo una contraseña débil puede ser vulnerable cuando se usa un ataque de fuerza bruta.

## Herramientas Usadas
- Python 3
- FastAPI
- SQLModel
- Uvicorn
- Requests
- WSL Ubuntu

## Estructura del proyecto
- main.py: API con CRUD de usuarios y endpoint de login.
- bruteforce.py: script de fuerza bruta controlada contra la API.
- README.md: documentación del proyecto.

## Modelo de usuario
El modelo de usuario contiene los siguientes campos:
- id: identificador del usuario
- username: nombre de usuario único
- password: contraseña
- email: correo opcional
- is_active: estado del usuario

## Endpoints implementados

GET /
Verifica que la API está funcionando.

GET /users
Lista todos los usuarios.

GET /users/{user_id}
Obtiene un usuario específico por su id.

POST /users
Crea un nuevo usuario.

PUT /users/{user_id}
Actualiza un usuario existente, excepto la contraseña.

DELETE /users/{user_id}
Elimina un usuario.

POST /login
Autentica un usuario con username y password.

Cómo ejecutar la API

1. Abrir Ubuntu o terminal WSL.
2. Entrar a la carpeta del proyecto:

bash de Ubuntu
cd api_proyecto
