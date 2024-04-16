import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='test'
    )
#actualizacion de varios registros
try:
    #conexion.autocommit = False #linea por default
    cursor = conexion.cursor()
    sentencia = 'insert into persona (nombre, apellido, email) values (%s,%s,%s) '
    valores =('maria', 'parra','manzana@gmail.com')
    cursor.execute(sentencia,valores)
    conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f"ocurrio un error : {e} ")
finally:
    conexion.close()