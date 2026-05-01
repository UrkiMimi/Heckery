### Basic preperation stuff
import json
import random as rand
import math

exFile = open("EasyStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()


### Noodle fuckery
# Add fake note array
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['environment'] = []

# Assigns notes to a track
def assignNotesToTrack(startTime, endTime, trackName, colorCheck):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            if colorCheck:
                if (exData['colorNotes'][index]['c'] == 0):
                    exData['colorNotes'][index]['customData']['track'] = trackName + '1'
                else:
                    exData['colorNotes'][index]['customData']['track'] = trackName + '2'
            else:
                exData['colorNotes'][index]['customData']['track'] = trackName

def assignEnvironmentToTrack(envName, trackName, lkMethod):
    exData['customData']['environment'].append(dict(id=envName, lookupMethod=lkMethod, track=trackName))

# Returns an array for all notes at a specified time
def findNoteAt(nTime):
    timeList = []
    for index in range(len(exData['colorNotes'])):
        if (nTime == exData['colorNotes'][index]['b']):
            timeList.append(index)
    return(timeList)

def convertNoteToFake(startTime, endTime):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index]))
            exData['colorNotes'].pop(index)

def noteSetup(nTime, trackName, duration, scale, pos, dissolveArrow):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [scale,scale]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [pos,pos]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [dissolveArrow,dissolveArrow]

# Bounce on track
def quagBounce(nTime, trackName, duration):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
        [4,0.25,1,0,'easeInOutSine'],
        [0.5,2,1,0.25,'easeInOutSine'],
        [1.5,0.67,1,0.5,'easeInOutSine'],
        [0.8,1.25,1,0.75,'easeInOutSine'],
        [1,1,1,1,'easeInOutSine']
    ]

def squish(nTime, trackName, duration, easing):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
        [4,0.25,0,0],
        [1,1,1,1]
    ]

def turn(nTime, trackName, duration, easing, oldx,x):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetWorldRotation'] = [
        [oldx,0,0,0],
        [x,0,0,1],
    ]
    
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['rotation'] = [
        [oldx,0,0,0],
        [x,0,0,1],
    ]

def lazyOffset(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset

# Use only for environment tracks
def posTween(nTime, trackName, duration, easing, oldPosVector, posVector):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['localPosition'] = [
        oldPosVector,
        posVector
    ]    

# Use only for note tracks
def posTweenNote(nTime, trackName, duration, easing, oldPosVector, posVector):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        oldPosVector,
        posVector
    ]    

def timeTrack(nTime, trackName, duration, easing, ogTime, time):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['time'] = [
        [ogTime,0],
        [time,1]
    ]    

def dissolve(nTime, trackName, duration, be, af):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [be,0],
        [af,1]
    ]
    
def assignPlayerToTrack(nTime, trackName):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AssignPlayerToTrack', d={'track':trackName}))

# Disables object in scene
def disableObject(envId, lookupMe):
    exData['customData']['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False))

def dupe(envId, lookupMe, dupe):
    exData['customData']['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False,duplicate=dupe))

# Customization for center tubelight
def editer(envId, lookupMe, pos, sc, rotation, enabled):
    exData['customData']['environment'].append(dict(
        id=envId, 
        lookupMethod=lookupMe,
        localPosition=pos,
        scale=sc,
        localRotation=rotation,
        active=enabled
        ))


### do note scripts here
# Init Stuff
assignEnvironmentToTrack('BTSEnvironment.[0]Environment','player','Exact')
assignPlayerToTrack(0,'player')
disableObject('BTSEnvironment.[0]Environment.[35]GlowLineC','Exact')
disableObject('BTSEnvironment.[0]Environment.[6]PlayersPlace.[0]Mirror','Exact')
disableObject('BTSEnvironment.[0]Environment.[6]PlayersPlace.[2]Construction','Exact')
disableObject('BTSEnvironment.[0]Environment.[6]PlayersPlace.[3]RectangleFakeGlow','Exact')
editer('BTSEnvironment.[0]Environment.[4]TrackMirror','Exact',
       [0.3,0,-92],
       [1,1,1],
       [0,0,0],
       True)
editer('BTSEnvironment.[0]Environment.[5]Construction','Exact',
       [0,0,-100],
       [1,1,1],
       [0,0,0],
       True)
editer('BTSEnvironment.[0]Environment.[34]GlowLineR','Exact',
       [0.6,-0.05,-92],
       [1,1,1],
       [0,0,0],
       True)
editer('BTSEnvironment.[0]Environment.[33]GlowLineL','Exact',
       [-0.6,-0.05,-92],
       [1,1,1],
       [0,0,0],
       True)
assignNotesToTrack(0,2,'cube',False)
noteSetup(0,'cube',1,[2,2,2,0],[0,1,0,0],[0,0])
convertNoteToFake(0,2)
timeTrack(0,'cube',0.1,'easeLinear',0,0)
dissolve(0,'cube',0.25,0,0)

# Animation stuff
dissolve(2,'cube',0.25,0,1)
posTweenNote(8.5,'cube',1.476,'easeOutQuad',[0,1,0,0],[0,3,0,1])
posTweenNote(9.976,'cube',1.25,'easeInExpo',[0,3,0,0],[0,0.4,0,1])
posTweenNote(11.226,'cube',2,'easeInOutSine',[0,0.4,0,0],[0,25000000,0,1])
posTween(11.226,'player',2,'easeInOutSine',[0,0,0,0],[0,25000000,0,1])

### Save json to Ex+ file
exPlusFile = open('NormalStandard.dat', 'w')
exPlusFile.write(json.dumps(exData,indent=2))
exPlusFile.close()