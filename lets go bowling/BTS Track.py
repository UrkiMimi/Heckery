### Basic preperation stuff
import json
import random as rand
import math

envData = {}

### Use this function first
# function that creates the metadata for the environment
def metaData(na,auth,envVer,envName,desc):
    envData['version'] = '1.0.0'
    envData['name'] = na
    envData['author'] = auth
    envData['environmentVersion'] = envVer
    envData['environmentName'] = envName
    envData['description'] = desc
    envData['features'] = {}

metaData(
    'BTS Track',
    'ojooj',
    '0.0.1',
    'BTSEnvironment',
    'holy shit an environment :glaggle:'
)
envData['environment'] = []
### Env Functions
# Disables object in scene
def disableObject(envId, lookupMe):
    envData['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False))

def dupe(envId, lookupMe, dupe):
    envData['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False,duplicate=dupe))

def fogging(envId, lookupMe, atten, offset, startY, height):
    envData['environment'].append(dict(
        id=envId,
        lookupMethod=lookupMe,
        components={'BloomFogEnvironment':{'attenuation':atten,'offset':offset,'startY':startY,'height':height}}
    ))

# Customization for objects
def editer(envId, lookupMe, pos, sc, rotation, enabled):
    envData['environment'].append(dict(
        id=envId, 
        lookupMethod=lookupMe,
        localPosition=pos,
        scale=sc,
        localRotation=rotation,
        active=enabled
        ))
    
# Customization for tubelights you want to do hacky shit with
def tubeEditer(envId, lookupMe, pos, sc, rotation, enabled, id, multi, fogMulti):
    envData['environment'].append(dict(
        id=envId, 
        lookupMethod=lookupMe,
        localPosition=pos,
        scale=sc,
        localRotation=rotation,
        active=enabled,
        components={'ILightWithId':{'lightID':id},'TubeBloomPrePassLight':{'colorAlphaMultiplier':multi,'bloomFogIntensityMultiplier':fogMulti}}
        ))

# fixes env errors
def sanityCheck():
    for index in range(len(envData['environment'])):
        if 'duplicate' in envData['environment'][index]:
            if envData['environment'][index]['duplicate'] == 0:
                envData['environment'][index].pop('duplicate')

### Do Env scripting here
disableObject('BTSEnvironment.[0]Environment.[35]GlowLineC','Exact')
dupe('BTSEnvironment.[0]Environment.[35]GlowLineC','Exact',3)
disableObject('BTSEnvironment.[0]Environment.[35]GlowLineC','Exact')
disableObject('BTSEnvironment.[0]Environment.[8]MagicDoorSprite','Exact')
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
# Track Lights
tubeEditer('BTSEnvironment.[0]Environment.[34]GlowLineR','Exact',
       [0.6,-0.05,-92],
       [1,1,1],
       [90,0,0],
       True,0,1,1)
tubeEditer('BTSEnvironment.[0]Environment.[33]GlowLineL','Exact',
       [-0.6,-0.05,-92],
       [1,1,1],
       [90,0,0],
       True,0,1,1)
editer('BTSEnvironment.[0]Environment.[9]NarrowGameHUD.[0]EnergyPanel','Exact',
       [0,0.6,3.65],
       [0.02,0.02,0.02],
       [0,0,0],
       True)

#Center Light
tubeEditer('BTSEnvironment.[0]Environment.[49]GlowLineC(Clone)','Exact',
       [0,4,65],
       [4,3.5/1.15,4],
       [0,0,90],
       True,0,2.5,4)
tubeEditer('BTSEnvironment.[0]Environment.[50]GlowLineC(Clone)','Exact',
       [2.49,2.84,65],
       [4,1.5/1.15,4],
       [0,0,-38],
       True,4,2.5,4)
tubeEditer('BTSEnvironment.[0]Environment.[51]GlowLineC(Clone)','Exact',
       [-2.49,2.84,65],
       [4,1.5/1.15,4],
       [0,0,38],
       True,4,2.5,4)
fogging('BTSEnvironment.[0]Environment','Exact',0.002,10,-5,2.5)
sanityCheck()

### Save json to Ex+ file
exPlusFile = open('BTSTrack.dat', 'w')
exPlusFile.write(json.dumps(envData, indent=2))
exPlusFile.close()