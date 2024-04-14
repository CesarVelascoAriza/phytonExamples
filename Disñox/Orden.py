from Producto import Producto
class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes +=1
        self._id = Orden.contador_ordenes
        self._productos = list(productos)

    @property
    def productos(self):
        return self._productos
    @productos.setter
    def productos(self,productos):
        self._productos =productos

    def agregar_producto(self, producto):
        self._productos.append(producto)
    
    def calcular_total(self) -> float:
        total =0 
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self) -> str:
        productos_str = '|'
        for producto in self._productos:
            productos_str +=  producto.__str__() + '|'
        
        return f'Orden : {self._id}\nproductos \n{productos_str}'


if __name__=='__main__':
    producto1 = Producto('Camisa',200.02)
    producto2 = Producto('Patalon',100.01)
    productos =[producto1,producto2]
    orden1 = Orden(productos)
    print(orden1)