import serial
import threading

class ExternalHeatSensorSource:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.serial_connection = serial.Serial(self.port, self.baud_rate)
        self.temperature = None
        self.read_data_thread = threading.Thread(target=self.read_data)
        self.read_data_thread.daemon = True
        self.read_data_thread.start()

    def read_data(self):
        while True:
            # Read data from the Arduino
            self.serial_connection.write(b'1')  # Send a request for data (change this if needed)
            data = self.serial_connection.readline().decode().strip()
            
            try:
                self.temperature = float(data)
            except ValueError:
                print("Invalid data received from the external heat sensor. Please check the connection.")
                self.temperature = None

    def get_temperature(self):
        return self.temperature
