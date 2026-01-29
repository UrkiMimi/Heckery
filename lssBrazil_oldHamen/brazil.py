### Basic preperation stuff
import json
import random as rand
import math as mth

exFile = open("ExpertStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()


### Noodle fuckery
# Add fake note array
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []


## ==some shit may be left overs from c18 python rewrite==
# Using leftovers from that mess is encouraged -dwm

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

# Similar to assignNotesToTrack but has the ability to seperate track based on line index
def assignIndexNotesToTrack(startTime, endTime, starterName):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['track'] = starterName + str(exData['colorNotes'][index]['x'])

# Returns an array for all notes at a specified time
def findNoteAt(nTime):
    timeList = []
    for index in range(len(exData['colorNotes'])):
        if (nTime == exData['colorNotes'][index]['b']):
            timeList.append(index)
    return(timeList)

# Spawns a bulk of notes based on nTime
def kablooey(amount, nTime, spread):
    nBuffer = findNoteAt(nTime)
    for index2 in nBuffer:
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        for index in range(amount):
            # to keep my sanity
            fakeIndex = index + fakeNoteLength

            # General customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][nBuffer[0]]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + 0.001
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = 3

            # Animation Fuckery
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['localRotation'] = [
                [0,0,0,0.5],
                [rand.randint(0,360),rand.randint(0,360),rand.randint(0,360),0.65,'easeOutExpo']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [0,0,0,0.5],
                [round(rand.uniform(-spread,spread),3),round(rand.uniform(-spread,spread),3),round(rand.uniform(0,spread),3),0.65,'easeOutExpo']
                ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0,0.5],
                [1,0.51,'easeOutExpo'],
                [0,0.75,'easeInQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0,0.5],
                [1,0.51,'easeOutExpo'],
                [0,0.75,'easeInQuad']
            ]

# Makes the notes tween from random positions 
def randMovements(startTime, endTime, noteOffset, easing):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = noteOffset
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-4,4),rand.randint(-4,4),0,0.25],
                [0,0,0,0.4,easing]
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [rand.randint(0,360),rand.randint(0,360),rand.randint(0,360),0.25],
                [0,0,0,0.4,easing]
            ]

# Does a scale like trail at specified time
def scaleTrail(time, amount):
    nBuffer = findNoteAt(time)
    for index2 in nBuffer:
        t = 0
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        for index in range(amount):
            # sanity check
            fakeIndex = index + fakeNoteLength

            # general customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + t
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 0.001
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = -1
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}

            # Note fuckery
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [0,0,index*10,0]
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['scale'] = [
                [index*2,index*2,index*2,0]
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0,0.5],
                [1,0.5],
                [0,0.65,'easeInExpo']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0,0.5],
                [1,0.5],
                [0,0.7,'easeInCirc']
            ]
            t+=0.02

# Does trail at specified time
def trail(time):
    nBuffer = findNoteAt(time)
    for index2 in nBuffer:
        t = 0
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        for index in range(32):
            # to keep my sanity
            fakeIndex = index + fakeNoteLength

            # General customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + t
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 20
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = 0
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}

            # Yippie
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [0,0,index*2,0.9],
                [0,0,100,0.95,'easeInCirc']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),0],
                [0,0,index*15,0.25,'easeOutQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0,0.5],
                [0.25,0.51,'easeOutExpo'],
                [0,0.85,'easeInQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0,0.5],
                [0.75,0.51,'easeOutExpo'],
                [0,0.85,'easeInQuad']
            ]
            t+=0.02

# Does a knockoff 'Oh no.' effect
def ohYes(startTime, endTime):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['colorNotes'][index]['customData']['disableNoteLook'] = True
            exData['colorNotes'][index]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 2
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,0,40,0],
                [0,0,21,0.25,'easeOutExpo'],
                [0,0,0,0.5,'easeInSine'],
                [0,0,-20,0.75,'easeOutSine']
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [270,270,270,0],
                [0,0,0,0.25,'easeOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0],
                [1,0.15],
                [1,0.65],
                [0,0.75]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0],
                [1,0.15],
                [1,0.65],
                [0,0.75]
            ]

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
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0.25],
                [0.95,0.45]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0.25,0],
                [0.75,0.25]
            ]

# Makes the notes go through a zig zag thing
def zigZagWobble(startTime, endTime, noteOffset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = noteOffset
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [10,0,0,0],
                [-8,0,0,0.05,'easeInOutQuad'],
                [6,0,0,0.1,'easeInOutQuad'],
                [-4,0,0,0.15,'easeInOutQuad'],
                [2,0,0,0.2,'easeInOutQuad'],
                [-1,0,0,0.25,'easeInOutQuad'],
                [0,0,0,0.3,'easeInOutQuad'],
            ]

# Make the notes go all over the place for the majority of their lifetime
def lordFoog(startTime, endTime, scaling, posOffset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 10
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),0,'easeOutQuad'],
                [rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),0.1,'easeOutQuad'],
                [rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),0.2,'easeInExpo'],
                [rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),rand.randint(-posOffset,posOffset),0.3,'easeInExpo'],
                [rand.randint(-posOffset/2,posOffset/2),rand.randint(-posOffset/2,posOffset/2),rand.randint(-posOffset/2,posOffset/2),0.4,'easeInExpo'],
                [0,0,0,0.45,'easeOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['interactable'] = [
                [0,0.4],
                [1,0.45]
            ]
            if scaling:
                exData['colorNotes'][index]['customData']['animation']['scale'] = [
                    [10,10,10,0.3],
                    [1,1,1,0.45,'easeOutExpo']
                ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0],
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0.1,'easeOutQuad'],
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0.2,'easeInExpo'],
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0.3,'easeInExpo'],
                [rand.randint(-90,90),rand.randint(-90,90),rand.randint(-90,90),0.4,'easeInExpo'],
                [0,0,0,0.45,'easeOutExpo']
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

# Makes the notes tween from random positions 
def xShift(startTime, endTime):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 1
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-2,2),0,0,0],
                [0,0,0,0.4,'easeInOutExpo']
            ]

# Makes the notes on a track bust a move on each beat
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
        [0,0,0,0.25,'easeInOuExpo'],
        [-0.1,0,0,0.5],
        [0,0,0,0.75,'easeInOutExpo']
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
            [0,0,15,0.25],
            [0,0,18,0.3,'easeOutSine'],
            [0,0,0,0.5,'easeInSine'],
            [0,0,-20,1]
        ]

# Makes the notes on assigned track do a wave like effect on the y axis
def vertWave(startTime, endTime, trackName, duration, low, high):
    t = endTime - startTime
    exData['customData']['customEvents'].append(dict(b=startTime, t='AnimateTrack', d={'duration':duration, 'repeat':t/duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        [0,low,0,0],
        [0,high,0,0.5,'easeInOutQuad'],
        [0,low,0,1,'easeInOutQuad']
    ]

# simple offset script
def simpleOffset(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset

# Makes notes assigned on a track either squish, rotate, or offset a note on the selected time
def bounce(nTime, trackName, duration, rotateAnim, bounceAnim, offsetAnim):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    if rotateAnim:
        exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['localRotation'] = [
            [0,0,-90,0],
            [0,0,180,0.1],
            [0,0,360,1,'easeOutExpo']
        ]
    elif bounceAnim:
        exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
            [4,0.25,1,0],
            [1,1,1,1,'easeOutExpo']
        ]
    elif offsetAnim:
        exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
            [0,0,3,0],
            [0,0,0,0,'easeInSine']
        ]

# Notes just rotate in weirdly i guess
def yack(startTime, endTime, offset,easing):
    nBuffer = []
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            nBuffer.append(index)
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['animation']['offsetWorldRotation'] = [
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(0,360),0],
                [0,0,0,0.35,easing]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0]
            ]
    
    for index2 in nBuffer:
        fakeIndex = len(exData['customData']['fakeColorNotes'])
        exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
        exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = offset - 1
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
            [rand.randint(-180,180),rand.randint(-180,180),rand.randint(0,360),0],
            [0,0,0,0.35,easing]
        ]  
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
            [0,0],
            [1,0.5,'easeOutQuad']
        ]
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
            [0,0]
        ]

#shifts note on specified track and time
def trackShift(nTime, duration, trackName, x, y, z):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        [x,y,z,0],
        [0,0,0,1,'easeOutQuad']
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [0.75,0],
        [1,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [0.75,0],
        [1,1]
    ]

# dissolves note on specified track and time
def trackDissolve(nTime, duration, trackName):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [1,0],
        [0,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [1,0],
        [0.25,1]
    ]

# Does an elastic bounce like effect on notes that have the track assigned
def trackBounceDissolve(nTime, duration, trackName):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [0,0],
        [1,0.01]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
        [2,2,2,0],
        [1,1,1,1,'easeOutElastic']
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [0,0],
        [1,0.01]
    ]

# Makes all notes dissapear on assigned track, use this in case you have a track effect that makes notes undissolve.
def dissolveFix(nTime, duration, trackName):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [0,0],
        [0,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [0,0],
        [0,1]
    ]

# Tangent Part 2
def tan(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            r1 = []
            r2 = []
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['colorNotes'][index]['customData']['animation'] = {}

            for i in range(50):
                oneMin = (49 - i) / 50
                r1.append([0,(mth.tan(i/5)*2.5*oneMin),0,i/100,'easeInOutSine'])
                r2.append([1,abs(mth.tan(i/5)*1.25*oneMin)+1,1,i/100,'easeInOutSine'])
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = r1
            exData['colorNotes'][index]['customData']['animation']['scale'] = r2

### do note scripts here

# hel lo *fades in*
rotationFly(19,52,3)
ghostArrows(19,69,2,5)
randMovements(52.5,68,3,'easeInOutBack')
kablooey(2,67.5,10)
trail(68)

# ls ~/vocals
elasticRotate(75)
assignIndexNotesToTrack(69,75,'v')
simpleOffset(69,75,2.5)
# what the fuck is wrong with me
vertWave(69,75,'v0',4,0.075,-0.075)
vertWave(69,75,'v1',4,-0.075,0.075)
vertWave(69,75,'v2',4,0.075,-0.075)
vertWave(69,75,'v3',4,-0.075 ,0.075)

tangent(76,84,3)
ohYes(84.5,95.5)
assignNotesToTrack(76,78,'hi',False)
bounce(75,'hi',1,False,True,True)

assignNotesToTrack(101.5,114,'hi0',False)
bounce(101,'hi0',1,True,False,False)
trackShift(102.25,0.75,'hi0',0.5,0,0)
trackShift(104.5,0.75,'hi0',-0.5,0,0)
bounce(107,'hi0',1,False,True,True)
trackDissolve(108,6,'hi0')
tan(108,114,3)
simpleOffset(101,107,3)
ohYes(116,127)
tangent(128,131.5,3)
friedRoad(107)

scaleDown(96,99.5,0,1,'easeOutElastic',5)
scaleTrail(99.5,4)

# i am going to turn into a 
lordFoog(132.5,140, False, 20)
assignNotesToTrack(132.5,140,'hi1',False)
dissolveFix(122.5,10,'hi1')
trackBounceDissolve(131.5,1,'hi1')


### Save json to Ex+ file
exPlusFile = open('ExpertPlusStandard.dat', 'w')
exPlusFile.write(json.dumps(exData))
exPlusFile.close()