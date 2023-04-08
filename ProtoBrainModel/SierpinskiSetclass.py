import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import turtle
# Sierpinski Set
class SierpinskiSet:
    def __init__(self, depth=5):
        self.depth = depth

    def draw_sierpinski(self, t, length, depth):
        if depth == 0:
            for _ in range(3):
                t.forward(length)
                t.left(120)
        else:
            self.draw_sierpinski(t, length / 2, depth - 1)
            t.forward(length / 2)
            self.draw_sierpinski(t, length / 2, depth - 1)
            t.backward(length / 2)
            t.left(60)
            t.forward(length / 2)
            t.right(60)
            self.draw_sierpinski(t, length / 2,
depth - 1)
            t.left(60)
            t.backward(length / 2)
            t.right(60)

    def generate(self):
        window = turtle.Screen()
        t = turtle.Turtle()
        t.speed(0)

        t.penup()
        t.goto(-200, 200)
        t.pendown()

        self.draw_sierpinski(t, 400, self.depth)

        window.mainloop()