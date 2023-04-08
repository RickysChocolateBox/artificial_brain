import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import turtle
# Mandelbrot Set
class MandelbrotSet:
    def __init__(self, width=800, height=800, max_iter=1000):
        self.width = width
        self.height = height
        self.max_iter = max_iter

    def mandelbrot(self, x, y):
        c = complex(x, y)
        z = 0.0j
        for i in range(self.max_iter):
            z = z*z + c
            if (z.real*z.real + z.imag*z.imag) >= 4:
                return i
        return self.max_iter

    def generate(self):
        img = Image.new('RGB', (self.width, self.height), 'white')
        pixels = img.load()

        for x in range(self.width):
            for y in range(self.height):
                zx, zy = x * (3.5 / self.width) - 2.5, y * (2.0 / self.height) - 1.0
                c = self.mandelbrot(zx, zy)
                r, g, b = c % 8 * 32, c % 16 * 16, c % 32 * 8
                pixels[x, y] = (r, g, b)

        img.show()
