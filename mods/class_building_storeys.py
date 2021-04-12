import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


class building_storey_obj(object):
    def __init__(self, data, get_obj=False):
        self.get_obj = get_obj
        self.data = data
        self.num = 0
        self.simplified_data_arr = []  # array of all simple space objects
        #
        self.get_building_storeys()  # run the functions
        #
        self.out = {"building_storeys": self.simplified_data_arr}
        #

    def get_building_storeys(self):
        a = parse("$..data[?(@.type=='BuildingStorey')]").find(self.data)
        for i in a:
            json2 = json.loads(json.dumps(i.value))
            out = self.repr_json(json2)
            self.simplified_data_arr.append(out)
            self.num += 1

    def repr_json(self, json2):
        out = {}
        try:
            out['name'] = parse("$.name").find(json2)[0].value
        except:
            pass
        try:
            out['globalId'] = parse("$.globalId").find(json2)[0].value
        except:
            pass
        try:
            out['elevation'] = parse("$.Elevation").find(json2)[0].value
        except:
            pass
        try:
            out['composition_type'] = parse(
                "$.compositionType").find(json2)[0].value
        except:
            pass
        # address data
        try:
            x = parse("$..containsElements[*]").find(json2)
            ele = []
            for i in x:
                ele.append(i.value)
            out['contains_elements'] = ele
        except:
            pass
        return out

    def display(self):
        print(json.dumps(self.out, indent=2))
        return self.out


""" with open("ifcJsonData.json", "r") as json_file:
    Data = json.load(json_file)

print(len(Data))
DATA = json.loads(str(json.dumps(Data)))
bldg = building_storey_obj(DATA)
print(json.dumps(bldg.out, indent=2)) """
