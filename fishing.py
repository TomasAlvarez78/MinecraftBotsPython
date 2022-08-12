import pyautogui as pt
# import pydirectinput as pdi
from time import sleep

sleep(3)

while(True):
    position = pt.locateOnScreen("images\imagefishing.png",confidence =.7)

    sleep(0.1)

    if position is not None:
        pt.rightClick()
        sleep(1)
        pt.rightClick()
    