"""halil ibrahim mut
Performing actions on the cube according
to the matrix operations learned from
Computer Graphics
-------------------------------------
Computer Graphics deslerinden öğrenilen
matris işlemlerine göre küpte eylemler
gerçekleştirmek
"""

#required functions and stuffs are on settings.py file
from settings import *

pygame.init()

#define the points of cube that its centers on origin
cube=[-1,1,
      1,1,
      1,-1,
      -1,-1]
cube=size(cube,40)      #rescaling for bigger cube
cube=translate(cube,100,RESOLUTION[1]//2 -40)#RESOLUTION[1]//2)#translate points to center of window

cube3d=[-1,-1,-1,
        1,-1,-1,
        1,1,-1,
        -1,1,-1,
        -1,-1,1,
        1,-1,1,
        1,1,1,
        -1,1,1]
cube3d=size(cube3d,40)#rescaling for bigger 3d cube
cube3d=trans3d(cube3d,240,RESOLUTION[1]//2 -40,150)#translate points to center of window

def run():
    global cube
    global cube3d
    global clock
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print("space")
                    #cube=rotate(cube,10)

        ekran.fill(WHITE)
        draw_cube(cube,[RED,GREEN,BLUE,BLACK])#delete 2nd argument if you want one color
        cube=rotate(cube,theta_z=1)

        draw3d(cube3d, [RED, GREEN, BLUE, BLACK])
        cube3d = rotate3d(cube3d, theta_x=1, theta_y=1, theta_z=1)
        pygame.display.flip()
        clock.tick(FPS)
run()
pygame.quit()
exit()
