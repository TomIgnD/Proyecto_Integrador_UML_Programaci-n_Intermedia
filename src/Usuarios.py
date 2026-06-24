from abc import ABC, abstractmethod
from Productos import Producto, Hardware, Software

# Clase abstracta Usuario
class Usuario(ABC):
    def __init__(self, nombre, email, contraseña):
        self.__nombre = nombre
        self.__email = email
        self.__contraseña = contraseña

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
    
    def get_contraseña(self):
        return self.__contraseña
    
    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña

    # Método abstracto, se impelmte aen las clases de Cliente y Administrador
    @abstractmethod
    def validar_credenciales(self, email, contraseña):
        pass


# Clase Cliente
class Cliente(Usuario):
    def __init__(self, nombre, email, contraseña):
        super().__init__(nombre, email, contraseña)
        self.__carrito = []
    
    # ""
    def validar_credenciales(self, email, contraseña):
        return (
            self.get_email() == email
            and self.get_contraseña() == contraseña
        )

    # Este metodo lo que hace es agregar compras al carrito, primero evalua si 
    # el stock peretnciente a la clase porducto es mayor o igual a la canitdad solicitada y 
    # lo agrega, sino manda un mensaje de error dicenido que el stock es insuficiente
    def agregar_al_carrito(self, producto: Producto, cantidad):
        if producto.stock >= cantidad:
            self.__carrito.append((producto, cantidad))
            producto.reducir_stock(cantidad)
            print(f"{cantidad} x {producto.nombre_comercial} agregado al carrito.")
        else:
            print("Stock insuficiente.")

    # Este metodo lo que hce es calcular el total a pagar de lo que se agrego en el carrito, utiliza 
    # el comando sum para sumar todos los elemetos numericos de la lista de carritos y luego limpia el carrito para 
    # poder agregar una nueva compra
    def procesar_checkout(self):
        total = sum(prod.precio_base * cant for prod, cant in self.__carrito)
        print(f"Compra procesada. Total a pagar: ${total}")
        self.__carrito.clear()


# Clase Administrador
class Administrador(Usuario):
    def __init__(self, nombre, email, contraseña):
        super().__init__(nombre, email, contraseña)
        
    # ""
    def validar_credenciales(self, email, contraseña):
        return (
            self.get_email() == email
            and self.get_contraseña() == contraseña
        )

    #Este metodo permite al administrador agregra un nuevo producto si quiere, utiliza como 
    # parametros una lista de productos y la referncia "producto" de la clase Producto
    def agregar_producto_nuevo(self, lista_productos, producto: Producto):
        lista_productos.append(producto)
        print(f"Producto {producto.nombre_comercial} agregado con éxito.")

    #Este metodo como dice su nombre repone el stock y muestra un mensaje del producto que se repuso y la cantdad; 
    # Recibe como parametro la clase Producto renombrada como producto y la cantidad.
    def reponer_stock(self, producto: Producto, cantidad):
        producto.stock += cantidad
        print(f"Stock de {producto.nombre_comercial} actualizado a {producto.stock}.")

