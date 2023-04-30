import sys
import importlib

import bpy

# Add-on Metadata

bl_info = {
    "name": "SWTOR Area Assembler",
    "author": "ZeroGravitas & Crunch",
    "version": (1, 2, 0),
    "blender": (3, 1, 0),
    "category": "SWTOR",
    "location": "File > Import > SWTOR (Area .json)",
    "description": "Imports Jedipedia.net-exported SWTOR .DAT Files converted to .JSON Format",
    "doc_url": "",
    "tracker_url": "",
}

# Add-on modules loader: 
# Simplifies coding the loading of the modules to keeping a list of their names
# (See https://b3d.interplanety.org/en/creating-multifile-add-on-for-blender/ )
    
modulesNames = [
    'preferences',
    'area_import',
    ]
# Add an uber mats processor if the zg_swtor_tools addon
# isn't installed and activated.
# if not "process_uber_mats" in dir(bpy.ops.zgswtor):
#     modulesNames.append("process_uber_mats_plus")



modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)


def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()
 
if __name__ == "__main__":
    register()#
