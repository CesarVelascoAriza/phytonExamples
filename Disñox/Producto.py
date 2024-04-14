class Producto:
    contador_producto=0

    def __init__(self,nombre,precio):
        Producto.contador_producto += 1
        self._id =Producto.contador_producto
        self._nombre = nombre
        self._precio = precio


    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def precio(self) -> float :
        return self._precio
    @precio.setter
    def precio(self,precio):
        self._precio = precio

    def __str__(self) -> str:
        return f'{self._id } {self._nombre} {self._precio}'