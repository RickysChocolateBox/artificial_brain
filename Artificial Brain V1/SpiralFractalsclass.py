import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import turtle

# Spiral Fractals
class SpiralFractals:
    def __init__(self, depth=5):
        self.depth = depth

    def generate(self):
        window = turtle.Screen()
        t = turtle.Turtle()
        t.speed(0)

        def spiral(t, length, angle, factor):
            if length > 1:
                t.forward(length)
                t.right(angle)
                spiral(t, length * factor, angle, factor)

        t.penup()
        t.goto(-200, 200)
        t.pendown()

        spiral(t, 200, 120, 0.9)

        window.mainloop()

