### Basic preperation stuff
from hamen.main import *
from hamen.noodle import *
from hamen.chroma import *

infoDat_addRequirement([
    "Noodle Extensions",
    "Chroma"
])

### Noodle fuckery
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []

### do note scripts here

# hel lo *fades in*
rotationFly(19,52,3)
ghostArrows(19,69,2,5)
randMovements(52.5,68,3)
kablooey(2,67.5,10)
trail(68)

# ls ~/vocals
elasticRotate(75)
for i in range(4):
    assignNoteLaneToTrack(69, 75, f'v{i}', i)
forceOffset(69,75,2.5)
# what the fuck is wrong with me

for i in range(4):
    assignPathAnimation(75, f'v{i}', 0.5, 'easeOutExpo', [[0,(i%2)-0.5,0,0],[0,0,0,1]])

tangent(76,84,3)
ohYes(84.5,95.5)
assignNotesToTrack(76,78,'hi',False)
scaleTween(75, 'hi', 1, 'easeOutExpo', [2,0.5,0.5,0], [1,1,1,1])

assignNotesToTrack(101.5,114,'hi0',False)

# these effects are completely deprecated and no longer exist :^)
"""
bounce(101,'hi0',1,True,False,False)
trackShift(102.25,0.75,'hi0',0.5,0,0)
trackShift(104.5,0.75,'hi0',-0.5,0,0)
bounce(107,'hi0',1,False,True,True)
trackDissolve(108,6,'hi0')
tan(108,114,3)"""
forceOffset(101,107,3)
ohYes(116,127)
tangent(128,131.5,3)
friedRoad(107)

scaleDown(96,99.5,0,1,'easeOutElastic',5)
scaleTrail(99.5,4)

# i am going to turn into a 
lordFoog(132.5,140)
assignNotesToTrack(132.5,140,'hi1',False)
# same with these too
#dissolveFix(122.5,10,'hi1')
#trackBounceDissolve(131.5,1,'hi1')


### Save json to Ex+ file
export_diff()
export_infoDat