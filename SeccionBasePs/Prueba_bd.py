
'''forma basica de conexion a posgrest'''
import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='test'
    )
cusor = conexion.cursor()

sentencia = ''
cusor.execute(sentencia)
registros = cusor.fetchall()
print(registros)
cusor.close()
conexion.close()