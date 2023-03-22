import random

import numpy as np

from block_texture.chunk2 import ChunkGeometry
from core.texture import Texture
from materials.textureMaterial import TextureMaterial
from core.mesh import Mesh

from block_texture.perlin import *
class WorldGenerator:
    def __init__(self,sceneObj=None):
        self.sceneRef=sceneObj

        self.chunk_positions=[]

    def generate(self,pos=[0,0,0],CHUNK_SIZE=4):

        dirt_texture=Texture("./block_texture/dirt3.jpg")
        dirtTextMat=TextureMaterial(dirt_texture)

        DEFAULT_CHUNK_GENERATE_SIZE=CHUNK_SIZE

        for ground_x in range(pos[0],DEFAULT_CHUNK_GENERATE_SIZE+pos[0]):
                for ground_z in range(pos[2], DEFAULT_CHUNK_GENERATE_SIZE+pos[2]):

                    lin_array = np.linspace(0, 15,96, endpoint=False)
                    # create grid using linear 1d arrays
                    x, y = np.meshgrid(lin_array, lin_array)
                    map=perlin(x,y,seed=DEFAULT_CHUNK_GENERATE_SIZE*ground_x+ground_z)

                    map=map.flatten()
                    map+=abs(min(map))
                    map*=16.0/max(map)


                    dirtChunk = ChunkGeometry(position=[(ground_x*16),0,(ground_z*16)],
                                              imgParse=3,
                                              generateList=map )

                    m1=Mesh(dirtChunk,dirtTextMat)
                    self.sceneRef.add(m1)
