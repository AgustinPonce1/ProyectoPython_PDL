# Pre-entrega nº2 Agustin Lucas Ponce de Leon -- 22/08/23 --
# En esta entrega me base en hacer un programa para mi empresa, tomando en cuenta cuales serian los atributos y..
# metodos que quiero que tengan mis clientes. Mas adelante ire expandiendo mas las clases y funcionalidades.

class Persona():
    # Definido el metodo constructor general de una persona.
    def __init__(self, nombre, apellido, edad, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
    
class Cliente(Persona):
    # Definido el metodo constructor de mis clientes.
    def __init__(self, nombre, apellido, edad, dni, telefono, email, direccion, categoria):
        super().__init__(nombre, apellido, edad, dni, telefono)
        self.email = email
        self.direccion = direccion
        self.categoria = categoria
        self.hist_compras = []

    # Definido el metodo __str__ para darle nombre a los objetos.
    def __str__(self):
        return f'Chequeando base de datos...\nCliente encontrado: {self.nombre} {self.apellido}\nCompras realizadas: {len(self.hist_compras)}'

    # Definida la funcion de bienvenida para cliente.
    def bienvenida(self):
        return f'Bienvenido {self.nombre} {self.apellido}, realizando compras y reclamos...\n'

    # Definida la funcion para comprar productos.
    def comprar(self, producto, cantidad):
        total = producto.precio * cantidad
        nro_compra = len(self.hist_compras) + 1
        compra = {'numero': nro_compra ,'producto': producto.nombre, 'cantidad': cantidad, 'total': total}
        self.hist_compras.append(compra)
        return f'Compra realizada.\nProducto: {producto.nombre}\nCantidad: {cantidad}\nTotal: ${total}'
    
    # Definida la funcion para reclamar productos.
    def reclamo(self, nro_compra, motivo):
        compra_respaldo = None
        for compra in self.hist_compras:
            if compra['numero'] == nro_compra:
                compra_respaldo = compra
                break
        if compra_respaldo:
            return f'Se realizo un reclamo para la compra #{nro_compra}:\nMotivo: {motivo}\nProducto: {compra_respaldo["producto"]}\nSe realizo el reembolso para el cliente.\n'
        else:
            return f'No se encontró una compra con el número #{nro_compra}'

    # Definida la funcion para ver el historial de compras.
    def ver_hist_compras(self):
        return f'Historial de compras: {self.hist_compras}'

# Cree la clase Productos para generar los mismos.
class Producto():

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Los productos ya estaran permanentemente definidios por que son parte de la tienda.
producto1_aluminio = Producto(nombre='Juego de Sillones de Aluminio', precio=7000)
producto2_aluminio = Producto(nombre='Aluminio + WPC -> Barra + Banquetas', precio=6032)
producto3_aluminio = Producto(nombre='Mesa ratona de aluminio', precio=1200)

# Gracias por ver <3