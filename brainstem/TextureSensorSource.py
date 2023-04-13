import serial
import smbus
import spidev
import time

class TextureSensorSource:
    def __init__(self, sensor_type, port=None, bus_number=None, sensor_address=None):
        self.sensor_type = sensor_type
        self.port = port
        self.bus_number = bus_number
        self.sensor_address = sensor_address
        self.serial_connection = None
        self.i2c_connection = None

        if self.sensor_type == "biotac_sp" or self.sensor_type == "biotac_toccare":
            if self.port:
                self.serial_connection = serial.Serial(self.port, 115200)
            else:
                raise ValueError("Serial port is required for BioTac sensors.")
        elif self.sensor_type == "optoforce":
            if self.bus_number is not None and self.sensor_address is not None:
                self.i2c_connection = smbus.SMBus(self.bus_number)
            else:
                raise ValueError("I2C bus number and sensor address are required for OptoForce sensors.")
        else:
            raise ValueError("Invalid sensor_type. Supported types are 'biotac_sp', 'biotac_toccare', and 'optoforce'.")

    def read_data(self):
        if self.sensor_type == "biotac_sp" or self.sensor_type == "biotac_toccare":
            return self.read_biotac_data()
        elif self.sensor_type == "optoforce":
            return self.read_optoforce_data()

    def read_biotac_data(self):
        # Assuming BioTac sensor uses SPI communication protocol
        # Replace CHANNEL and DEVICE with the appropriate values for your setup
        CHANNEL = 0
        DEVICE = 0
        spi = spidev.SpiDev()
        spi.open(CHANNEL, DEVICE)
        spi.max_speed_hz = 1000000  # 1MHz

        # Send request for data
        request = [0x00]  # Replace with the appropriate request command for the BioTac sensor
        response = spi.xfer(request)

        # Parse response data according to the BioTac sensor's documentation
        # ...

        spi.close()
        return parsed_data


    def read_optoforce_data(self):
        # Assuming OptoForce sensor uses I2C communication protocol
        # Read data from the I2C device
        data = self.i2c_connection.read_i2c_block_data(self.sensor_address, 0, 6)

        # Parse the received data according to the OptoForce sensor's documentation
        # ...

        return parsed_data
