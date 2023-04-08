import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import turtle
# Julia Set
class JuliaSet:
    def __init__(self, width=800, height=800, max_iter=1000):
        self.width = width
        self.height = height
        self.max_iter = max_iter

    def julia(self, x, y, c):
        z = complex(x, y)
        for i in range(self.max_iter):
            z = z * z + c
            if abs(z) > 2.0:
                return i
        return self.max_iter

    def generate(self, c=complex(-0.7, 0.27015)):
        img = Image.new('RGB', (self.width, self.height), 'white')
        pixels = img.load()

        for x in range(self.width):
            for y in range(self.height):
                zx, zy = x * (3.0 / self.width) - 1.5, y * (2.0 / self.height) - 1.0
                c_value = self.julia(zx, zy, c)
                r, g, b = c_value % 8 * 32, c_value % 16 * 16, c_value % 32 * 8
                pixels[x, y] = (r, g, b)

        img.show()

