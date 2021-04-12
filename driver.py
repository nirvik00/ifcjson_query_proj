from mods.class_sites import site_obj
from mods.class_buildings import building_obj
from mods.class_building_storeys import building_storey_obj
from mods.class_spaces import space_obj
from mods.class_walls import wall_obj
from mods.class_slabs import slab_obj
from mods.class_beams import beam_obj
from mods.class_roofs import roof_obj
from mods.class_doors import door_obj
from mods.class_windows import window_obj
import json

from datetime import datetime

""" building_elements = ["Site", "Building", "BuildingStorey",
                     "WallStandardCase", "Window", "Door", "Roof", "Beam", "Slab"]
# NOT CONVERTED
XYZ = ["Stair", "StairFlight", "Railing",
       "FurnitureType", "FurnishingElement"] """


def test():
    out_file = "simplified_out.json"
    with open(out_file, "r") as f:
        res = json.load(f)
    return res


def test2():
    out_file = "simplified_out2.json"
    with open(out_file, "r") as f:
        res = json.load(f)
    return res


def run_driver_proc():
    inp_file = "ifcJsonData.json"
    #
    with open(inp_file, "r") as json_file:
        data = json.load(json_file)
    DATA = json.loads(str(json.dumps(data)))
    res = {}
    #
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
    #
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
    #
    out_file = "simplified_out2.json"
    with open(out_file, 'w') as outfile:
        json.dump(res, outfile, indent=2)
    #
    return res


""" test() """
""" #
datetime_0 = datetime.now()
#
run_driver_proc()
#
datetime_1 = datetime.now()
datetime_dt = datetime_1-datetime_0
print("time taken according to datetime: ", datetime_dt, " hh:mm:ss:ms")
 """
