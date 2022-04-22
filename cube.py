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

cube=translate(cube,150,150)#translate points to center of window
###
def run():
    global cube
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
        draw_cube(cube)
        cube=rotate(cube,1)
        pygame.display.flip()
        clock.tick(60)
run()
pygame.quit()
exit()