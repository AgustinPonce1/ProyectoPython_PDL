## PRIMERA PRE-ENTREGA DEL PROYECTO  
## -- FUNCIONALIDADES DE REGISTRO Y LOG IN A
## -- ALMACENAMIENTO DE USUARIOS EN UNA "BASE DE DATOS", SIMULANDO SU USO CON DICCIONARIOS

from funciones import * #Funciones Importadas del archivo "Funciones"

#Inicio del programa
print(f'Bienvenido a mi programa, a continuacion complete su registro...')

#Registro (explicacion en funciones.py)
usuario_creado, contrasena_creada, usuarios_registrados = registro_user()

#Log In (explicacion en funciones.py)
login_usuario(usuarios_registrados)

#Informacion de los usuarios registrados (con peticion de usuario).
mostrar_informacion(usuarios_registrados)

#Informacion de los usuarios registrados en un .json (con confirmacion).
archivo('registros.json', usuarios_registrados)