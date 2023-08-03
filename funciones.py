#FUNCIONES -- PROYECTO AGUSTIN LUCAS PONCE DE LEON

#FUNCION PARA EL REGISTRO DE USUARIOS - SI EL USUARIO YA EXISTE, DIRA QUE YA EXISTE.
def registro_user():

    usuarios_registrados = {
        'test':'test'
    }

    while True:
        usuario_creado = input('Cree un nombre de usuario: ')

        if usuario_creado in usuarios_registrados:
            print('Error: El nombre de usuario ya existe.')
        else:
            contrasena_creada = input('Cree su contraseña: ')
            usuarios_registrados[usuario_creado] = contrasena_creada
            print(f'Bienvenido al sistema, ingrese sus datos nuevamente para el logeo...')
            break

    return usuario_creado, contrasena_creada, usuarios_registrados

#FUNCION PARA EL LOGEO DE USUARIOS YA REGISTRADOS
def login(usuario, contrasena, usuarios_registrados):
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena:
        return True
    else:
        return False
    
#FUNCION PARA MOSTRAR DATOS INGRESADOS HASTA EL MOMENTO
def mostrar_informacion(usuarios_registrados, usuario):
    if usuario in usuarios_registrados:
        return usuarios_registrados[usuario]
    else:
        return None

#FUNCION PARA GUARDAR LOS REGISTROS GUARDADOS EN UN TXT
import json 

def archivo(archivo_name, info):
    with open(archivo_name, 'a') as f:
        json.dump(info, f)
        f.write('\n')
