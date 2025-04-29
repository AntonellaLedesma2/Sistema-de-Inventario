
inventario = []

def agregar_producto(nombre, precio, stock):
    producto = {"nombre": nombre, "precio": precio, "stock": stock}
    inventario.append(producto)

def listar_productos():
    for prod in inventario:
        print(f"Nombre: {prod['nombre']} | Precio: {prod['precio']} | Stock: {prod['stock']}")

def buscar_producto(nombre):
    for prod in inventario:
        if prod["nombre"].lower() == nombre.lower():
            print(f"Nombre: {prod['nombre']} | Precio: {prod['precio']} | Stock: {prod['stock']}")
            return
    print("Producto no encontrado")

def actualizar_stock(nombre, nuevo_stock):
    for prod in inventario:
        if prod["nombre"].lower() == nombre.lower():
            prod["stock"] = nuevo_stock
            print("Stock actualizado")
            return
    print("Producto no encontrado")
