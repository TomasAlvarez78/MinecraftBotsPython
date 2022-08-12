from time import sleep
from miner import Miner

sleep(3)
miner = Miner()
position = miner.positionImage("images\clicktoplay.png", 0.7)
while(True):
    miner.leftClick()