from logger_base import log
from Conexion import Conexion
from Persona import Persona
class PersonaDAO:
    '''
    DAO (data Access Object)

    '''
    _SELECT = 'SELECT * FROM PERSONA ORDER BY ID_PERSONA'
    _INSERT = 'INSERT INTO PERSONA (nombre, apellido, email), VALUES (%s,%s,%s)' 
    _ACTUALIZAR = 'UPDATE PERSONA SET nombre = %s, apellido= %s, email =%s WHERE ID_persona = %s'
    _ELIMINAR = 'DELETE FROM  PERSONA WHERE ID_PERSONA = %s'

    @classmethod
    def seleccionar(cls):
        with  Conexion.obtener_cursor() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtener_conexion():
            with  Conexion.obtener_cursor() as cursor:
                log.debug(f'persona a insertar :{persona}')
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERT,valores)
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtener_conexion():
            with  Conexion.obtener_cursor() as cursor:
                log.debug(f'persona a actializar :{persona}')
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtener_conexion():
            with  Conexion.obtener_cursor() as cursor:
                log.debug(f'persona a actializar :{persona}')
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                return cursor.rowcount


if __name__=='__main__':
    #insertar un registro
    persona1 = Persona(nombre='pedrito',apellido='navajas',email='pedrito@gmail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'personas insertadas {personas_insertadas}')
    #seleccionar todos los registros 
    personas = PersonaDAO().seleccionar()
    for persona in personas:
        log.debug(persona)

    #Actualizar el registro
    personaA = Persona(1,'pedro','najeras','pernajeras@gmail.com')
    personas_actualizadas = PersonaDAO.actualizar(personaA)
    log.debug(f'personas actualizadas : {personas_actualizadas}' )
    #eliminar persona
    persona = Persona(id_persona=1)
    personas_eliminadas = PersonaDAO.eliminar(persona)
    log.debug(f'personas eliminada : {personas_eliminadas}' )
