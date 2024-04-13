
from MiClase import MiClase
from Constantes import *
from ConstantesClase import ContantesClase
def main():
    #Constantes
    print (MI_CONSTANTE)

    print(ContantesClase.PI)
    #variable estatica de mi clase 
    print (MiClase.variable)
    #metodo estatico 
    print(MiClase.metodo_static())
    #acceder al valor de la seguntada variable 
    miClase = MiClase('instacia de la clase')
    print(miClase.variable_instancia)
    print(miClase.variable)

if __name__=="__main__":
    main()