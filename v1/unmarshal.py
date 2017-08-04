import json
import v1.types as v1

classObj= {
    'v1/Event': lambda dict: construct_V1_Event(dict),
    'v1/TypeMeta': lambda  dict: construct_V1_TypeMeta(dict),
    'v1/ObjectMeta': lambda  dict: construct_V1_ObjectMeta(dict),
    'v1/ObjectReference': lambda dict: construct_V1_ObjectReference(dict),
    'v1/EventSource': lambda dict: construct_V1_EventSource(dict),
}

def construct_V1_EventSource(dict):
    pass

def construct_V1_ObjectReference(dict):
    pass
def construct_V1_ObjectMeta(dict):
    pass
def construct_V1_TypeMeta(dict):
    pass

def construct_V1_Event(dict):
    e = v1.Event()
    jsonMap = e.jsonMap
    for k,v in jsonMap:
        marks = parseTag(v)
        if marks == None:
            return None, 'Tag Error: please Check'

def genDataMemberByTag():
    pass

def parseTag(tag):
    marks = str.split(tag, ',')
    res = {}
    for m in marks:
        if '=' in m:
            r1,r2 = m.split('=')
            res[r1] = r2
        if 'omitempty' in m:
            res['omitempty']= True
    keys = res.keys()
    if 'type' not in keys:
        return None
    if 'name' not in keys:
        return None
    if 'omitempty' not in keys:
        res['omitempty'] = False

def unmarshal(obj):
    if not isinstance(obj,str):
        return None
    # print obj
    v1Obj = json.loads(obj,strict=False)
    if not isinstance(v1Obj,dict):
        return None
    if not v1Obj.has_key('apiVersion') and v1Obj.has_key('kind'):
        return None
    print v1Obj
    apiVersion = v1Obj['apiVersion']
    kind = v1Obj['kind']
    solidObj = classObj[apiVersion + '/' +kind]()
    print solidObj.__dict__

if __name__ == '__main__':
    v1Obj = {'a':1,'b':2}
    v1Obj.has_key()
    if hasattr(v1Obj, 'a'):
        print True