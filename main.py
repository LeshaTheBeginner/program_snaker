
import pygame
import random

class Screen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.size = (self.width/16,self.height/12)


class Grid:
    def __init__(self, size):
        self.size = size

class Snake:
    def __init__(self):
        self.size = 3
        self.xy = [(0,0),(1,0)(2,0)(3,0)]
        self.current = [3,0]
        self.direction = 0 # 0 left 1 up 2 right 3 bottom
        self.speed = 0.5
    
    def movement(self):
        # 0,0 1,0 2,0 3,0 -> 1,0 2,0 3,0 3,1 ->  2,0 3,0 3,1 3,2
        if self.direction == 0:
            self.current[0] -= 1
        elif self.direction == 1:
            self.current[1] += 1
        elif self.direction == 2:
            self.current[0] += 1
        elif self.direction == 3:
            self.current[1] -= 1
        
        self.xy.append(self.current)
        self.xy.pop(0)
    
    def eat(self):
        self.xy.insert(0,"i was here")

        

class Apple:
    def __init__(self):
        self.xy = (1,2)
        self.eaten=False

    def respawn(self):
        self.xy = (random.randint(0,2),random.randint(0,2)) #numbers are placeholder, change them when grid is implemented
        print("Apple: Respawned")        