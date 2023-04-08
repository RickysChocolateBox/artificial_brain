import numpy as np
import cv2

class DataAugmentation:
    def __init__(self, rotation_range=0, zoom_range=0, horizontal_flip=False, vertical_flip=False):
        self.rotation_range = rotation_range
        self.zoom_range = zoom_range
        self.horizontal_flip = horizontal_flip
        self.vertical_flip = vertical_flip

    def rotate_image(self, image):
        angle = np.random.uniform(-self.rotation_range, self.rotation_range)
        height, width = image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1.0)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)
        return rotated_image

    def zoom_image(self, image):
        zoom_factor = np.random.uniform(1-self.zoom_range, 1+self.zoom_range)
        height, width = image.shape[:2]
        zoom_matrix = cv2.getAffineTransform(np.float32([[0,0],[width,0],[0,height]]), \
            np.float32([[0,0],[width*zoom_factor,0],[0,height*zoom_factor]]))
        zoomed_image = cv2.warpAffine(image, zoom_matrix, (width, height), flags=cv2.INTER_LINEAR)
        return zoomed_image

    def flip_image(self, image):
        if self.horizontal_flip and self.vertical_flip:
            flip_mode = -1
        elif self.horizontal_flip:
            flip_mode = 1
        elif self.vertical_flip:
            flip_mode = 0
        else:
            return image
        flipped_image = cv2.flip(image, flip_mode)
        return flipped_image

    def augment_data(self, image):
        transformed_image = image.copy()
        if self.rotation_range != 0:
            transformed_image = self.rotate_image(transformed_image)
        if self.zoom_range != 0:
            transformed_image = self.zoom_image(transformed_image)
        if self.horizontal_flip or self.vertical_flip:
            transformed_image = self.flip_image(transformed_image)
        return transformed_image

