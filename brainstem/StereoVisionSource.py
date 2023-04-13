import cv2
import numpy as np
import serial
import time


class StereoVisionSource:
    def __init__(self, port, left_camera_id=0, right_camera_id=1):
        self.port = port
        self.left_camera_id = left_camera_id
        self.right_camera_id = right_camera_id
        self.serial_connection = None

        # Create StereoBM object for depth calculation
        self.stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

    def connect(self):
        self.serial_connection = serial.Serial(self.port, 115200)
        time.sleep(2)  # Allow time for the connection to be established

    def capture_stereo_images(self):
        # Send command to Arduino to capture stereo images
        self.serial_connection.write(b'capture')

        # Read left and right images captured by Arduino
        left_image = self.read_image_from_serial()
        right_image = self.read_image_from_serial()

        return left_image, right_image

    def read_image_from_serial(self):
        image_data = bytearray()

        # Read image size from Arduino
        image_size = int(self.serial_connection.readline().strip())

        # Read image data from Arduino
        for _ in range(image_size):
            image_data.append(self.serial_connection.read(1))

        # Decode image data and return as OpenCV image
        return cv2.imdecode(np.array(image_data, dtype=np.uint8), cv2.IMREAD_COLOR)

    def calculate_depth(self, left_image, right_image):
        # Convert images to grayscale
        left_gray = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
        right_gray = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

        # Compute the disparity map
        disparity = self.stereo.compute(left_gray, right_gray)

        return disparity

