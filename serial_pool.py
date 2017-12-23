import serial
import time

import logging
log = logging.getLogger('ERIC.serial')

class SerialPool:
    SERIAL_BAUD_RATE = 57600

    def __init__(self):
        self.__pool = {}

    def connect(self, port, timeout):
        existing = self.__pool.get(port, None)
        if isinstance(existing, serial.Serial):
            if not existing.is_open:
                existing.open()
            if existing.is_open:
                return existing
        try:
            ser = serial.Serial(port, self.SERIAL_BAUD_RATE, timeout = timeout)
            time.sleep(2)
            if ser.is_open:
                self.__pool[port] = ser
                log.info('SERIAL: Started serial connection on Port %s' % (port))
                return ser
        except serial.SerialException as exc:
            log.error('SERIAL: %s' % (exc))
        return None
