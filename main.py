# main.py

import productos

while True:
    print("\n1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar stock")
    print("5. Salir")

    op = input("Opción: ")

    if op == "1":
        n = input("Nombre: ")
        p = float(input("Precio: "))
        s = int(input("Stock: "))
        productos.agregar_producto(n, p, s)

    elif op == "2":
        productos.listar_productos()

    elif op == "3":
        n = input("Nombre a buscar: ")
        productos.buscar_producto(n)

    elif op == "4":
        n = input("Nombre: ")
        s = int(input("Nuevo stock: "))
        productos.actualizar_stock(n, s)

    elif op == "5":
        break

    else:
        print("Opción inválida")
