import time
import numpy as np
from sklearn.cluster import DBSCAN


class LiDARSource:
    def __init__(self, port):
        self.port = port
        self.serial_connection = None

    def connect(self):
        self.serial_connection = serial.Serial(self.port, 115200)
        time.sleep(2)  # Allow time for the connection to be established
 
    def read_data(self):
        lidar_data = []

        while True:
            line = self.serial_connection.readline().decode("utf-8").strip()

            if line == "END":
                break

            values = line.split(',')
            x, y, z = float(values[0]), float(values[1]), float(values[2])
            lidar_data.append([x, y, z])

        return np.array(lidar_data)
        return lidar_data

    def apply_filter(self, lidar_data, distance_threshold=1.0):
        filtered_data = lidar_data[lidar_data[:, 2] < distance_threshold]
        return filtered_data

    def cluster_data(self, lidar_data, eps=0.5, min_samples=5):
        clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(lidar_data)
        return clustering.labels_

    def process_lidar_data(self, lidar_data):
        # Apply filter (optional)
        filtered_data = self.apply_filter(lidar_data, distance_threshold=1.0)

        # Apply clustering (optional)
        clustered_data = self.cluster_data(filtered_data, eps=0.5, min_samples=5)

        return clustered_data


