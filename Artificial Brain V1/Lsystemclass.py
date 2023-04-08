import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import turtle
# L-system (Lindenmayer system)
class LSystem:
    def __init__(self, axiom, rules, angle, depth=5):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.depth = depth

    def apply_rules(self, axiom):
        new_axiom = ""
        for char in axiom:
            if char in self.rules:
                new_axiom += self.rules[char]
            else:
                new_axiom += char
        return new_axiom

    def generate(self, length=5):
        current_axiom = self.axiom

        for _ in range(self.depth):
            current_axiom = self.apply_rules(current_axiom)

        window = turtle.Screen()
        t = turtle.Turtle()
        t.speed(0)

        t.penup()
        t.goto(-200, 200)
        t.pendown()

        stack = []
        for char in current_axiom:
            if char == "F":
                t.forward(length)
            elif char == "+":
                t.left(self.angle)
            elif char == "-":
                t.right(self.angle)
            elif char == "[":
                stack.append((t.position(), t.heading()))
            elif char == "]":
                position, heading = stack.pop()
                t.penup()
                t.goto(position)
                t.setheading(heading)
                t.pendown()

        window.mainloop()
