from serial import Serial
from threading import Thread
from time import sleep


class SerialReader(Thread):
    serial = None

    def __init__(self, name, parser):
        Thread.__init__(self)
        self.name = name
        self.parser = parser

    def run(self):
        self.connect()
        self.read()

    def connect(self):  # Atuomatically detect COM port
        try:
            self.serial = Serial("COM11", 9600)
        except:
            return None

    def read(self):
        while True:
            try:
                read = self.serial.readline()
                command = read.decode().replace("\r\n", "")
                self.parser(command)
                sleep(0.2)
            except:
                break
        self.reconnect()

    def reconnect(self):
        self.serial = None
        while self.serial is None:
            self.connect()
        self.read()
