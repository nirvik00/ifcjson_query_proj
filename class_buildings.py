import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


class building_obj(object):
    def __init__(self, data):
        self.data = data
        self.num = 0
        self.simplified_data_arr = []  # array of all simple space objects
        #
        self.get_buildings()  # run the functions
        #
        self.out = {"buildings": self.simplified_data_arr}
        #

    def get_buildings(self):
        a = parse("$..data[?(@.type=='Building')]").find(self.data)
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
            out['client_name'] = parse(
                "$.'Client Name'").find(json2)[0].value
        except:
            pass
        try:
            out['project_issue_date'] = parse(
                "$.'Project Issue Date'").find(json2)[0].value
        except:
            pass
        try:
            out['project_status'] = parse(
                "$.'Project Status'").find(json2)[0].value
        except:
            pass
        try:
            out['project_address'] = parse(
                "$.'Project Address'").find(json2)[0].value
        except:
            pass
        try:
            out['project_name'] = parse(
                "$.'Project Name'").find(json2)[0].value
        except:
            pass
        try:
            out['project_number'] = parse(
                "$.'Project Number'").find(json2)[0].value
        except:
            pass
        try:
            out['category_description'] = parse(
                "$.'Category Description'").find(json2)[0].value
        except:
            pass
        try:
            out['number_of_Storeys'] = parse(
                "$.NumberOfStoreys").find(json2)[0].value
        except:
            pass
        #
        # address data
        try:
            x = parse("$..buildingAddress[*]").find(json2)[0].value
            a = x['type']
            b = x['addressLines']
            c = x['town']
            d = x['country']

            #
            out['building_address'] = a
            out['address_lines'] = b
            out['city'] = c
            out['state'] = d

        except:
            pass
        return out

    def display(self):
        print(json.dumps(self.out, indent=2))
        return self.out


""" 
with open("ifcJsonData.json", "r") as json_file:
    Data = json.load(json_file)

print(len(Data))
DATA = json.loads(str(json.dumps(Data)))
bldg = building_obj(DATA)
print(json.dumps(bldg.out, indent=2)) """
