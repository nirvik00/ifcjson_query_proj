import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


class site_obj(object):
    def __init__(self, data):
        self.data = data
        self.num = 0
        self.simplified_data_arr = []  # array of all simple space objects
        #
        self.get_sites()  # run the functions
        #
        self.out = {"sites": self.simplified_data_arr}
        #

    def get_sites(self):
        a = parse("$..data[?(@.type=='Site')]").find(self.data)
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
            out['ref_latitude'] = parse("$.refLatitude").find(json2)[0].value
        except:
            pass
        try:
            out['ref_longitude'] = parse(
                "$.refLongitude").find(json2)[0].value
        except:
            pass
        #
        # materials
        try:
            mat = parse("$..materialLayers").find(json2)
            matr = []
            for i in mat:
                for j in i.value:
                    # print(j['material']['name'], j['layerThickness'])
                    matr.append({j['material']['name']: j['layerThickness']})

            out['material'] = matr
        except:
            pass
        #
        # obj data
        try:
            x = parse("$..representations").find(json2)
            out['shape_representation_ref_obj'] = x[0].value[0]['ref']
            s = "$..data[?(@.type=='shapeRepresentation' " + \
                "& @.globalId == '"+str(x[0].value[0]['ref'])+"')]"
            a_obj = parse(s).find(self.data)[0].value["items"][0]
            #
            out['OBJ'] = a_obj
        except:
            pass
        return out

    def display(self):
        print(json.dumps(self.out, indent=2))
        return self.out
