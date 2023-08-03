## PRIMERA PRE-ENTREGA DEL PROYECTO  
## -- FUNCIONALIDADES DE REGISTRO Y LOG IN A
## -- ALMACENAMIENTO DE USUARIOS EN UNA "BASE DE DATOS", SIMULANDO SU USO CON DICCIONARIOS

from funciones import * #Funciones Importadas del archivo "Funciones"

#Inicio del programa
print(f'Bienvenido a mi programa, a continuacion realice su registro...')

usuario_creado, contrasena_creada, usuarios_registrados = registro_user() #Registro realizado.

#Bucle de logeo, si el usuario o contraseña es incorrecta, volvera a pedirla (funciona por separado).
while True:    
    while True:
        usuario_ingresado = input("Ingrese su nombre de usuario: ")

        if usuario_ingresado != usuario_creado:
            print(f'El nombre de usuario ingresado no existe, vuelva a intentarlo: ')
        else:
            usuario_ingresado == usuario_creado 
            break
        
    while True:
        contrasena_ingresada = input("Ingrese su contraseña: ")

        if contrasena_ingresada != contrasena_creada:
            print(f'La contraseña es incorrecta, vuelva a intentarlo: ')
        else:
            contrasena_ingresada == contrasena_creada
            break

    if login(usuario_ingresado, contrasena_ingresada, usuarios_registrados): #En esta parte, el programa chequea que los tres datos coincidan con los de la "bdd".
        print(f'Sesion iniciada correctamente, bienvenido.')
        break

#Informacion de los usuarios registrados (con peticion de usuario).
usuario_requerido = input("De que usuario deseas obtener informacion: ")
info_mostrada = mostrar_informacion(usuarios_registrados, usuario_requerido)

if info_mostrada:
    print(f"Informacion solicitada: Usuario:{usuario_requerido}; Contraseña:{info_mostrada}")
else:
    print(f"El usuario {usuario_requerido} no está registrado.")

#Informacion de los usuarios registrados en un .json (con confirmacion).
txt = input('Desea guardar los datos en un TXT: "SI" - "NO": ') #Guardar datos de registro en TXT.
if txt == ("SI") or txt == ("si"):
    archivo('registros.json', usuarios_registrados)
    print(f'Se guardaron correctamente los registros.')
else:
    print(f'No se guardo ningun archivo.')