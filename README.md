from Productos import Producto

class Carrito:

    def __init__(self):
        # Lista donde se guardan los productos y sus cantidades
        self.productos = []

    def agregar_producto(self, producto, cantidad=1):

        # Calcula cuántos productos hay en total en el carrito
        total = 0
        for prod, cant in self.productos:
            total += cant

        # Verifica que no se superen los 50 productos
        if total + cantidad > 50:
            print("No se pueden agregar más de 50 productos.")
            return

        # Verifica que haya stock suficiente
        if producto.stock < cantidad:
            print("No hay suficiente stock.")
            return

        # Busca si el producto ya está en el carrito
        for i in range(len(self.productos)):
            prod, cant = self.productos[i]

            if prod.id == producto.id:
                # Si existe, aumenta la cantidad
                self.productos[i] = (prod, cant + cantidad)
                print("Producto agregado.")
                return

        # Si no existe, lo agrega al carrito
        self.productos.append((producto, cantidad))
        print("Producto agregado.")

    def calcular_total(self):
        # Acumula el precio total de la compra
        total = 0

        for prod, cant in self.productos:
            total += prod.precio_base * cant

        return total

    def vaciar_carrito(self):
        # Elimina todos los productos del carrito
        self.productos.clear()
        print("Carrito vaciado.")

    def generar_factura(self):

        # Verifica que el carrito no esté vacío
        if len(self.productos) == 0:
            print("El carrito está vacío.")
            return

        print("Procesando compra...")

        # Descuenta del stock los productos comprados
        for prod, cant in self.productos:
            prod.reducir_stock(cant)

        # Muestra el total de la compra
        print("Total a pagar:", self.calcular_total())

        # Vacía el carrito después de la compra
        self.productos.clear()

        print("Compra finalizada.")
