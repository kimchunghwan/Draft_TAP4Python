import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'KISSCO'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)
logging.info("info Test")

logging.debug("debug Test")
logging.warn("warn Test")
logging.error("error Test")
logging.critical("critical Test")

