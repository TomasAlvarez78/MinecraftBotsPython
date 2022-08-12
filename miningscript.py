import pyautogui as pt
import pydirectinput as pdi
from time import sleep

class Miner:

    def moveToImage(self, image, clicks, off_x = 0 , off_y = 0):
        ## Returns the position of the image ex. ( 1300 , 700 )
        position = pt.locateOnScreen(image,confidence =.7)

        ## If positions doesn't exist, meaning that the image itself was not found
        if position is None:
            print(f'{image} not found')
            return 0
        else:
            ## If the image was found then
            ## it moves the mouse to that position
            ## And clicks it x amount of times
            pdi.moveTo(position[0],position[1])
            pdi.moveRel(off_x,off_y)
            pdi.click(clicks=clicks)
    
    def locateStop(self):
        position = pt.locateCenterOnScreen("images\craftingtable.png",confidence =.5)

        if position is None:
            return False
        else:
            print("Stopping programm")
            return True


    def locateLava(self):
        ## Returns boolean if lava was found using image
        position = pt.locateCenterOnScreen("images\lavaclose.png",confidence =.7)

        if position is None:
            return False
        else:
            return True

    def locateGravel(self):
        ## Returns boolean if lava was found using image
        position = pt.locateCenterOnScreen("images\gravel.png",confidence =.7)

        if position is None:
            return False
        else:
            return True

    def actionKey(self, key, duration = 1):
        ## Helper function, presses key during certain amount of time
        pdi.keyDown(key)
        sleep(duration)
        pdi.keyUp(key)

    def changeDirectionCamera(self, x, y):
        pdi.moveRel(x,y)

    def startAttack(self, duration):
        pdi.mouseDown()
        sleep(duration)
    
    def stopAttack(self):
        pdi.mouseUp()

def main():
    miner = Miner()

    ## Presses the resume game button
    miner.moveToImage("images\playgame2.png", 1)
    miner.actionKey('x',0.75)
    miner.changeDirectionCamera(400,400)


sleep(3)
# # main()
miner = Miner()
# miner.moveToImage("images\playgame2.png",2)
# miner.actionKey("w",1)
# miner.startAttack(1)
# miner.stopAttack()
# sleep(1)

# for i in range(0,10):
#     pdi.moveRel(100,100)
#     pdi.moveRel(-100,-100)
#     pdi.moveRel(-100,100)
#     pdi.moveRel( 100,-100)
# # pdi.moveTo(100,100) 

altura = 300
contador = 0
resolution = pt.size()

pdi.moveTo(resolution[0]/2,resolution[1]/2)

while(True):
    miner.startAttack(0.3)
    miner.stopAttack()
    if contador == 2:
        pdi.moveRel(0,-400)
        contador = 0
        miner.actionKey("w",0.09)
    else:
        pdi.moveRel(0,205)
        contador += 1

    if miner.locateStop():
        break
    
    # if miner.locateGravel() :
    #     miner.actionKey("3",0.2)
    # else:
    #     miner.actionKey("2",0.2)
