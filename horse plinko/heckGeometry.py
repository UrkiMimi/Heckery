## Geometry based library for noodle maps
from Noodled import *

# adds geometry
def addPrimitiveModel(type, material, position, localRotation, scale):
    exData['customData']['environment'].append(dict(
        scale=scale,
        position=position,
        localRotation=localRotation,
        geometry={'type':type,'material':material}
        ))

def addPrimitiveModelTrack(type, material, position, localRotation, scale, track):
    exData['customData']['environment'].append(dict(
        scale=scale,
        position=position,
        localRotation=localRotation,
        track=track,
        geometry={'type':type,'material':material}
        ))

# adds geometry
def addMaterial(shader, color, unlit, matName):
    if not(unlit):
        exData['customData']['materials'][matName] = dict(shader=shader,color=color)
    else:
        exData['customData']['materials'][matName] = dict(shader=shader,color=color,shaderKeywords=[])