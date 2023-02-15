import pygame

class Input(object):
    def __init__(self):
        #has the user quit from program
        self.quit=False

        #list to store key events
        #down:up discrete events, last for one iter
        #pressed: continuous events
        self.keyDownList=[]
        self.keyPressedList=[]
        self.keyUpList=[]
        self.wheel=0

    def update(self):

        self.keyDownList = []
        self.keyUpList = []

        #check for user inputs
        for event in pygame.event.get():
            #quit if window close event occuered
            if event.type==pygame.QUIT:
                self.quit=True

            if event.type==pygame.KEYDOWN:
                keyName=pygame.key.name(event.key)
                self.keyDownList.append( keyName )
                self.keyPressedList.append( keyName )

            if event.type==pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyUpList.append(keyName)
                self.keyPressedList.remove(keyName)

            #mouse wheel to scale
            if event.type==pygame.MOUSEWHEEL:
                self.wheel=event.y
            else:
                self.wheel=0

    def isKeyDown(self, keyName):
        return keyName in self.keyDownList

    def isKeyUp(self, keyName):
        return keyName in self.keyUpList

    def isKeyPressed(self, keyName):
        return keyName in self.keyPressedList

    def isMouseWheelPressed(self):
        return self.wheel

