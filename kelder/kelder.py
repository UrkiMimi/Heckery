'''
This script is easily the most broken out of all the modcharts uploaded here.
If you want to use any of these modchart scripts as a base, I highly recommend using the latest committed ones since most of those have fixed up functions.

- Urki
'''
### Basic preperation stuff
import json
import random as rand

exFile = open("ExpertStandard.dat", "r")
exData = json.loads(exFile.read())
exFile.close()

### Noodle fuckery
# Add fake note array
exData['customData']['fakeColorNotes'] = []


# Returns an array for all notes at a specified time
def findNoteAt(nTime):
    timeList = []

    for index in range(len(exData['colorNotes'])):
        if (nTime == exData['colorNotes'][index]['b']):
            timeList.append(index)
    return(timeList)

def kablooey(amount, nTime, spread):
    nBuffer = findNoteAt(nTime)
    for index in range(amount):
        for index1 in nBuffer:
            # General customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index1]))
            exData['customData']['fakeColorNotes'][index]['customData'] = {}
            exData['customData']['fakeColorNotes'][index]['b'] = exData['customData']['fakeColorNotes'][index]['b'] + 0.001
            exData['customData']['fakeColorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][index]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][index]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['customData']['fakeColorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 3
            # Animation Fuckery
            exData['customData']['fakeColorNotes'][index]['customData']['animation'] = {}
            exData['customData']['fakeColorNotes'][index]['customData']['animation']['localRotation'] = [
                [0,0,0,0.5],
                [rand.randint(0,360),rand.randint(0,360),rand.randint(0,360),0.65,'easeOutExpo']
            ]
            exData['customData']['fakeColorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,0,0,0.5],
                [round(rand.uniform(-spread,spread),3),round(rand.uniform(-spread,spread),3),round(rand.uniform(0,spread),3),0.65,'easeOutExpo']
            ]
            exData['customData']['fakeColorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0.5],
                [1,0.51,'easeOutExpo']
            ]
            exData['customData']['fakeColorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0.5],
                [1,0.51,'easeOutExpo']
            ]


### do note scripts here
findNoteAt(22.125)
kablooey(200, 22.125, 50)


### Save json to Ex+ file
exPlusFile = open('ExpertPlusStandard.dat', 'w')
exPlusFile.write(json.dumps(exData))
exPlusFile.close()