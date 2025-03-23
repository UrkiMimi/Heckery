### Basic preperation stuff
import json
from Hamen import *
from hamenNoodle import *
from copy import deepcopy


# load bundles

# infodat
infoDat_addRequirement([
    "Noodle Extensions"
])

# add arrays for important stuff
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = []


#region ### do note scripts here
flipBug(0,9999)

### Save edited json and info dat
countUp()

export_infoDat()
export_diff()