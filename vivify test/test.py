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

# Load bundle
bundle = loadBundleInfo('bundleinfo.json')

### Noodle fuckery
# Add arrays
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []

## do note scripts here
# do bounce on each beat with real notes
assignNotesToTrack(0,110,'notes')
lazyOffset(68,110,1)

# spawn funi cube
InstantiatePrefab(59, bundle['prefabs']['funi cube'], 'funi')
destroyObject(68, 'funi')

for i in range(10):
    InstantiatePrefab(59, bundle['prefabs']['rigidcube'], f'rCube{i}', localPosition=[round(rand.uniform(-10,10),3),round(rand.uniform(-10,10),3),round(rand.uniform(-10,10),3)], scale=[0.5,0.5,0.5])
InstantiatePrefab(59, bundle['prefabs']['plane'], 'plane')



# loop for assignpathbounce
for i in range(110-68):
    offset = ((i%2-0.5)*2)*30
    assignPathAnimation(i+68,'notes',0.1,worldRotation=[[0,offset,0,0],[0,0,0,0.5,'easeOutQuad']])
    assignPathAnimation(i+68.9,'notes',0.9,worldRotation=[[0,0,0,0]])

    # scale bounce
    scaleTween(i+68,'notes',0.8,'easeOutQuad',[4,0.25,1,0],[1,1,1,1])

    # set screen displacement material
    unityBlit(68+i, 1, '_DisplacementIntensity', 'Float', [[0.1,0],[0,1,'easeOutSine']], asset='assets/materials/post.mat')
    

# funny fake note
spawnFakeNotesWithSpiral(52, 60, 1, [-90,0,0])
spawnFakeNotesWithSpiral(52, 60, 1, [90,0,0])

# funny fake note part 2
spawnFakeNotesWithSpiral(68, 110, 1/4, [-90,0,0])
spawnFakeNotesWithSpiral(68, 110, 1/4, [90,0,0])

ghostArrows(68,110,4,0.05,0.4)

### Save json to Ex+ file
diPlusFile = open('ExpertPlusStandard.dat', 'w')
diPlusFile.write(json.dumps(exData,indent=2))
diPlusFile.close()