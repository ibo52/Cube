"""
Halil Ibrahim Mut
settings for CG matrix operations.
"""
import pygame
from math import cos, sin, radians

FPS = 60

# ---- window settings ----
RESOLUTION = (300, 300)  # window size
WINDOW_NAME = "hz ibo; CG 2d MATRIX deneme"

clock = pygame.time.Clock()
ekran = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(WINDOW_NAME)
# --------------------------

# ---- colours ----
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
# -----------------

def draw_cube(array,color_array=[BLACK]):
    color_len=len(color_array)

    arr_size=len(array)
    for idx in range(0,arr_size,2):
        pygame.draw.line(ekran, color_array[idx%color_len], (array[idx], array[idx+1]),
                         (array[(idx+2)%arr_size], array[(idx+3)%arr_size]), 5)

    """ OLD : deprecated
    pygame.draw.line(ekran, BLACK, (array[0], array[1]), (array[2], array[3]), 5)
    pygame.draw.line(ekran, BLACK, (array[2], array[3]), (array[4], array[5]), 5)
    pygame.draw.line(ekran, BLACK, (array[4], array[5]), (array[6], array[7]), 5)
    pygame.draw.line(ekran, BLACK, (array[6], array[7]), (array[0], array[1]), 5)
    """

# resize the points on an array
def size(array, coefficient):
    l = array.copy()
    for idx in range(len(array)):
        l[idx] *= coefficient

    return l


# move/displace the points on an array

def translate2(array, x=0, y=0):
    """ old and wrong function.Deprecated """
    l = array.copy()
    for idx in range(len(array)):
        l[idx] += x
        # l[idx+1]=+

    return l


def translate(array, x=0, y=0):
    """-_-"""
    l = array.copy()
    idx = 0
    while (idx + 1 < len(array)):
        l[idx] = x + array[idx]
        l[idx + 1] = y + array[idx + 1]
        idx += 2

    return l


# --------------------------

# rotate the points on an array on their own center
def rotate(array, theta):
    """rotate x-y planes on array according to theta"""
    theta = radians(theta)
    rot_matrix = [cos(theta), -sin(theta),
                  sin(theta), cos(theta)]

    # IMPORTANT:firstly translate to origin
    # to rotate around their OWN center
    array = translate(array, -150, -150)

    idx = 0
    rotated = []
    while (idx + 1 < len(array)):
        x = rot_matrix[0] * array[idx] + rot_matrix[1] * array[idx + 1]
        y = rot_matrix[2] * array[idx] + rot_matrix[3] * array[idx + 1]
        rotated += x, y
        idx += 2
    # translate to original positions
    rotated = translate(rotated, 150, 150)
    return rotated
