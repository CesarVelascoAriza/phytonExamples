
from MiClase import MiClase

def main():
    #variable estatica de mi clase 
    print (MiClase.variable)
    #acceder al valor de la seguntada variable 
    miClase = MiClase('instacia de la clase')
    print(miClase.variable_instancia)
    print(miClase.variable)

if __name__=="__main__":
    main()