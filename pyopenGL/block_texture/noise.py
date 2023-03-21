from numpy import sin,pi,arange as range
from matplotlib import pyplot as p
import random
def sinNoise(amp=16,f=None, offset=None,sampleSize=None,plotRange=None):
    l = []

    f = (2 * pi / amp) if f==None else f

    offset = (amp/4) if offset==None else offset

    plotRange=amp if plotRange==None else plotRange
    sampleSize=1 if sampleSize==None else plotRange/sampleSize
    amp=amp/2
    for a in range(0,plotRange,sampleSize):
        l.append((sin((a - offset) * f) * amp)+amp)
    return l

if __name__=="__main__":

    s=sinNoise( 16 )
    p.plot(s)
    #p.plot(sinNoise(amp,f,k))
    p.show()
