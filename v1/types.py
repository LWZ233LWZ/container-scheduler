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
        self.Kind = ''
        self.APIVersion = ''

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
        'Name':                 'name=name,type=str,omitempty',
        'GenerateName':         'name=generateName,type=str,omitempty',
        'Namespace':            'name=namespace,type=str,omitempty',
        'SelfLink' :            'name=selfLink,type=str,omitempty',
        'UID':                  'name=selfLine,type=str,omitempty',
        'ResourceVersion':      'name=resourceVersion,type=str,omitempty',
        'Generation':           'name=generation,type=int,omitempty',
        'CreationTimestamp':    'name=creationTimestamp,type=Time,omitempty',
        'DeletionTimestamp':    'name=deletionTimestamp,type=Time,omitempty',
        'DeletionGracePeriodSeconds': 'name=deletionGracePeriodSeconds,type=int,omitempty',
        'Labels':               'name=labels,type=dict,omitempty',
        'Annotations':          'name=annotations,type=list,omitempty',
        'OwnerReferences':      'name=ownerReferences,type=list,emitempty',
        'Finalizers':           'name=finalizers,type=list,emitempty',
        'ClusterName':          'name=clusterName,type=str,emitempty'
    }

    def __init__(self):
        self.Name = ''
        self.GenerateName = ''
        self.Namespace = ''
        self.SelfLine = ''
        self.UID = ''
        self.ResourceVersion = ''
        self.Generation = ''
        self.CreationTimestamp = None
        self.DeletionTimestamp = None
        self.DeletionGracePeriodSeconds = None
        self.Labels = None
        self.Annotations = {}
        self.OwnerReferences = []
        self.Finalizers = []
        self.ClusterName = ''

class ObjectReference(object):
    jsonMap = {
        'Kind':             'name=kind,type=str,omitempty',
        'Namespace':        'name=namespace,type=str,omitempty',
        'Name':             'name=name,type=str,omitempty',
        'UID':              'name=uid,type=str,omitempty',
        'APIVersion':       'name=apiVersion,type=str,omitempty',
        'ResourceVersion':  'name=resourceVersion,type=str,omitempty',
        'FieldPath':        'name=fieldPath,type=str,omitempty',
    }
    def __init__(self):
        self.Kind = ''
        self.Namespace = ''
        self.Name = ''
        self.UID = ''
        self.APIVersion = ''
        self.ResourceVersion = ''
        self.FieldPath = ''

class EventSource(object):
    jsonMap = {
        'Component':            'name=component,type=str,omitempty',
        'Host':                 'name=host,type=str,omitempty',
    }

    def __init__(self):
        self.Component = ''
        self.Host = ''

class Event(object):
    jsonMap = {
          'TypeMeta':           'action=inline,type=TypeMeta,name=.',
          'ObjectMeta':         'name=metadata,type=ObjectMeta',
          'InvolvedObject':     'name=involvedObject,type=ObjectReference,',
          'Reason':             'name=reason,type=str,omitempty',
          'Message':            'name=message,type=str,omitempty',
          'Source':             'name=source,type=EventSource,omitempty',
          'FirstTimestamp':     'name=firstTimestamp,type=Time,omitempty',
          'LastTimestamp':      'name=lastTimestamp,type=Time,omitempty',
          'Count':              'name=count,type=int,omitempty',
          'Type':               'name=type,type=str,omitempty',
    }

    def __init__(self):
        self.TypeMeta = TypeMeta()
        self.ObjectMeta = ObjectMeta()
        self.InvolvedObject = ObjectReference()
        self.Reason = ''
        self.Message = ''
        self.Source = EventSource()
        self.FirstTimestamp = None
        self.LastTimestamp = None
        self.Count = int()
        self.Type = ''

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



