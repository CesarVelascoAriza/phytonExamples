from logger_base import log
import psycopg2 as pg
import sys
class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD ='admin'
    _PORT ='5432'
    _HOST ='localhost'
    _conexion = None
    _curson =None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = pg.connect(host=cls._HOST, user=cls._USERNAME, password =cls._PASSWORD, port=cls._PORT, database = cls._DATABASE)
                log.info(f'conexion exitosa {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'ocurrio una exception en la conexion : {e}')
                sys.exit()
        else:
            return cls._conexion
    
    @classmethod
    def obtener_cursor(cls):
        if cls._curson is None:
            try:
                cls._curson =cls.obtener_conexion().cursor()
                log.info(f'se abrio correctamete el cursor : {cls._curson}')
            except Exception as e:
                log.error(f'error en la obtencion del cursor {e}')
                sys.exit()
        else:
            return cls._curson


if __name__=='__main__':
    Conexion.obtener_conexion()
    Conexion.obtener_cursor()