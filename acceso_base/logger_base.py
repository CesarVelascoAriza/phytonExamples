import logging as log

log.basicConfig(
    level= log.DEBUG
)

if __name__=='__main__':
    log.debug('mesaje a debug')
    log.info('mensaje a ifo')
    log.warning('level warning')
    log.error('errror')
    log.critical('critical')