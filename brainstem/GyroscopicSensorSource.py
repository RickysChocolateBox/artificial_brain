import smbus2 as smbus
import time

class GyroscopicSensorSource:
    def __init__(self):
        self.address = 0x68
        self.bus = smbus.SMBus(1)
        self.data = None
        self.connect()

    def connect(self):
        # Wake up the MPU-6050
        self.bus.write_byte_data(self.address, 0x6B, 0)

    def read_data(self):
        # Read the accelerometer and gyroscope data from the MPU-6050
        raw_data = [self.bus.read_byte_data(self.address, i) for i in range(0x3B, 0x3F+1)]

        # Convert the raw data to signed 16-bit integers
        data = [((raw_data[i] << 8) | raw_data[i+1]) for i in range(0, len(raw_data), 2)]
        for i in range(len(data)):
            if data[i] >= 0x8000:
                data[i] -= 0x10000

        # Update the data attribute
        self.data = {
            'accel_x': data[0],
            'accel_y': data[1],
            'accel_z': data[2],
            'gyro_x': data[3],
            'gyro_y': data[4],
            'gyro_z': data[5]
        }

    def get_data(self):
        self.read_data()
        return self.data