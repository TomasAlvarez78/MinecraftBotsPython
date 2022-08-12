from time import sleep
from miner import Miner

sleep(3)
miner = Miner()
while(True):
    position = miner.positionImage("images\imagefishing.png", 0.7)

    sleep(0.1)

    if position is not None:
        miner.rightClick()
        sleep(1)
        miner.rightClick()
    