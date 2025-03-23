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
    'Timbaland Chevron',
    'ojooj',
    '0.0.2',
    'TimbalandEnvironment',
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
disableObject('TimbalandEnvironment.[0]Environment.[25]Light (4)','Exact')
disableObject('TimbalandEnvironment.[0]Environment.[27]Light (5)','Exact')
# make chevron
dupe('TimbalandEnvironment.[0]Environment.[26]Light (6)','Exact',4)
disableObject('TimbalandEnvironment.[0]Environment.[26]Light (6)','Exact')
tubeEditer('TimbalandEnvironment.[0]Environment.[35]Light (6)(Clone)','Exact',
       [1.5,3.5,55],
       [0.8,2.05/3.5,0.8],
       [0,0,55],True,4,3,0.4)
tubeEditer('TimbalandEnvironment.[0]Environment.[36]Light (6)(Clone)','Exact',
       [-1.5,3.5,55],
       [0.8,2.05/3.5,0.8],
       [0,0,-55],True,4,3,0.4)
tubeEditer('TimbalandEnvironment.[0]Environment.[37]Light (6)(Clone)','Exact',
       [-1.5,3.5,85],
       [0.8,2.05/3.5,0.8],
       [0,0,-55],True,4,3,0.4)
tubeEditer('TimbalandEnvironment.[0]Environment.[38]Light (6)(Clone)','Exact',
       [1.5,3.5,85],
       [0.8,2.05/3.5,0.8],
       [0,0,55],True,4,3,0.4)

sanityCheck()

### Save json to Ex+ file
exPlusFile = open('doubleChev.dat', 'w')
exPlusFile.write(json.dumps(envData, indent=2))
exPlusFile.close()