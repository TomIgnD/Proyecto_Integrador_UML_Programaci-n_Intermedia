from abc import ABC, abstractclassmethod

# Tiago — Módulo de Productos
# Clases:
#   - Producto (abstracta)
#   - Hardware
#   - Software
# Responsabilidades:
#   - Crear atributos privados (__id, __nombre_comercial, etc.).
#   - Getters y setters.
#   - Implementar herencia.
# Implementar:
#   - mostrar_precio()
#   - reducir_stock()
#   - calcular_elegibilidad_garantia()
#   - enviar_licencia_por_email()
# Debe entregar:
#   - Archivo o sección de código completa del módulo Productos.
#   - Ejemplos de creación de Hardware y Software.

# Tiago
# 
# Herencia de Producto → Hardware y Software.
# Encapsulamiento.

# ==============================================================================
# CONSIGNAS: MÓDULO DE PRODUCTOS (TIAGO)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CLASE BASE ABSTRACTA: Producto
# ------------------------------------------------------------------------------
# [ ] Debe ser una clase abstracta (heredar de ABC).
# [ ] Atributos Privados obligatorios (usar doble guión bajo '__'):
#     - __id (str)
#     - __nombre_comercial (str)
#     - __precio_base (int/float)
#     - __stock (int)
# [ ] Métodos Obligatorios:
#     - Constructor __init__ para inicializar todos los atributos base.
#     - Getters y setters para cada uno de los atributos privados.
#     - mostrar_precio(): Debe retornar el precio base.
#     - reducir_stock(unidades): Debe descontar la cantidad indicada del stock disponible.

class Producto (ABC):
    def __init__(self, id, nombre_comercial, precio_base, stock):
        self.__id = id
        self.__nombre_comercial = nombre_comercial
        self.__precio_base = precio_base
        self.__stock = stock
    

    # Getters de atributos privados (id, nombre_comercial, precio_base, stock)
    @property
    def id (self):
        return self.__id
    
    @property
    def nombre_comercial (self):
        return self.__nombre_comercial
    
    @property
    def precio_base (self):
        return self.__precio_base
    
    @property
    def stock (self):
        return self.__stock
    
    # Setters de atributos privados (id, nombre_comercial, precio_base, stock)
    @id.setter
    def id(self, identificador):
        self.__id = identificador

    @nombre_comercial.setter
    def nombre_comercial(self, nom_com):
        self.__nombre_comercial = nom_com
    
    @precio_base.setter
    def precio_base(self, precio_bas):
        self.__precio_base = precio_bas
    
    @stock.setter
    def stock(self, cantidad):
        self.__stock = cantidad
        
    # Metodos
    def mostrar_precio(self):
        return self.__precio_base
    
    def reducir_stock(self, cantidad):
        if (cantidad > self.stock):
            print("Error | La cantidad a descontar no puede ser mayor al stock actual")
        
        elif (cantidad == 0):
            print("Error | La cantidad a descontar no puede ser nula")

        else:
            self.__stock -= cantidad
            return f"El stock de {self.__nombre_comercial}, ahora es de: {self.__stock}"

# ------------------------------------------------------------------------------
# 2. SUBCLASE: Hardware
# ------------------------------------------------------------------------------
# [ ] Debe heredar formalmente de la clase Producto.
# [ ] Atributos Privados Específicos:
#     - __meses_garantia (int)
#     - __peso (float)
# [ ] Métodos Obligatorios:
#     - Constructor __init__ que invoque a super().__init__() obligatoriamente en su primera línea.
#     - Getters y setters para sus atributos específicos (__meses_garantia y __peso).
#     - calcular_elegibilidad_garantia(): Debe validar la cobertura técnica.

class Hardware(Producto):
    def __init__(self, id, nombre_comercial, precio_base, stock, meses_garantia, peso):
        super().__init__(id, nombre_comercial, precio_base, stock)
        self.__meses_garantia = meses_garantia
        self.__peso = peso

    # Getters de los atributos privados (meses_garantia, peso)
    @property
    def meses_garantias(self):
        return self.__meses_garantia
    
    @property
    def peso(self):
        return self.__peso
    
    #Setters de los atributos privados (meses_garantia, peso)
    @meses_garantias.setter
    def meses_garantias(self, meses):
        self.__meses_garantia = meses

    @peso.setter
    def peso(self, num_peso):
        self.__peso = num_peso

    # Metodos
    
    def calcular_elegibilidad_garantia(self):
        if (self.__meses_garantia > 0):
            return f"El producto {self.nombre_comercial} sigue estando bajo cobertura" 
        
        else:
            return f"El producto {self.nombre_comercial} no esta bajo cobertura"

# ------------------------------------------------------------------------------
# 3. SUBCLASE: Software
# ------------------------------------------------------------------------------
# [ ] Debe heredar formalmente de la clase Producto.
# [ ] Atributos Privados Específicos:
#     - __tamanio_mb (float)
#     - __clave_licencia (str)
# [ ] Métodos Obligatorios:
#     - Constructor __init__ que invoque a super().__init__() en su primera línea.
#     - Getters y setters para sus atributos específicos (__tamano_mb y __clave_licencia).
#     - enviar_licencia_por_email(): Debe simular el envío de la clave de licencia.

class Software(Producto):
    def __init__(self, id, nombre_comercial, precio_base, stock, tamanio_mb, clave_licencia):
        super().__init__(id, nombre_comercial, precio_base, stock)
        self.__tamanio_mb = tamanio_mb
        self.__clave_licencia = clave_licencia

    # Getters de los atributos privados (tamanio_mb, clave_licencia)
    @property
    def tamanio_mb(self):
        return self.__tamanio_mb
    
    @property
    def clave_licencia(self):
        return self.__clave_licencia
    
    # Setters de los atributos privados (tamanio_mb, clave_licencia)
    @tamanio_mb.setter
    def tamanio_mb(self, peso_mb):
        self.__tamanio_mb = peso_mb
    
    @clave_licencia.setter
    def clave_licencia(self, licencia):
        self.__clave_licencia = licencia

    # Metodos

    def enviar_licencia_por_email(self):
        return f"Se ha enviado la clave {self.__clave_licencia} para el producto de Software: {self.nombre_comercial} al email del cliente"
