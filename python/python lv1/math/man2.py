import os
import pygame

os.environ["SOL_VIDEO_CENTERED"] = '1'

width,height =1920,1080
win = (width,height)
screen = pygame.display.set_mode(win)
xaxis = width/1.80 + 150
yaxis = height/2
scale = 450
iterations = 10

def main():
    for iy in range(int(height/2+1)):
        for ix in range(width):
            z = 0 + 0j
            c = complex(float(ix-xaxis)/scale,float(iy-yaxis)/scale)
            x = ]
