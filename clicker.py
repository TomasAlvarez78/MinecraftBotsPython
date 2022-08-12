import pyautogui as pt
from time import sleep

sleep(3)

position = pt.locateOnScreen("images\clicktoplay.png",confidence =.7)
while(True):
    pt.leftClick()