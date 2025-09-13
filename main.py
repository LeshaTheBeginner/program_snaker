import pygame

class Snake:
    def __init__(self):
        self.size = 3
        self.xy = [(0,0),(1,0)(2,0)(3,0)]
        self.direction = 0 # 0 left 1 up 2 right 3 bottom
        self.speed = 0.5

class Apple:
    def __init__(self):
        self.xy = (1,2)
        self.eaten=False
        