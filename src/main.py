from Productos import Hardware, Software
from Usuarios import Cliente, Administrador
from Compras import Compras
from Facturacion import Factura


# DATOS INICIALES


productos = [
    Hardware(1, "Mouse Gamer", 15000, 10, 12, 0.5),
    Software(2, "Windows 11", 50000, 5, 6000, "ABC-123")
]

cliente = Cliente(
    "Tomas",
    "tomas@gmail.com",
    "1234"
)

admin = Administrador(
    "Admin",
    "admin@gmail.com",
    "admin123"
)

carrito = Compras()


# MENU


while True:

    print("===== Electrodomesticos Pepe =====")
    print("1. Ver productos")
    print("2. Agregar al carrito")
    print("3. Ver total")
    print("4. Finalizar compra")
    print("5. Reponer stock")
    print("6. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":

        for producto in productos:
            print(
                producto.id,
                producto.nombre_comercial,
                "$" + str(producto.precio_base),
                "Stock:",
                producto.stock
            )

    elif opcion == "2":

        id_producto = int(input("ID producto: "))
        cantidad = int(input("Cantidad: "))

        for producto in productos:
            if producto.id == id_producto:
                carrito.agregar_producto(
                    producto,
                    cantidad
                )

    elif opcion == "3":

        print(
            "Total:",
            carrito.calcular_total()
        )

    elif opcion == "4":

        factura = Factura(
            1,
            carrito.productos
        )

        print(
            "Total factura:",
            factura.mostrar_total()
        )

        carrito.generar_factura()

    elif opcion == "5":

        id_producto = int(input("ID producto: "))
        cantidad = int(input("Cantidad a reponer: "))

        for producto in productos:
            if producto.id == id_producto:
                admin.reponer_stock(
                    producto,
                    cantidad
                )

    elif opcion == "6":
        break
