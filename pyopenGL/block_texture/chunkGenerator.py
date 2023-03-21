import random

import numpy as np

from block_texture.chunk2 import ChunkGeometry
from core.texture import Texture
from materials.textureMaterial import TextureMaterial
from core.mesh import Mesh

from block_texture.noise import sinNoise
class WorldGenerator:
    def __init__(self,sceneObj=None):
        self.sceneRef=sceneObj

        self.chunk_positions=[]

    def generate(self,pos=[0,0,0],CHUNK_SIZE=4):

        dirt_texture=Texture("./block_texture/dirt3.jpg")
        dirtTextMat=TextureMaterial(dirt_texture)

        DEFAULT_CHUNK_GENERATE_SIZE=CHUNK_SIZE

        offset=4
        for ground_x in range(pos[0],DEFAULT_CHUNK_GENERATE_SIZE+pos[0]):
                for ground_z in range(pos[2], DEFAULT_CHUNK_GENERATE_SIZE+pos[2]):
                    r=random.randint(8,32)#random wave amplitude(height)
                    offset+=random.randint(4,16)#16/8#random wave offset(width)
                    dirtChunk = ChunkGeometry(position=[(ground_x*16),0,(ground_z*16)],
                                              imgParse=3,
                                              generateList=sinNoise(amp=r,sampleSize=16,offset=offset) )

                    m1=Mesh(dirtChunk,dirtTextMat)
                    self.sceneRef.add(m1)
