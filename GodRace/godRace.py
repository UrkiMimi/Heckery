#imports 
from Hamen import *
from hamenNoodle import *
from hamenChroma import *
from hamenVivify import *
import random as rand

#init
infoDat_addRequirement([
    "Noodle Extensions",
    "Chroma",
    "Vivify"
])

bundle = loadBundleInfo('bundleinfo.json')
infoDat_injectCRCs(bundle)

# add stuff
exData['customData'] = {}
exData['customData']['customEvents'] = []

## add cubes and shit
for z in range(10):
    for y in range(10):
        for x in range(10):
            InstantiatePrefab(
                0, bundle['prefabs']['godracecube'], 
                f'cube{rand.randint(0,9999999)}', 'cubes', 
                position=[(x-5)*2,(y-5)*2,(z-5)*2],
                scale=[0,0,0]
            )

scaleTween(1,'cubes',2,'easeOutQuad',[0,0,0,0],[2,2,2,1])

# save
export_diff()
export_infoDat()

countUp()