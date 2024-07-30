### Basic preperation stuff
import json
import random as rand
import math

exFile = open("ExpertStandard.dat", "r")
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

def assignObstacleToTrack(startTime, endTime, trackName):
    for index in range(len(exData['obstacles'])):
        if (startTime <= exData['obstacles'][index]['b']) and (endTime >= exData['obstacles'][index]['b']):
            if not('customData' in exData['obstacles'][index]):
                exData['obstacles'][index]['customData'] = {}
            exData['obstacles'][index]['customData']['track'] = trackName

### Notemod Stuff
# Returns an array for all notes at a specified time
def findNoteAt(nTime):
    timeList = []
    for index in range(len(exData['colorNotes'])):
        if (nTime == exData['colorNotes'][index]['b']):
            timeList.append(index)
    return(timeList)

# Makes the notes act like a tangent graph
def tangent(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            # Invert xAxis tangent if note is blue
            if (exData['colorNotes'][index]['c'] == 1):
                xAxis = -25
            else:
                xAxis = 25

            # customData setup
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            
            # Animations
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,0,0,0.25],
                [xAxis,0,0,0.3,'easeInExpo'],
                [-xAxis,0,0,0.3],
                [0,0,0,0.35,'easeOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['scale'] = [
                [1,1,1,0.25],
                [abs(xAxis)/2,1,1,0.3,'easeInExpo'],
                [abs(xAxis)/2,1,1,0.3],
                [1,1,1,0.35,'easeOutExpo']
            ]

# Makes the notes tween from random positions 
def rotationFly(startTime, endTime, noteOffset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = noteOffset
            exData['colorNotes'][index]['customData']['animation']['offsetWorldRotation'] = [
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),0],
                [0,0,0,0.45,'easeOutQuad']
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [rand.randint(-90,90),rand.randint(-90,90),rand.randint(-90,90),0.25],
                [0,0,0,0.45,'easeOutQuad']
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0.25],
                [0.95,0.45]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0.25,0],
                [0.75,0.25]
            ]

# Similar to rotationFly but instead spawns in fake arrows around the player
def ghostArrows(startTime, endTime, amount, noteOffset):
    nBuffer = []

    # Add notes in the time zone to note buffer
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            nBuffer.append(index)
            
    # real fun
    for index2 in nBuffer:
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        t = 0
        for index in range(amount):
            # to keep my sanity
            fakeIndex = index + fakeNoteLength

            # General customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + t
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = noteOffset

            # Animations
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),0],
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),1,'easeInOutQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-4,4),rand.randint(-50,50),5,0],
                [rand.randint(-4,4),rand.randint(-50,50),5,0,'easeOutSine']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0.25,0],
                [0,0.25]
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0.25,0],
                [0.75,0.25]
            ]
            t+=0.1
    
# Makes the notes spin and float into the players view
def friedRoad(nTime):
    # Get notes
    nBuffer = findNoteAt(nTime)

    # Add fried road animation to selected notes
    for index in nBuffer:
        exData['colorNotes'][index]['customData'] = {}
        exData['colorNotes'][index]['customData']['animation'] = {}
        exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 1
        exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
            [rand.randint(-10,10),rand.randint(-10,10),0,0],
            [0,0,0,0.45,'easeOutBack']
        ]
        exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
            [0,0,360,0],
            [0,0,180,0.15],
            [0,0,0,0.45,'easeOutQuad']
        ]

# Makes the notes on a track do a funny on each beat
def glitchTrack(startTime, endTime, trackName, duration):
    t = endTime - startTime
    exData['customData']['customEvents'].append(dict(b=startTime, t='AnimateTrack', d={'duration':duration, 'repeat':t/duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [0.25,0.5],
        [1,0.5],
        [1,1],
        [0.25,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [1,0.5],
        [0.25,0.5],
        [0.5,1],
        [1,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        [0.1,0,0,0],
        [0,0,0,0.5,'easeOutElastic'],
        [-0.1,0,0,0.5],
        [0,0,0,1,'easeOutElastic']
    ]

# Makes the notes move back and forth on each 1/2 beat
def theFunnyBounce(startTime, endTime, trackName, x, y):
    t = endTime - startTime
    # Track Part
    exData['customData']['customEvents'].append(dict(b=startTime, t='AnimateTrack', d={'duration':1, 'repeat':t}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        [x,y,0,0],
        [-x,-y,0,0.5,'easeOutBack'],
        [x,y,0,1,'easeOutBack']
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [1,0],
        [0.5,0.5,'easeInExpo'],
        [1,0.5],
        [0.5,1,'easeInExpo']
    ]

    nBuffer = []
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            nBuffer.append(index)
            exData['colorNotes'][index]['customData'].pop('track')
            exData['colorNotes'][index]['customData']['disableNoteLook'] = True
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [1,0]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0]
            ]
    for index2 in nBuffer:
        fakeIndex = len(exData['customData']['fakeColorNotes'])

        exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
        exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['track'] = trackName
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
            [0,0]
        ]

# Scales notes to desired size, easing is customizable
def scaleDown(startTime, endTime, scaleStart, scaleEnd, easing, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['colorNotes'][index]['customData']['animation']['scale'] = [
                [scaleStart,scaleStart,scaleStart,0.25],
                [scaleEnd,scaleEnd,scaleEnd,0.4,easing]
            ]
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,(scaleStart-1)/2,0,0.25],
                [0,0,0,0.4,easing]
            ]

# Makes notes spring up on desired time
def elasticRotate(time):
    nBuffer = findNoteAt(time)

    for index in nBuffer:
        exData['colorNotes'][index]['customData'] = {}
        exData['colorNotes'][index]['customData']['animation'] = {}
        exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
        exData['colorNotes'][index]['customData']['noteJumpMovementSpeed'] = 0.001
        exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 3
        exData['colorNotes'][index]['customData']['animation']['offsetWorldRotation'] = [
            [0,0,180,0],
            [0,0,0,0.25,'easeOutElastic']
        ]
        exData['colorNotes'][index]['customData']['animation']['interactable'] = [
            [0,0],
            [1,0.35]
        ]
        exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
            [0,0],
            [1,0.25],
        ]
        exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
            [0,0],
            [1,0.25],
        ]
        exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
            [0,0,12,0.25],
            [0,0,14,0.3,'easeOutSine'],
            [0,0,0,0.5,'easeInSine'],
            [0,0,-20,1]
        ]

# Does a reflection like effect on the y-axis for notes
def noteReflection(startTime, endTime, reflectionOffset):
    nBuffer = []
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            nBuffer.append(index)
    for index in nBuffer:
        # just so i dont have to copy and paste code
        exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index]))
        # My shitty code bugs out if I dont reset customData for fakeColorNotes so a reset it is
        exData['customData']['fakeColorNotes'][index]['customData'] = {}
        exData['customData']['fakeColorNotes'][index]['x'] = 3 - exData['colorNotes'][index]['x']
        exData['customData']['fakeColorNotes'][index]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][index]['customData']['animation']['offsetPosition'] = [
            [0,1-reflectionOffset,0,0]
        ]
        exData['customData']['fakeColorNotes'][index]['customData']['animation']['scale'] = [
            [-1,1,1,0]
        ]
        exData['customData']['fakeColorNotes'][index]['customData']['animation']['offsetWorldRotation'] = [
            [0,0,180,0]
        ]
            
# Track animations
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
        [0,oldx,0,0],
        [0,x,0,1],
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['rotation'] = [
        [0,oldx,0,0],
        [0,x,0,1],
    ]

def dissolveTrack(nTime, trackName, duration, easing, old, new):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [old,0],
        [new,1]
    ]

def backTrack(nTime, trackName, duration, easing, old, new):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['position'] = [
        [0,0,old,0],
        [0,0,new,0]
    ]

### Wall Mods
def lazyNoteOffset(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset

def lazyObstacleMovement(startTime, endTime, offset, jumpSpeed, fake):
    for index in range(len(exData['obstacles'])):
        if (startTime <= exData['obstacles'][index]['b']) and (endTime >= exData['obstacles'][index]['b']):  
            if not('customData' in exData['obstacles'][index]):
                exData['obstacles'][index]['customData'] = {}
            exData['obstacles'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['obstacles'][index]['customData']['noteJumpMovementSpeed'] = jumpSpeed
            exData['obstacles'][index]['customData']['uninteractable'] = fake

### do note scripts here
#Init
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[5]Construction', 'Envir', 'Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[3]Floor', 'FuckouttaHere', 'Exact')
lazyObstacleMovement(0,100,5,5,True)
assignObstacleToTrack(0,100,'River')

# Animation stuff
backTrack(0,'Envir',6, 'easeOutQuad', 0, 50)
backTrack(0,'FuckouttaHere', 0, 'easeLinear', 100000, 100000)
dissolveTrack(0,'River',3,'easeOutSine',0,0)
dissolveTrack(3,'River',2.5,'easeOutSine',0,1)
dissolveTrack(36,'River',6,'easeOutSine',1,0)
noteReflection(0,36,0.5)
ghostArrows(0,35,5,5)
ghostArrows(36,38,128,5)




### Save json to Ex+ file
exPlusFile = open('ExpertPlusStandard.dat', 'w')
exPlusFile.write(json.dumps(exData))
exPlusFile.close()