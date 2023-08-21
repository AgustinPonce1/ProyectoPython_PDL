#FUNCIONES PYTHON -- PROYECTO AGUSTIN LUCAS PONCE DE LEON -- 01/08/2023

from users import * #Traer el diccionario de users ("BDD")

#FUNCION PARA EL REGISTRO DE USUARIOS - SI EL USUARIO YA EXISTE, DIRA QUE YA EXISTE.
def registro_user():

    while True:
        usuario_creado = input('Cree un nombre de usuario: ')

        if usuario_creado in usuarios_registrados: #Compara si el nombre de usuario ingresado ya existe en la BDD...
            print('Error: El nombre de usuario ya existe.') 
        else:
            contrasena_creada = input('Cree su contraseña: ')
            usuarios_registrados[usuario_creado] = contrasena_creada #Guarda la contraseña con el usuario creado...
            print(f'Bienvenido al sistema, ingrese sus datos nuevamente para el logeo...')
            break

    return usuario_creado, contrasena_creada, usuarios_registrados

#FUNCION PARA EL LOGEO DE USUARIOS YA REGISTRADOS
# -- Bucle de logeo, si el usuario o contraseña es incorrecta, volvera a pedirla (funciona por separado). 
def login(usuario, contrasena, usuarios_registrados):
    return usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena

def login_usuario(usuarios_registrados):
    while True:
        usuario_ingresado = input("Ingrese su nombre de usuario: ")

        if usuario_ingresado not in usuarios_registrados: #Si el usuario NO esta en la BDD...
            print("El nombre de usuario ingresado no existe, vuelva a intentarlo.")
        else:
            break

    while True:
        contrasena_ingresada = input("Ingrese su contraseña: ")
        
        if usuarios_registrados[usuario_ingresado] != contrasena_ingresada: #Si la contraseña es != a la del usuario ingresado...
            print("La contraseña es incorrecta, vuelva a intentarlo.")
        else:
            break

    if login(usuario_ingresado, contrasena_ingresada, usuarios_registrados): #Si todos los datos son coincidentes...
        print("Sesión iniciada correctamente, bienvenido.")

#FUNCION PARA MOSTRAR DATOS INGRESADOS HASTA EL MOMENTO
def mostrar_informacion(usuarios_registrados):
    usuario_requerido = input("De qué usuario deseas obtener información: ")

    if usuario_requerido in usuarios_registrados:
        print(f"Información solicitada: Usuario: {usuario_requerido}; Contraseña: {usuarios_registrados[usuario_requerido]}")
    else:
        print(f"El usuario {usuario_requerido} no está registrado.")

#FUNCION PARA GUARDAR LOS REGISTROS GUARDADOS EN UN TXT
import json 

def archivo(archivo_name, info):
    txt = input('Desea guardar los datos en un TXT: "SI" - "NO": ') #Confirmar accion o denegar.

    if txt == ("SI") or txt == ("si"):
        with open(archivo_name, 'w') as f: #Guardar en archivo (reemplazara lo que ya existia)
            json.dump(info, f)
            f.write('\n')
        print(f'Se guardaron correctamente los registros.')
    else:
        print(f'No se guardó ningún archivo.')



