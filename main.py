# Pre-entrega nº2 Agustin Lucas Ponce de Leon -- 22/08/23 -- PROGRAMA PYTHON 
# ARCHIVO DONDE PROBAR EL PROGRAMA.

from paquete_agustin.objetos.clases import Cliente, Producto # Añadida importacion de las clases creadas
from paquete_agustin.objetos.clases import producto1_aluminio, producto2_aluminio, producto3_aluminio # Añadida importacion de productos.
from paquete_agustin.register_login import * # Añadida importacion de register/login de la entrega anterior.

# Creacion del Cliente.
cliente1 = Cliente("Juani", "Frasson", "22", "39519501", "1122786962", "juan@gmail.com", "direccion1", "Regular")
# Bienvenida al cliente.
print(cliente1.bienvenida())
# Realizar una compra.
print(cliente1.comprar(producto1_aluminio, cantidad=2))
# Realizar un reclamo a la tienda.
numero_compra_reclamo = 1
motivo_reclamo = "Producto defectuoso"
print(cliente1.reclamo(numero_compra_reclamo, motivo_reclamo))
# Imprimir historial de compras.
print(cliente1.ver_hist_compras())
# Buscar cliente creado en supuesta base de datos (usando metodo str).
print(cliente1)

