from class_sites import site_obj
from class_buildings import building_obj
from class_building_storeys import building_storey_obj
from class_spaces import space_obj
from class_walls import wall_obj
from class_slabs import slab_obj
from class_beams import beam_obj
from class_roofs import roof_obj
from class_doors import door_obj
from class_windows import window_obj


import json

building_elements = ["Site", "Building", "BuildingStorey",
                     "WallStandardCase", "Window", "Door", "Roof", "Beam", "Slab"]

XYZ = ["Stair", "StairFlight", "Railing",
       "FurnitureType", "FurnishingElement", ]


with open("ifcJsonData.json", "r") as json_file:
    data = json.load(json_file)
DATA = json.loads(str(json.dumps(data)))

res = {}
site = site_obj(DATA)
building = building_obj(DATA)
building_storeys = building_storey_obj(DATA)
spaces = space_obj(DATA)
walls = wall_obj(DATA)
doors = door_obj(DATA)
windows = window_obj(DATA)
slabs = slab_obj(DATA)
beams = beam_obj(DATA)
roofs = roof_obj(DATA)


res.update(site.out)
res.update(building.out)
res.update(building_storeys.out)
res.update(spaces.out)
res.update(walls.out)
res.update(doors.out)
res.update(windows.out)
res.update(slabs.out)
res.update(beams.out)
res.update(roofs.out)


with open('simplified_out.json', 'w') as outfile:
    json.dump(res, outfile, indent=2)
