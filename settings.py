"""
Halil Ibrahim Mut
settings for CG matrix operations
"""
import pygame
from math import cos, sin, radians,sqrt

FPS = 60

# ---- window settings ----
RESOLUTION = (400, 300)  # window size
WINDOW_NAME = "CG 2D/3D point MATRIX implementation | Halil ibrahim Mut"

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
def draw3d(array,color_array=[BLACK]):
    color_len=len(color_array)

    arr_size=len(array)
    for idx in range(0,arr_size,3):
        ax, ay = array[idx] + (array[idx+2] * 0.3) , array[idx+1] + (array[idx+2] * 0.3)
        bx, by = array[(idx+3)%arr_size] + (array[(idx+5)%arr_size] * 0.3) , array[(idx+4)%arr_size] + (array[(idx+5)%arr_size] * 0.3)
        pygame.draw.line(ekran, color_array[(idx//2)%color_len], (ax, ay),
                         (bx,by), 5)

def draw_cube(array,color_array=[BLACK]):
    color_len=len(color_array)

    arr_size=len(array)
    for idx in range(0,arr_size,2):
        pygame.draw.line(ekran, color_array[(idx//2)%color_len], (array[idx], array[idx+1]),
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
def rotate(array, theta_x=0,theta_y=0,theta_z=0):
    """rotate x-y planes on array according to theta"""
    theta_x = radians(theta_x)
    theta_y = radians(theta_y)
    theta_z = radians(theta_z)
    
    #turn around z axis
    rot_matrix_z = [cos(theta_z), -sin(theta_z),
                  sin(theta_z), cos(theta_z)]

    # IMPORTANT:firstly translate to origin
    # to rotate around their OWN center

    #thinked as object is always cube
    cube_len=sqrt( (array[0]-array[2])**2 + (array[1]-array[3])**2 )/2
    posx,posy=array[0],array[1]
    array = translate(array, -posx, -posy)

    #array = translate(array, -100, -100)

    idx = 0
    rotated = []
    while (idx + 1 < len(array)):
        x = rot_matrix_z[0] * array[idx] + rot_matrix_z[1] * array[idx + 1]
        y = rot_matrix_z[2] * array[idx] + rot_matrix_z[3] * array[idx + 1]
        rotated += x, y
        idx += 2
    # re-translate to original positions
    #rotated = translate(rotated, 100, 100)
    rotated = translate(rotated, posx, posy)
    return rotated


#-------------------------------
#------3d transformations -------
#-------------------------------
def trans3d(array,x=0,y=0,z=0):
    l = array.copy()
    idx = 0
    while (idx + 1 < len(array)):
        l[idx] = x + array[idx]
        l[idx + 1] = y + array[idx + 1]
        l[idx+2]=z+array[idx + 2]
        idx += 3

    return l
def rotate3d(array, theta_x=0,theta_y=0,theta_z=0):
    theta_x = radians(theta_x)
    theta_y = radians(theta_y)
    theta_z = radians(theta_z)

    rot_matrix_z = [cos(theta_z), -sin(theta_z),0,
                  sin(theta_z), cos(theta_z),0,
                    0,0,1]
    
    rot_matrix_y = [cos(theta_y),0, sin(theta_y),
                    0,1,0,
                  -sin(theta_y),0, cos(theta_y)]
    
    rot_matrix_x = [1,0, 0,
                    0,cos(theta_x),-sin(theta_x),
                  0,sin(theta_x), cos(theta_x)]

    # IMPORTANT:firstly translate to origin
    # to rotate around their OWN center
    posx, posy, posz = array[0], array[1], array[2]  # original poision of points
    array = trans3d(array,-posx,-posy,-posz)

    # rotate around x
    idx = 0;rotated = []
    while (idx + 1 < len(array)):
        x = rot_matrix_x[0] * array[idx] + rot_matrix_x[1] * array[idx + 1] + rot_matrix_x[2] * array[idx + 2]
        y = rot_matrix_x[3] * array[idx] + rot_matrix_x[4] * array[idx + 1] + rot_matrix_x[5] * array[idx + 2]
        z = rot_matrix_x[6] * array[idx] + rot_matrix_x[7] * array[idx + 1] + rot_matrix_x[8] * array[idx + 2]
        rotated += x, y,z
        idx += 3

    # rotate around y
    array=rotated;rotated=[];idx=0
    while (idx + 1 < len(array)):
        x = rot_matrix_y[0] * array[idx] + rot_matrix_y[1] * array[idx + 1] + rot_matrix_y[2] * array[idx + 2]
        y = rot_matrix_y[3] * array[idx] + rot_matrix_y[4] * array[idx + 1] + rot_matrix_y[5] * array[idx + 2]
        z = rot_matrix_y[6] * array[idx] + rot_matrix_y[7] * array[idx + 1] + rot_matrix_y[8] * array[idx + 2]
        rotated += x, y,z
        idx += 3

    # rotate around z
    array = rotated;rotated = [];idx = 0
    while (idx + 1 < len(array)):
        x = rot_matrix_z[0] * array[idx] + rot_matrix_z[1] * array[idx + 1] + rot_matrix_z[2] * array[idx + 2]
        y = rot_matrix_z[3] * array[idx] + rot_matrix_z[4] * array[idx + 1] + rot_matrix_z[5] * array[idx + 2]
        z = rot_matrix_z[6] * array[idx] + rot_matrix_z[7] * array[idx + 1] + rot_matrix_z[8] * array[idx + 2]
        rotated += x, y,z
        idx += 3

    #re-move back from origin to original position
    rotated= trans3d(array, posx,posy,posz)
    return rotated
