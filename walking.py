import pyautogui as pt
# import pydirectinput as pdi
from time import sleep

sleep(3)

def pressKey(key,duration):
    pt.keyDown(key)
    print(f"{key} Npressed")
    sleep(1)
    pt.keyUp(key)

while(True):
    if( pt.locateOnScreen("images/craftingtable.png",confidence =.7)):
        print("Breaking loop")
        break
    pressKey('d',1)
    pressKey('a',1)