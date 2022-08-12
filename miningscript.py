from time import sleep
from miner import Miner

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
resolution = miner.getResolution()

miner.moveToCenter(resolution)

while(True):
    miner.startAttack(0.3)
    miner.stopAttack()
    if contador == 2:
        miner.changeDirectionCamera(0,-400)
        contador = 0
        miner.actionKey("w",0.09)
    else:
        miner.changeDirectionCamera(0,205)
        contador += 1

    if miner.locateStop():
        break
    
    # if miner.locateGravel() :
    #     miner.actionKey("3",0.2)
    # else:
    #     miner.actionKey("2",0.2)
