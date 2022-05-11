import pygame
pygame.init()
from pygame.locals import *
from pygame import mixer

import sys
import random
import math
import time
import csv

path = "/home/abhay/Desktop/Python/Games/Pong/"

# Create the screen
screen_width = 1600
screen_height = 800
# screen_height = int(screen_width/1.5 * 0.45)

screenSize = (screen_width, screen_height)
screen = pygame.display.set_mode(screenSize)

# Background Image
# background = pygame.image.load('Images/background2.png')

# Background Music
mixer.music.load(path + 'Sound/digital.wav')
mixer.music.play(-1)

# Load Images
icon = pygame.image.load(path + 'Images/icon.png')
pixel_img = pygame.image.load(path + 'pixel.png').convert()
p5_img = pygame.image.load(path + '5p.png').convert()
green_img = pygame.image.load(path + 'Images/green3px.png').convert()

# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (250,150,0)

# Title and Icon
pygame.display.set_caption("Science A4 Simulation")
pygame.display.set_icon(icon)

X = 0
Y = 0

x = X
y = Y

a = 1.4
b = 0.3

c = 0
stop = False

def sign(x):
    if(x == 0):
        return 1

    return x/abs(x)

def draw():
    global x, y
    scale = 500

    # Draw Pixel
    
    ball_location = ((screen_width/2 + scale*x - sign(x)*3, screen_height/2 - scale*y - sign(y)*3))
    screen.blit(green_img, ball_location)

def ball():
    global x, y, X, Y

    x = Y + 1 - a*X*X
    y = b*X

    # x += 0.1
    # y += 0.1

    X = x
    Y = y

draw()
pygame.display.update()
time.sleep(1)
sleep = 1.01
s = 0.1

# Game Loop
while True:
    c += 1

    # Refill with black, otherwise the images paint the screen
    # screen.fill(black)

    # Events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                pygame.quit()
                sys.exit() 

    if(not stop):
        print(c)

    if(not stop):
        ball()
        draw()
    # time.sleep(sleep)
    sleep -= s
    s *= 0.9
    
    # Update
    pygame.display.update()

    if(c == 10000):
        stop = True