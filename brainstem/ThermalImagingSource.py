import cv2
import threading
import numpy as np
import time

class ThermalImagingSource:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.camera = None
        self.frame = None
        self.lock = threading.Lock()
        self.is_running = False
        self.thread = None

    def connect(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(self.camera_id)
            if not self.camera.isOpened():
                raise RuntimeError(f"Error opening thermal imaging camera with ID: {self.camera_id}")

            self.is_running = True
            self.thread = threading.Thread(target=self._update_frames)
            self.thread.start()

    def _update_frames(self):
        while self.is_running:
            ret, frame = self.camera.read()
            if not ret:
                raise RuntimeError("Error reading frame from thermal imaging camera")

            frame = self.process_frame(frame)

            with self.lock:
                self.frame = frame

            time.sleep(0.01)  # Add a small delay to prevent excessive CPU usage

    def process_frame(self, frame):
        # Apply a colormap
        frame = cv2.applyColorMap(frame, cv2.COLORMAP_JET)

        # Apply Gaussian filtering
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        # Normalize pixel values
        frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)

        return frame

    def read_frame(self):
        if self.camera is None:
            raise RuntimeError("Thermal imaging camera not connected")

        with self.lock:
            return self.frame.copy() if self.frame is not None else None

    def disconnect(self):
        if self.camera is not None:
            self.is_running = False
            if self.thread is not None:
                self.thread.join()

            self.camera.release()
            self.camera = None
