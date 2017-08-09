import json
import re
import v1.types as v1

classObj= {
    'v1.Event': lambda dict: construct_V1_Event(dict),
    'v1.TypeMeta': lambda  dict: construct_V1_TypeMeta(dict),
    'v1.ObjectMeta': lambda  dict: construct_V1_ObjectMeta(dict),
    'v1.ObjectReference': lambda dict: construct_V1_ObjectReference(dict),
    'v1.OwnerReference' : lambda  dict : construct_V1_OwnerReference(dict),
    'v1.EventSource': lambda dict: construct_V1_EventSource(dict),
    'str': lambda i: str(i),
    'bool': lambda i: bool(i),
    'v1.Time': lambda i: v1.Time(i),
    'list': lambda list,ty : filter(lambda x: classObj[ty](x) , list),
    'int': lambda i: int(i),
}

def construct_V1_EventSource(dict):
    e = v1.EventSource()
    for key in e.jsonMap.keys():
        if dict.has_key(key):
            setattr(e, key, dict[key])

    return e

def construct_V1_ObjectReference(dict):
    e = v1.ObjectReference()
    for key in e.jsonMap.keys():
        if dict.has_key(key):
            setattr(e, key, dict[key])

    return e

def construct_V1_OwnerReference(dict):
    e = v1.ObjectReference()
    jsonMap = e.jsonMap
    for (outerName, rawValue) in jsonMap.items():
        marks = parseTag(rawValue)
        if marks == None:
            return None, 'Tag Error: please Check'
        types = marks['type']
        isList = False
        listType = None
        if 'list' in types:
            isList = True
            listType = types[5:len(types) - 1]
        names = marks['name']
        action = None if not marks.has_key('action') else marks['action']
        if action == 'inline':
            tmp = classObj[types](dict)
            setattr(e, names, tmp)
            continue
        if isList:
            tmp = classObj['list'](dict[names], listType)
            setattr(e, names, tmp)
            continue
        if types in classObj.keys() and dict.has_key(names):
            tmp = classObj[types](dict[names])
            setattr(e, names, tmp)
            continue
    return e

def construct_V1_ObjectMeta(dict):
    e = v1.ObjectMeta()
    jsonMap = e.jsonMap
    for (outerName, rawValue) in jsonMap.items():
        marks = parseTag(rawValue)
        if marks == None:
            return None, 'Tag Error: please Check'
        types = marks['type']
        isList = False
        listType = None
        if 'list' in types:
            isList = True
            listType = types[5:len(types) - 1]
        names = marks['name']
        action = None if not marks.has_key('action') else marks['action']
        if action == 'inline':
            tmp = classObj[types](dict)
            setattr(e, names, tmp)
            continue
        if isList and dict.has_key(names):
            tmp = classObj['list'](dict[names], listType)
            setattr(e, names, tmp)
            continue
        if types in classObj.keys() and dict.has_key(names):
            tmp = classObj[types](dict[names])
            setattr(e, outerName, tmp)
            continue

    return e

def construct_V1_TypeMeta(dict):
    e = v1.TypeMeta()
    for key in e.jsonMap.keys():
        if dict.has_key(key):
            setattr(e, key, dict[key])

    return e

def construct_V1_Event(dict):
    e = v1.Event()
    jsonMap = e.jsonMap
    for (outerName,rawValue) in jsonMap.items():
        marks = parseTag(rawValue)
        if marks == None:
            return None, 'Tag Error: please Check'
        types = marks['type']
        isList = False
        listType = None
        if 'list' in types:
            isList = True
            listType = types[5:len(types)-1]
        names = marks['name']
        action = None if not marks.has_key('action') else marks['action']
        if action == 'inline':
            tmp = classObj[types](dict)
            setattr(e, names , tmp )
            continue
        if isList:
            tmp = classObj['list'](dict[names], listType)
            setattr(e, names, tmp)
            continue
        if types in classObj.keys() and dict.has_key(names):
            tmp = classObj[types](dict[names])
            setattr(e, outerName, tmp)
            continue

    print e.message
    print e.objectMeta.name
    return e

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
    return res

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def unmarshal(obj):
    if not isinstance(obj,str):
        return None
    v1Obj = json.loads(obj,strict=False,object_hook=_byteify)
    if not isinstance(v1Obj,dict):
        return None
    if not v1Obj.has_key('apiVersion') and v1Obj.has_key('kind'):
        return None
    apiVersion = v1Obj['apiVersion']
    kind = v1Obj['kind']
    solidObj = classObj[apiVersion + '.' +kind](v1Obj)

if __name__ == '__main__':
    v1Obj = {'a':1,'b':2}
    v1Obj.has_key()
    if hasattr(v1Obj, 'a'):
        print True