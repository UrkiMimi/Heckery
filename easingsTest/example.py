### Basic preperation stuff
from hamen.main import *
setup('ExpertStandard.dat', 'ExpertPlusStandard.dat')

# import optionals
from hamen.vivify import *
from hamen.chroma import *
from hamen.noodle import *

# load bundles
bundle = loadBundleInfo('bundleinfo.json')
infoDat_injectCRCs(bundle)

# infodat
infoDat_addRequirement([
    "Noodle Extensions",
    "Chroma",
    "Vivify"
])

heckEasings = [
    'easeLinear',
    'easeStep',
    'easeInSine',
    'easeInQuad',
    'easeInCubic',
    'easeInQuart',
    'easeInQuint',
    'easeInExpo',
    'easeInCirc',
    'easeInBack',
    'easeInElastic',
    'easeInBounce',
    'easeOutSine',
    'easeOutQuad',
    'easeOutCubic',
    'easeOutQuart',
    'easeOutQuint',
    'easeOutExpo',
    'easeOutCirc',
    'easeOutBack',
    'easeOutElastic',
    'easeOutBounce',
    'easeInOutSine',
    'easeInOutQuad',
    'easeInOutCubic',
    'easeInOutQuart',
    'easeInOutQuint',
    'easeInOutExpo',
    'easeInOutCirc',
    'easeInOutBack',
    'easeInOutElastic',
    'easeInOutBounce',
]


# Assigns a bunch of environment ids based on text file
def envBulkRemove(fi):
    f = open(fi, 'r')
    # this is gross
    g = 0
    for line in f:
        # debug print(line.rstrip('\n')) 
        disableObject(line.rstrip('\n'), 'Exact')
        g+=1
    f.close()

#region ### do note scripts here
envBulkRemove('bigMirror.log')

# spawn items
InstantiatePrefab(1, bundle['prefabs']['easingframe'], 'frame')
InstantiatePrefab(0, bundle['prefabs']['point'], 'point', 'point')


# more internal setup
childrenTracks(0, 'axis', ['point'], False)
animateTrack(0, 'axis', 0, pos=[[-5,0,15,0]])


for i in range(len(heckEasings)):
    # xaxis movement
    animateTrack((i*3)+3, 'axis', 1.5 , pos=[[-5,0,14.9,0], [5,0,14.9,1]])
    animateTrack((i*3)+5, 'axis', 1, pos=[[5,0,14.9,0], [-5,0,14.9,1,'easeOutCubic']])

    # line
    InstantiatePrefab((i*3)+3, bundle['prefabs']['line'], 'line', 'point', localPosition=[-5,-1.25,14.9])
    destroyObject((i*3)+5,'line')

    # point animation
    animateTrack((i*3)+3,'point', 1.5, 
                 localPos=[[0,-1.25,0,0], [0,5.75,0,1,heckEasings[i]]])
    animateTrack((i*3)+5,'point', 1, 
                 localPos=[[0,5.75,0,0], [0,-1.25,0,1,'easeOutCubic']])
    
    #text
    InstantiatePrefab((i*3)+3, bundle['prefabs'][heckEasings[i].lower()], 'txt', position=[-1, 6.25, 15])
    destroyObject((i*3)+5,'txt')






# increment run
countUp()

### Save edited json and info dat
export_infoDat()
export_diff()