# Python program to convert
# numpy array to image
  
# import required libraries
import numpy as np
from PIL import Image as im
from random import randint
from matplotlib import pyplot as plt
# define a main function

class TextureGenerator:
    def __init__(self,SIZE=256):
        #----image buffer properties------
        self.SIZE=SIZE
        self.pixel_size=3*(256**2)
        self.shape=(self.SIZE,self.SIZE,3)
        #----image buffer properties------

        self.texture_dictionary={"dirt":[ (128,176), (64,128), (0,64) ],
                                 "stone":(32,224)}

        self.colorMap=[]
        self.generateColorMap(color_range=self.texture_dictionary["stone"],grayscale=True)
        

    def generate(self):
        imageBuff = np.zeros(self.shape, dtype=np.uint8)

        mapLen=len(self.colorMap)

        skip_size=256//8#draw N pixels with same color
        for y in range(0, self.SIZE, skip_size):
            for x in range(0, self.SIZE, skip_size):
                imageBuff[y:y+skip_size, x:x+skip_size ] = self.colorMap[ randint(0,mapLen-1) ]


        plt.imshow(imageBuff)
        plt.show()
        data = im.fromarray(imageBuff)
        
        data.save('generated_np_image.png')

        
    def generateColorMap(self,color_range=[ (128,176), (64,128), (0,64) ],grayscale=False):

        Map=[]
        for i in range(16):
            if grayscale:
                r=randint( color_range[0], color_range[1] )
                g=r
                b=r
            else:
                r=randint( color_range[0][0], color_range[0][1] )
                g=randint( color_range[1][0], color_range[1][1] )
                b=randint( color_range[2][0], color_range[2][1] )
            
            Map+=[[r,g,b]]
            
        self.colorMap=Map

  
# driver code
if __name__ == "__main__":
    
  # function call
  c=TextureGenerator()
  c.generate()
  print("DONE")
