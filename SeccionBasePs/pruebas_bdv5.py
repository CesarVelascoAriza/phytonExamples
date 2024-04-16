import psycopg2
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='test'
    )

try:
    with conexion:
        with conexion.cursor() as cursor:
           sentencia = 'insert into persona(nombre, apellido , mail) values (%s,%s,%s)'
           valores =(
               ('carlos','relara','clara@gmail.com'),
               ('marcos','quintana','marcos@gmail.com'),
               ('marcos','marrana','marcos123@gmail.com'),
               )
           #insertcion de un solo registro
           #cursor.execute(sentencia,valores)
           cursor.executemany(sentencia,valores)
           #conexion.commit()
           registros_insertados = cursor.rowcount
           print(f'registros insertados {registros_insertados}')
except Exception as e:
    print(f"ocurrio un error : {e} ")
finally:
    conexion.close()