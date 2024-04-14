from Orden import Orden
from Producto import Producto


def main():
    producto1   = Producto('camisa',56.40)
    producto2   = Producto('pantalon',56.40)
    producto3   = Producto('chaqueta',42.40)
    producto4   = Producto('medias',60.40)
    productos = [producto1,producto2,producto3,producto4]
    orden1 = Orden(productos)
    print(orden1)
    print(f'calcular orden total {orden1.calcular_total()}')
    order2 = Orden(productos)
    producto10  = Producto('compultado',2506.40)
    order2.agregar_producto(producto10)
    print(order2)
    print(f'calcular orden total {order2.calcular_total()}')



if __name__=="__main__":
    main()