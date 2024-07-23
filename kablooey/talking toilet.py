### Basic preperation stuff
import json
import random as rand

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

def simpleOffset(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset



# Assigns a bunch of environment ids based on text file
def envBulkAssign(fi):
    f = open(fi, 'r')
    # this is gross
    g = 0
    for line in f:
        # debug print(line.rstrip('\n')) 
        assignEnvironmentToTrack(line.rstrip('\n'),'tr' + str(g),'Exact')
        g+=1
    f.close()


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
# Squish on track
def squish(nTime, trackName, duration, easing):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
        [4,0.25,0,0],
        [1,1,1,1]
    ]

# Spin on track
def spin(nTime, trackName, duration, easing, x,y,z):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['localRotation'] = [
        [x/8,y/8,z/8,0.125],
        [x/7,y/7,z/7,0.25],
        [x/6,y/6,z/6,0.375],
        [x/5,y/5,z/5,0.5],
        [x/4,y/4,z/4,0.625],
        [x/3,y/3,z/3,0.75],
        [x/2,y/2,z/2,0.875],
        [x/1,y/1,z/1,1],
    ]

def randomize(nTime, trackName, duration, easing, intensity):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['localRotation'] = [
        [0,0,0,0],
        [rand.randint(0,360)*intensity/50,rand.randint(0,360)*intensity/50,rand.randint(0,360)*intensity/50,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['position'] = [
        [0,0,0,0],
        [rand.randint(-intensity,intensity),rand.randint(-intensity,intensity),rand.randint(-intensity,intensity),1]
    ]

### do note scripts here
envBulkAssign('env.txt')
simpleOffset(9,10,5)
kablooey(1,9.109,20)
for i in range(301):
    randomize(9.109,'tr'+str(i),4,'easeOutExpo',200)

### Save json to Ex+ file
exPlusFile = open('ExpertPlusStandard.dat', 'w')
exPlusFile.write(json.dumps(exData))
exPlusFile.close()