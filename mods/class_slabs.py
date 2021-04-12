import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


class slab_obj(object):
    def __init__(self, data, get_obj = False):
        self.get_obj = get_obj
        self.data = data
        self.num = 0
        self.simplified_data_arr = []  # array of all simple space objects
        #
        self.get_slabs()  # run the functions
        #
        self.out = {"slabs": self.simplified_data_arr}
        #

    def get_slabs(self):
        a = parse("$..data[?(@.type=='Slab')]").find(self.data)
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
            out['level'] = parse("$.Level").find(json2)[0].value
        except:
            pass
        try:
            out['predefined_type'] = parse(
                "$.predefinedType").find(json2)[0].value
        except:
            pass
        try:
            out['load_bearing'] = parse("$.LoadBearing").find(json2)[0].value
        except:
            pass
        try:
            out['area'] = parse("$.Area").find(json2)[0].value
        except:
            pass
        try:
            out['volume'] = parse("$.Volume").find(json2)[0].value
        except:
            pass
        try:
            out['Thickness'] = parse(
                "$.Thickness").find(json2)[0].value
        except:
            pass
        #
        # openings
        try:
            a_ope = parse("$..hasOpenings.ref").find(json2)
            openings_arr = []
            for i in a_ope:
                openings_arr.append(i.value)
            out['openings'] = openings_arr
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
            if(self.get_obj):
                x = parse("$..representations").find(json2)
                out['shape_representation_ref_obj'] = x[0].value[0]['ref']
                s = "$..data[?(@.type=='shapeRepresentation' " + \
                    "& @.globalId == '"+str(x[0].value[0]['ref'])+"')]"
                a_obj = parse(s).find(self.data)[0].value["items"][0]
                #
                out['OBJ'] = a_obj
            else:
                out['OBJ'] = "suppressed"

        except:
            pass
        return out

    def display(self):
        print(json.dumps(self.out, indent=2))
        return self.out
