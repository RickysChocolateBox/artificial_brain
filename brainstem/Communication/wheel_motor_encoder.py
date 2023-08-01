import serial
import time

# Create a serial object.
ser = serial.Serial('COM3', 9600)
time.sleep(2)  # Give serial connection a bit of time to initialize

def read_from_arduino():
    while True:
        if ser.inWaiting():
            try:
                data_line = ser.readline().decode('utf-8').strip()
                motor1_val, motor2_val, motor3_val, motor4_val = map(int, data_line.split(','))
                print(f"Motor 1: {motor1_val}, Motor 2: {motor2_val}, Motor 3: {motor3_val}, Motor 4: {motor4_val}")
            except ValueError:
                print("Received malformed data. Skipping.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    read_from_arduino()

