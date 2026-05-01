### Basic preperation stuff
import json
from hamen.main import *
from hamen.noodle import *
from hamen.chroma import *
'''
exFile = open("ExpertStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()
'''

arrayFile = open('array.json','r')
array = json.loads(arrayFile.read())
arrayFile.close()

### Noodle fuckery
# Add arrays
#exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['environment'] = []
exData['customData']['materials'] = {}

## Urki note time
'''
I used to keep the scripts for modcharts in one file but it leads to it being horribly organized so 
I'm storing it in megaScript.py since it keeps this project a lot more organized and makes me able 
to use the same script for multiple modcharts without retweaking.
This dumb change will probably be in future charts that I make.
'''

## animations
# init
spawnFakeNotesWithTrackAt(0,2,True,0,'peeb cube')
assignObstaclesToTrack(0,2,'peeb hand')
forceOffset(0,2,-10)
forceOffset(0,2,-10)

# freeze time for animation setup
time(0,'peeb cube',1,'easeStep',0.5,0.5)
time(0,'peeb hand',1,'easeStep',0.25,0.25)

# actual animation stuff
posTweenObjekt(0.05,'peeb cube',0,'easeStep',[0,0,0,0],[-1.3,0.4,3.605525,0])
rotate(0.05,'peeb cube',0,'easeStep',[0,0,0,0],[0,30,0,0])
dissolve(8.47,'peeb cube',0.6,1,0)
dissolveArrow(8.47,'peeb cube',0.6,1,0)

#guh
posTweenObjekt(8.47,'peeb cube',0.6,'easeInQuart',[-1.3,0.8,3.605525,0],[-1.3,4.5,3.605525,1])
#localRotate(8.47,'peeb cube',0.6,'easeInQuad',[0,0,0,0],[45,75,45,1])
scaleTween(8.47,'peeb cube',0.6,'easeInQuart',[1,1,1,0],[2,2,2,1])

# wall stuff
posPointDef(1,'peeb hand', 8.08, array['_array'])
exData['colorNotes'].pop()
dissolve(8.47,'peeb hand',0.6,1,0)


# heck geometry
addMaterial('Standard',[0.1,0.1,0.1],True,'pianoB')
addMaterial('Standard',[1,1,1],True,'pianoA')

addPrimitiveModel('Cube','pianoB',[-0.3867495,0.374,2.654629],[0,30,29.23],[1.6,0.025,0.025])
addPrimitiveModel('Cube','pianoB',[-0.1797497,0.374,3.013164],[0,30,29.23],[1.6,0.025,0.025])
addPrimitiveModel('Cube','pianoB',[-0.3867495,0.374,2.654629],[0,30,-29.23],[1.6,0.025,0.025])
addPrimitiveModel('Cube','pianoB',[-0.1797497,0.374,3.013164],[0,30,-29.23],[1.6,0.025,0.025])
addPrimitiveModel('Cube','pianoB',[0.265,0.81,2.698],[0,30,0],[0.034875,0.025,0.2118208])
addPrimitiveModel('Cube','pianoB',[0.1105659,0.81,2.787815],[0,30,0],[0.034875,0.025,0.2118208])
addPrimitiveModel('Cube','pianoB',[-0.2929415,0.81,3.02078],[0,30,0],[0.034875,0.025,0.2118208])
addPrimitiveModel('Cube','pianoB',[-0.515233,0.81,3.14912],[0,30,0],[0.034875,0.025,0.2118208])
addPrimitiveModel('Cube','pianoB',[-0.7169867,0.81,3.265602],[0,30,0],[0.034875,0.025,0.2118208])
addPrimitiveModel('Cube','pianoA',[-0.2372497,0.781,2.913571],[0,30,0],[1.395,0.05,0.325])
addPrimitiveModel('Cube','pianoB',[-0.2872497,0.7409999,2.826968],[0,30,0],[1.5,0.1,0.5])



### Save json to Ex+ file
countUp()

export_diff()