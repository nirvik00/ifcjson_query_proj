import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


class beam_obj(object):
    def __init__(self, data):
        self.data = data
        self.num = 0
        self.simplified_data_arr = []  # array of all simple space objects
        #
        self.get_beams()  # run the functions
        #
        self.out = {"beams": self.simplified_data_arr}
        #

    def get_beams(self):
        a = parse("$..data[?(@.type=='Beam')]").find(self.data)
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
            out['object_type'] = parse("$.objectType").find(json2)[0].value
        except:
            pass
        try:
            out['contained_in_structure'] = parse(
                "$.containedInStructure").find(json2)[0].value
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
            out['beam_material'] = parse(
                "$.'Beam Material'").find(json2)[0].value
        except:
            pass
        try:
            out['Thickness'] = parse(
                "$.Thickness").find(json2)[0].value
        except:
            pass
        try:
            out['start_extension_calculation'] = parse(
                "$.'Start Extension Calculation'").find(json2)[0].value
        except:
            pass
        try:
            out['end_extension_calculation'] = parse(
                "$.'End Extension Calculation'").find(json2)[0].value
        except:
            pass
        try:
            out['cut_length'] = parse(
                "$.'Cut Length'").find(json2)[0].value
        except:
            pass
        try:
            out['d'] = parse("$.d").find(json2)[0].value
        except:
            pass
        try:
            out['k'] = parse("$.k").find(json2)[0].value
        except:
            pass
        try:
            out['kr'] = parse("$.kr").find(json2)[0].value
        except:
            pass
        try:
            out['tf'] = parse("$.tf").find(json2)[0].value
        except:
            pass
        try:
            out['tw'] = parse("$.tw").find(json2)[0].value
        except:
            pass
        try:
            out['W'] = parse("$.W").find(json2)[0].value
        except:
            pass
        try:
            out['A'] = parse("$.A").find(json2)[0].value
        except:
            pass
        #
        try:
            out['bf'] = parse("$.bf").find(json2)[0].value
        except:
            pass
        try:
            out['start_fx'] = parse("$.'Start Fx'").find(json2)[0].value
        except:
            pass
        try:
            out['start_fy'] = parse("$.'Start Fy'").find(json2)[0].value
        except:
            pass
        try:
            out['start_fz'] = parse("$.'Start Fz'").find(json2)[0].value
        except:
            pass
        try:
            out['start_mx'] = parse("$.'Start Mx'").find(json2)[0].value
        except:
            pass
        try:
            out['start_my'] = parse("$.'Start My'").find(json2)[0].value
        except:
            pass
        try:
            out['start_mz'] = parse("$.'Start Mz'").find(json2)[0].value
        except:
            pass
        try:
            out['end_fx'] = parse("$.'End Fx'").find(json2)[0].value
        except:
            pass
        try:
            out['end_fy'] = parse("$.'End Fy'").find(json2)[0].value
        except:
            pass
        try:
            out['end_fz'] = parse("$.'End Fz'").find(json2)[0].value
        except:
            pass
        try:
            out['end_mx'] = parse("$.'End Mx'").find(json2)[0].value
        except:
            pass
        try:
            out['end_my'] = parse("$.'End My'").find(json2)[0].value
        except:
            pass
        try:
            out['end_mz'] = parse("$.'End Mz'").find(json2)[0].value
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
