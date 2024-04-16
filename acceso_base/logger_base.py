import logging as log

log.basicConfig(
    level= log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I:%M:%S %p',
    handlers=[
        log.FileHandler('capa_datos.log'),
        log.StreamHandler()
    ]
)



if __name__=='__main__':
    log.debug('mesaje a debug')
    log.info('mensaje a ifo')
    log.warning('level warning')
    log.error('errror')
    log.critical('critical')