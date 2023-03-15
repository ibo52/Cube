import pygame.image

import pygame
from OpenGL.GL import *

class Texture(object):
    def __init__(self,fileName=None,properties={}):
        self.surface=None

        #texture reference to gpu
        self.textureRef=glGenTextures(1)

        self.properties={
            "magFilter":GL_LINEAR,
            "minFilter": GL_LINEAR_MIPMAP_LINEAR,
            "wrap"     :GL_REPEAT
        }

        self.setProperties(properties)

        if fileName is not None:
            self.loadImage(fileName)
            self.uploadData()

    def loadImage(self,fileName):
        try:
            self.surface=pygame.image.load(fileName)
        except Exception as e:
            print("Error while loading image:",fileName,e)
            exit(e)

    def setProperties(self,properties):
        for name,data in properties.items():
            if name in self.properties.keys():
                self.properties[name]=data
            else:
                raise Exception("No property named:",name)

    #upload image data to gpu
    def uploadData(self):
        width=self.surface.get_width()
        height = self.surface.get_height()

        #convert image to string buffer
        imgData=pygame.image.tostring(self.surface, "RGBA",1)

        #bind reference to gpu
        glBindTexture(GL_TEXTURE_2D,self.textureRef)

        #send data through reference pointer
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                     width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, imgData )

        #mipmap
        glGenerateMipmap(GL_TEXTURE_2D)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                        self.properties["magFilter"])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                        self.properties["minFilter"])

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,
                        self.properties["wrap"])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                        self.properties["wrap"])