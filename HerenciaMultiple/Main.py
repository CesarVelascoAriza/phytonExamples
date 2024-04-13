from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


def main():
    print('Creacion de los objetos'.center(50,'*'))

    cuadrado  = Cuadrado(5,'rojo')
    print(f'Area del cuadrado : {cuadrado.calcular_area()}')
    print(cuadrado)
    #MRO - method resolution order
    print(Cuadrado.mro())

    rectangulo = Rectangulo(3,8,'verde')
    print(f'Area del Rectangulo {rectangulo.calcular_area()}')
    print(rectangulo)

    print('fin de los objetos'.center(50,'*'))



if __name__=="__main__":
    main()