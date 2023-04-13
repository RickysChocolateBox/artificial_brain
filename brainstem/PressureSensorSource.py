import serial
import time

class PressureSensorSource:

    def __init__(self, port, baud_rate=9600):
        self.port = port
        self.baud_rate = baud_rate
        self.serial_connection = None

    def connect(self):
        self.serial_connection = serial.Serial(self.port, self.baud_rate)
        time.sleep(2)  # Allow some time for the connection to be established

    def read_pressure(self):
        if self.serial_connection is None:
            raise RuntimeError("You must connect to the sensor before reading the pressure.")

        # Read the pressure value sent by the Arduino
        pressure_data = self.serial_connection.readline().decode().strip()
        return pressure_data

    def close(self):
        if self.serial_connection is not None:
            self.serial_connection.close()


