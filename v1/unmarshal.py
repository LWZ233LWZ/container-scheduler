import json
import re
import v1.types as v1

classObj= {
    'v1.Event': lambda dict: construct_V1_Event(dict),
    'v1.TypeMeta': lambda  dict: construct_V1_TypeMeta(dict),
    'v1.ObjectMeta': lambda  dict: construct_V1_ObjectMeta(dict),
    'v1.ObjectReference': lambda dict: construct_V1_ObjectReference(dict),
    'v1.EventSource': lambda dict: construct_V1_EventSource(dict),
    'str': lambda i: str(i),
    'bool': lambda i: bool(i),
    'v1.Time': lambda i: v1.Time(i),
    'list': lambda list,ty : filter(lambda x: classObj[ty](x) , list),
    'int': lambda i: int(i),
}

def construct_V1_EventSource(dict):
    e = v1.ObjectReference()
    jsonMap = e.jsonMap
    for (outerName,rawValue) in jsonMap.items():
        marks = parseTag(rawValue)
        if marks == None:
            return None, 'Tag Error: please Check'
        for (name,value) in marks.items():
            if name == '.':
                setattr(e, outerName, classObj['v1.' + outerName](dict))
            else:
                if 'list' in value:
                    listtype = value[5:len(value) - 1]
                    setattr(e, outerName, classObj['list'](dict, listtype))
                else:
                    setattr(e, outerName, classObj[value](dict))
    return e

def construct_V1_ObjectReference(dict):
    e = v1.ObjectReference()
    jsonMap = e.jsonMap
    for (outerName,rawValue) in jsonMap.items():
        marks = parseTag(rawValue)
        if marks == None:
            return None, 'Tag Error: please Check'
        for (name,value) in marks.items():
            if name == '.':
                setattr(e, outerName, classObj['v1.' + outerName](dict))
            else:
                if 'list' in value:
                    listtype = value[5:len(value) - 1]
                    setattr(e, outerName, classObj['list'](dict, listtype))
                else:
                    setattr(e, outerName, classObj[value](dict))
    return e

def construct_V1_ObjectMeta(dict):
    e = v1.ObjectMeta()
    jsonMap = e.jsonMap
    for (outerName,rawValue) in jsonMap.items():
        marks = parseTag(rawValue)
        if marks == None:
            return None, 'Tag Error: please Check'
        for (name,value) in marks.items():
            if name == '.':
                setattr(e, outerName, classObj['v1.' + outerName](dict))
            else:
                if 'list' in value:
                    listtype = value[5:len(value) - 1]
                    setattr(e, outerName, classObj['list'](dict, listtype))
                else:
                    setattr(e, outerName, classObj[value](dict))
    return e

def construct_V1_TypeMeta(dict):
    e = v1.TypeMeta()
    jsonMap = e.jsonMap
    for (outerName,rawValue) in jsonMap.items():
        marks = parseTag(rawValue)
        if marks == None:
            return None, 'Tag Error: please Check'
        for (name,value) in marks.items():
            if name == '.':
                setattr(e, outerName, classObj['v1.'+outerName](dict))
            else:
                if 'list' in value:
                    listtype = value[5:len(value)-1]
                    setattr(e,outerName,classObj['list'](dict,listtype))
                else:
                    setattr(e,outerName, classObj[value](dict))
    return e

def construct_V1_Event(dict):
    e = v1.Event()
    jsonMap = e.jsonMap
    for (outerName,rawValue) in jsonMap.items():
        print rawValue
        marks = parseTag(rawValue)
        print marks
        if marks == None:
            return None, 'Tag Error: please Check'
        for (name,value) in marks.items():
            if name == '.':
                setattr(e, outerName, classObj['v1.'+outerName](dict[outerName]))
            else:
                if 'omitempty' == name:
                    continue
                if 'list' in value:
                    listtype = value[5:len(value) - 1]
                    setattr(e, outerName, classObj['list'](dict[outerName], listtype))
                else:
                    print dict[outerName]
                    print dict
                    setattr(e, outerName, classObj[value](dict[outerName]))
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
    print v1Obj
    apiVersion = v1Obj['apiVersion']
    kind = v1Obj['kind']
    solidObj = classObj[apiVersion + '.' +kind](v1Obj)
    print solidObj

if __name__ == '__main__':
    v1Obj = {'a':1,'b':2}
    v1Obj.has_key()
    if hasattr(v1Obj, 'a'):
        print True