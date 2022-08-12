import pyautogui as pt
import pydirectinput as pdi
from time import sleep

class Miner:
    def moveToImageClick(self, image, clicks, off_x = 0 , off_y = 0):
        ## Returns the position of the image ex. ( 1300 , 700 )
        position = pt.locateOnScreen(image,confidence =.7)

        ## Image was not found
        if position is None:
            print(f'{image} not found')
            return 0
        else:
            ## Image was found => move to it and click x times
            pdi.moveTo(position[0],position[1])
            pdi.moveRel(off_x,off_y)
            pdi.click(clicks=clicks)

    def positionImage(self, image, confidence):
        ## Returns the position of the image ex. ( 1300 , 700 )
        position = pt.locateOnScreen(image,confidence = confidence)

        ## Image was found => return position
        if position is not None:
            print(f'{image} found')
            return position
        else:
            print(f'{image} not found')
            return None
                
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

    def getResolution(self):
        return pt.size()

    def moveToCenter(self,resolution):
        pdi.moveTo(resolution[0]/2,resolution[1]/2)

    def rightClick(self):
        pt.rightClick()
    
    def leftClick(self):
        pt.leftClick()

