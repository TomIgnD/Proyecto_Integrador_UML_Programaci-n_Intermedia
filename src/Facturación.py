class LineaFactura:

    def __init__(self, id_linea, cantidad, precio_unit):

        self.__id_linea = id_linea
        self.__cantidad = cantidad
        self.__precio_unit = precio_unit
        self.__subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.__cantidad * self.__precio_unit

    def get_subtotal(self):
        return self.__subtotal


class Factura:

    def __init__(self, id_factura, items_carrito):

        self.__id_factura = id_factura
        self.__lineas = []
        self.__total_final = 0

        for indice, item in enumerate(items_carrito):

            producto, cantidad = item

            precio_vta = producto.mostrar_precio()

            nueva_linea = LineaFactura(
                indice + 1,
                cantidad,
                precio_vta
            )

            self.__lineas.append(nueva_linea)

            self.__total_final += nueva_linea.get_subtotal()

    def mostrar_total(self):
        return self.__total_final
