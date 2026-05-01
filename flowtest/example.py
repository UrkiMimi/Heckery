### Basic preperation stuff
import json
from hamen.main import *
from hamen.noodle import *
from hamen.chroma import *
from hamen.vivify import *



# infodat
infoDat_addRequirement([
    "Noodle Extensions",
    "Chroma"
])

# add arrays for important stuff
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []


## region do note scripts here
assignNotesToTrack(28,999,'circle')
circleThing(28,999,6)

dissolveBoth(5,'circle',0,0,0)
dissolveBoth(24,'circle',1,0,1,'easeOutQuad')

# increment run
countUp()

### Save edited json and info dat
export_infoDat()
export_diff()