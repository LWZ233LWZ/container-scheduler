import datetime
import schema
import os

NamespaceDefault = "default"
NamespaceAll = ''
NamespaceNone = ''
NamespaceSystem = "kube-system"
NamespacePublic = "kube-public"

EventTypeNormal = 'Normal'
EventTypeWarning = 'Warning'


class Time(object):
    patten = '%Y-%m-%dT%H:%M:%SZ'
    def __init__(self,obj):
        if isinstance(obj, datetime.datetime):
            self.time = obj
        elif isinstance(obj, str):
            self.time = datetime.datetime.strptime(obj,self.patten)
        else:
            self.time = None

    def __call__(self, *args, **kwargs):
        if len(args) != 1:
            return None
        if isinstance(args[0],datetime.datetime):
            return args[0].strftime(self.patten)
        elif isinstance(args[0],str):
            return datetime.datetime.strptime(args[0],self.patten)
        return None
    def __str__(self):
        if self.time == None:
            return ''
        else:
            return self.time.strftime(self.patten)

class TypeMeta(object):
    jsonMap = {
       'Kind' :             'name=kind,type=str,omitempty',
       'APIVersion':        'name=apiVersion,type=str,omitempty',
    }
    def __init__(self):
        self.Kind = None
        self.APIVersion = None

class OwnerReference(object):
    jsonMap = {
       'APIVersion':            'name=apiVersion,type=str',
       'Kind' :                 'name=kind,type=str',
       'Name':                  'name=name,type=str',
       'UID':                   'name=uid,type=str',
       'Controller':            'name=controller,type=bool',
       'BlockOwnerDeletion':    'name=blockOwnerDeletion,type=bool',
    }
    def __call__(self, *args, **kwargs):
        pass
    def __init__(self):
        self.APIVersion = None
        self.Kind = None
        self.Name = None
        self.UID = None
        self.Controller = None
        self.BlockOwnerDeletion = None

class ObjectMeta(object):
    jsonMap = {
        'name':                 'name=name,type=str,omitempty',
        'generateName':         'name=generateName,type=str,omitempty',
        'namespace':            'name=namespace,type=str,omitempty',
        'selfLink' :            'name=selfLink,type=str,omitempty',
        'uid':                  'name=uid,type=str,omitempty',
        'resourceVersion':      'name=resourceVersion,type=str,omitempty',
        'generation':           'name=generation,type=int,omitempty',
        'creationTimestamp':    'name=creationTimestamp,type=v1.Time,omitempty',
        'deletionTimestamp':    'name=deletionTimestamp,type=v1.Time,omitempty',
        'deletionGracePeriodSeconds': 'name=deletionGracePeriodSeconds,type=int,omitempty',
        'labels':               'name=labels,type=dict,omitempty',
        'annotations':          'name=annotations,type=list[str],omitempty',
        'ownerReferences':      'name=ownerReferences,type=list[v1.OwnerReference],emitempty',
        'finalizers':           'name=finalizers,type=list[str],emitempty',
        'clusterName':          'name=clusterName,type=str,emitempty'
    }

    def __init__(self):
        self.name = None
        self.generateName = None
        self.namespace = None
        self.selfLine = None
        self.uid = None
        self.resourceVersion = None
        self.generation = None
        self.creationTimestamp = None
        self.deletionTimestamp = None
        self.deletionGracePeriodSeconds = None
        self.labels = None
        self.annotations = None
        self.ownerReferences = None
        self.finalizers = None
        self.clusterName = None

class ObjectReference(object):
    jsonMap = {
        'kind':             'name=kind,type=str,omitempty',
        'namespace':        'name=namespace,type=str,omitempty',
        'name':             'name=name,type=str,omitempty',
        'uid':              'name=uid,type=str,omitempty',
        'apiVersion':       'name=apiVersion,type=str,omitempty',
        'resourceVersion':  'name=resourceVersion,type=str,omitempty',
        'fieldPath':        'name=fieldPath,type=str,omitempty',
    }
    def __init__(self):
        self.kind = None
        self.namespace = None
        self.name = None
        self.uid = None
        self.apiVersion = None
        self.resourceVersion = None
        self.fieldPath = None

class EventSource(object):
    jsonMap = {
        'component':            'name=component,type=str,omitempty',
        'host':                 'name=host,type=str,omitempty',
    }

    def __init__(self):
        self.component = None
        self.host = None

class Event(object):
    jsonMap = {
          'TypeMeta':           'action=inline,type=v1.TypeMeta,name=.',
          'objectMeta':         'name=metadata,type=v1.ObjectMeta',
          'involvedObject':     'name=involvedObject,type=v1.ObjectReference',
          'reason':             'name=reason,type=str,omitempty',
          'message':            'name=message,type=str,omitempty',
          'source':             'name=source,type=v1.EventSource,omitempty',
          'firstTimestamp':     'name=firstTimestamp,type=v1.Time,omitempty',
          'lastTimestamp':      'name=lastTimestamp,type=v1.Time,omitempty',
          'count':              'name=count,type=int,omitempty',
          'type':               'name=type,type=str,omitempty',
    }

    def __init__(self):
        self.TypeMeta = None
        self.objectMeta = None
        self.involvedObject = None
        self.reason = None
        self.message = None
        self.source = None
        self.firstTimestamp = None
        self.lastTimestamp = None
        self.count = None
        self.type = None

class Duration(object):
    def __init__(self):
        self.duration = float()
        self.LeaseDurationSeconds = int()
        self.AcquireTime = None
        self.RenewTime = None
        self.LeaderTransitions = int()

class LeaderElectionRecord(object):
    def __init__(self):
        self.HolderIdentity = ''
        self.LeaseDurationSeconds = int()
        self.AcquireTime = None
        self.RenewTime = None
        self.LeaderTransitions = int()
    

class LockInterface(object):
    def Get(self): pass
    def Create(self): pass

class LeaderElectionConfiguration(object):
    def __init__(self):
        self.LeaderElect = bool()
        self.LeaseDuration = Duration()
        self.RenewDeadline = Duration()
        self.RetryPeriod = Duration()

class KubeSchedulerConfiguration(TypeMeta):
    def __init__(self):
        super(self,KubeSchedulerConfiguration).__init__()
        self.Port = int()
        self.Address = ''
        self.AlgorithmProvider = ''
        self.PolicyConfigFile = ''
        self.EnableProfiling = bool()
        self.EnableContentionProfiling = bool()
        self.ContentType = str()
        self.KubeAPIQPS = float()
        self.KubeAPIBurst = float()
        self.SchedulerName = ''
        self.HardPodAffinitySymmetricWeight = int()
        self.FailureDomains = ''

if __name__ == '__main__':
    t = Time(datetime.datetime.now())
    print str(t)
    print hasattr(Event,'jsonMap')



