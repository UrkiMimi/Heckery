### Basic preperation stuff
import json
from Noodled import *
import math
import random as rand
from copy import deepcopy


'''
exFile = open("ExpertStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()
'''

### Noodle fuckery
# Add arrays
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}

### do note scripts here
## init

# region environment stuff
boomyTimes = [4,8,12,16,20,24,28,30,32]
halfBoomTimes = [7.5,15.5]
ugliTimes = [43.5,59.5]

# reduce code
for i in range(50-36):
    ugliTimes.append(36+i)

for i in range(64-52):
    ugliTimes.append(52+i)

for i in range(72-68):
    ugliTimes.append(68+i)

# im about to puke
for i in boomyTimes:
    # Set conts
    enRand = [[round(rand.uniform(-5,5),3),round(rand.uniform(-5,5),3),7.75],[round(rand.uniform(0,0.1),3),round(rand.uniform(0,0.1),3),round(rand.uniform(0,0.1),3)]]
    rRand = [[round(rand.uniform(-8,8),3),round(rand.uniform(-8,8),3),7],[round(rand.uniform(0,3),3),round(rand.uniform(0,3),3),round(rand.uniform(0,3),3)]]
    lRand = [[round(rand.uniform(-8,8),3),round(rand.uniform(-8,8),3),7],[round(rand.uniform(0,3),3),round(rand.uniform(0,3),3),round(rand.uniform(0,3),3)]]
    
    # energy panel anim
    posTween(i,'energyPanel',0.2,'easeOutQuad',[0,-0.64,7.75,0],[enRand[0][0],enRand[0][1],enRand[0][2],1])
    posTween(i+0.2,'energyPanel',1.8,'easeInSine',[enRand[0][0],enRand[0][1],enRand[0][2],0],[0,-0.64,7.75,1])
    scaleTween(i,'energyPanel',0.2,'easeOutQuad',[0.02,0.02,0.02,0],[enRand[1][0],enRand[1][1],enRand[1][2],1])
    scaleTween(i+0.2,'energyPanel',1.8,'easeInSine',[enRand[1][0],enRand[1][1],enRand[1][2],0],[0.02,0.02,0.02,1])

    # left panel anim
    posTween(i,'leftpanel',0.2,'easeOutQuad',[-3.2,0.4,7,0],[lRand[0][0],lRand[0][1],lRand[0][2],1])
    posTween(i+0.2,'leftpanel',1.8,'easeInSine',[lRand[0][0],lRand[0][1],lRand[0][2],0],[-3.2,0.4,7,1])
    scaleTween(i,'leftpanel',0.2,'easeOutQuad',[1,1,1,0],[lRand[1][0],lRand[1][1],lRand[1][2],1])
    scaleTween(i+0.2,'leftpanel',1.8,'easeInSine',[lRand[1][0],lRand[1][1],lRand[1][2],0],[1,1,1,1])

    # right panel anim
    posTween(i,'rightpanel',0.2,'easeOutQuad',[3.2,0.4,7,0],[rRand[0][0],rRand[0][1],rRand[0][2],1])
    posTween(i+0.2,'rightpanel',1.8,'easeInSine',[rRand[0][0],rRand[0][1],rRand[0][2],0],[3.2,0.4,7,1])
    scaleTween(i,'rightpanel',0.2,'easeOutQuad',[1,1,1,0],[rRand[1][0],rRand[1][1],rRand[1][2],1])
    scaleTween(i+0.2,'rightpanel',1.8,'easeInSine',[rRand[1][0],rRand[1][1],rRand[1][2],0],[1,1,1,1])

    customRingRotation(i,95,step=20,speed=10,direction=rand.randint(0,1))

# for gabber that happens on half times
for i in halfBoomTimes:
    rotate(i,'leftpanel', 1.5, 'easeOutBack', [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-90,90),0], [0,0,0,1])
    rotate(i,'leftpanel', 1.5, 'easeOutBack', [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-90,90),0], [0,0,0,1])
    customRingRotation(i,95,step=rand.randint(1,45),speed=10, direction=rand.randint(0,1))

# manual ring steps
customRingStep(0.01,step=0.5,speed=10000)
customRingStep(36,step=4,speed=10000)
customRingStep(52,step=-1.5,speed=10000)
customRingStep(64,step=15,speed=20)

# gabber part 2
for i in ugliTimes:
    customRingRotation(i,95,step=rand.randint(1,45),speed=50, direction=rand.randint(0,1))
    rotate(i,'leftpanel',1,'easeOutQuad',[25,180*((i%2)-0.5),0,0],[0,0,0,1])
    rotate(i,'rightpanel',1,'easeOutQuad',[25,180*((i%2)-0.5),0,0],[0,0,0,1])
    

# region notemods
#ye
assignNotesToTrack(35,90,'fakeNotes',False)
randomPosNJS(36,50)
moveIt(52,64,'easeInOutExpo',noteOffset=1,division=6)
randomPosNJS(68,72)

spawnFakeNotesWithTrackAt(35,90,False,0)
assignNotesToTrack(35,90,'realNotes',False)




### Save json to Ex+ file
diPlusFile = open('ExpertPlusStandard.dat', 'w')
diPlusFile.write(json.dumps(exData,indent=2))
diPlusFile.close()