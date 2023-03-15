import random

import numpy as np

from block_texture.chunk import ChunkGeometry
from core.texture import Texture
from materials.textureMaterial import TextureMaterial
from core.mesh import Mesh

class WorldGenerator:
    def __init__(self,sceneObj=None):
        self.sceneRef=sceneObj

    def generate(self,pos=[0,0,0],CHUNK_SIZE=1):

        dirt_texture=Texture("./block_texture/dirt3.jpg")
        dirtTextMat=TextureMaterial(dirt_texture)

        DEFAULT_CHUNK_GENERATE_SIZE=4

        for ground_x in range(pos[0],DEFAULT_CHUNK_GENERATE_SIZE+pos[0]):
                for ground_z in range(pos[2], DEFAULT_CHUNK_GENERATE_SIZE+pos[2]):
                    r=random.randint(0,4)
                    dirtChunk = ChunkGeometry(position=[(ground_x*16),r,(ground_z*16)],imgParse=3)

                    m1=Mesh(dirtChunk,dirtTextMat)
                    self.sceneRef.add(m1)