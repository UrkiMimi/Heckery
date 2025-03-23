### Basic preperation stuff
import json
from heckNoodle import *
from heckChroma import *
from heckVivify import *
import math
import random as rand
from copy import deepcopy


'''
exFile = open("ExpertStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()
'''

bundle = loadBundleInfo('assetinfo.json')


### Noodle fuckery
# Add arrays
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []

## do note scripts here

assignPlayerToTrack(0.001,'helo')
posTween(0.002,'helo', 4, 'easeLinear', [0,1000,0,0], [0,1000,0,1])

InstantiatePrefab(0.001, bundle['prefabs']['unfuck'], 'unfuck', localPosition=[0,1000,17.5], localRotation=[0,214,0])
destroyObject(8, 'unfuck')
InstantiatePrefab(8, bundle['prefabs']['fuck'], 'FUCK', localPosition=[0,1000,17.5], localRotation=[0,214,0])


### Save json to Ex+ file
diPlusFile = open('ExpertPlusStandard.dat', 'w')
diPlusFile.write(json.dumps(exData,indent=2))
diPlusFile.close()