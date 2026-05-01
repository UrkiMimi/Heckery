### Basic preperation stuff
import json
from Noodled import *
from heckGeometry import *
import math
import random as rand
from copy import deepcopy


'''
exFile = open("ExpertStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()
'''

plinkoFile = open("plinkopretty.json","r")
plinkSim = json.loads(plinkoFile.read())
plinkoFile.close()


### Noodle fuckery
# Add arrays
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []

### do note scripts here
## vars for easy editing and shit
distance = 5
height = 1.5
scale = 2

# materials
addMaterial('Standard',[1,1,1,1],True,'white')

# add pillars
ball = []

for i in plinkSim['obj']:
    if i['name'].startswith('object'):
        addPrimitiveModelTrack('Cube','white',[i['pos'][0]['x']*scale,(i['pos'][0]['y']*scale)+height,distance],[0,0,0],[0.0,0.0,0.0],'pillars')
    else:
        ball = i['pos']

# animate pillars when luke says horse plinko
scaleTween(7.484,'pillars',1.157,'easeOutQuad',[0,0,0,0],[scale/10,scale/10,scale/10,1])

# animations for ball
posDef = []
rotDef = []

for i in range(len(ball)):
    posDef.append(
        [
            ball[i]['x']*scale,
            (ball[i]['y']*scale)+height,
            distance,round(i/len(ball),4)
         ])
    rotDef.append([0,0,ball[i]['dir'],round(i/len(ball),4)])

addPrimitiveModelTrack('Cube','white',[posDef[0][0],posDef[0][1],distance],[0,0,rotDef[0][2]],[0,0,0],'ball')

scaleTween(11,'ball',0.45,'easeOutQuint',[0,0,0,0],[scale/10,scale/10,scale/10,1])

posPointDef(11.45,'ball',4.8,posDef,'easeLinear')
localRotatePointDef(11.45,'ball',4.8,rotDef,'easeLinear')


### Save json to Ex+ file
diPlusFile = open('ExpertPlusStandard.dat', 'w')
diPlusFile.write(json.dumps(exData,indent=2))
diPlusFile.close()