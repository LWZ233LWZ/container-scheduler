import time
import schema

NamespaceDefault = "default"
NamespaceAll = ''
NamespaceNone = ''
NamespaceSystem = "kube-system"
NamespacePublic = "kube-public"

EventTypeNormal = 'Normal'
EventTypeWarning = 'Warning'

def marshal(func):
    pass

def unmarshal(func):
    pass

@unmarshal
@marshal
class TypeMeta(object):
    jsonMap = {
        'Kind' : 'json:"kind,omitempty" protobuf:"bytes,1,opt,name=kind"',
        'APIVersion': 'json:"apiVersion,omitempty" protobuf:"bytes,2,opt,name=apiVersion"',
    }
    def __init__(self):
        self.Kind = ''
        self.APIVersion = ''

@marshal
@unmarshal
class OwnerReference(object):
    jsonMap = {
        'APIVersion': 'json:"apiVersion" protobuf:"bytes,5,opt,name=apiVersion"',
        'Kind' : 'json:"kind" protobuf:"bytes,1,opt,name=kind"',
        'Name': 'json:"name" protobuf:"bytes,3,opt,name=name"',
        'UID': 'json:"uid" protobuf:"bytes,4,opt,name=uid"',
        'Controller':'json:"controller,omitempty" protobuf:"varint,6,opt,name=controller',
        'BlockOwnerDeletion': 'json:"blockOwnerDeletion,omitempty" protobuf:"varint,7,opt,name=blockOwnerDeletion"',
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

@marshal
@unmarshal
class ObjectMeta(object):
    jsonMap = {
        'Name': 'json:"name,omitempty" protobuf:"bytes,1,opt,name=name"',
        'GenerateName': 'json:"generateName,omitempty" protobuf:"bytes,2,opt,name=generateName"',
        'Namespace': 'json:"namespace,omitempty" protobuf:"bytes,3,opt,name=namespace"',
        'SelfLink' : 'json:"selfLink,omitempty" protobuf:"bytes,4,opt,name=selfLink"',
        'UID':      'json:"uid,omitempty" protobuf:"bytes,5,opt,name=uid,casttype=k8s.io/kubernetes/pkg/types.UID"',
        'ResourceVersion': 'json:"resourceVersion,omitempty" protobuf:"bytes,6,opt,name=resourceVersion"',
        'Generation': 'json:"generation,omitempty" protobuf:"varint,7,opt,name=generation"',
        'CreationTimestamp': 'json:"creationTimestamp,omitempty" protobuf:"bytes,8,opt,name=creationTimestamp"',
        'DeletionTimestamp':  'json:"deletionTimestamp,omitempty" protobuf:"bytes,9,opt,name=deletionTimestamp"',
        'DeletionGracePeriodSeconds': 'json:"deletionGracePeriodSeconds,omitempty" protobuf:"varint,10,opt,name=deletionGracePeriodSeconds"',
        'Labels': 'json:"labels,omitempty" protobuf:"bytes,11,rep,name=labels"',
        'Annotations': 'json:"annotations,omitempty" protobuf:"bytes,12,rep,name=annotations"',
        'OwnerReferences': 'json:"ownerReferences,omitempty" patchStrategy:"merge" patchMergeKey:"uid" protobuf:"bytes,13,rep,name=ownerReferences"',
        'Finalizers': 'json:"finalizers,omitempty" patchStrategy:"merge" protobuf:"bytes,14,rep,name=finalizers"',
        'ClusterName': 'json:"clusterName,omitempty" protobuf:"bytes,15,opt,name=clusterName"'
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
        'Kind': 'json:"kind,omitempty" protobuf:"bytes,1,opt,name=kind"',
        'Namespace': 'json:"namespace,omitempty" protobuf:"bytes,2,opt,name=namespace"',
        'Name': 'json:"name,omitempty" protobuf:"bytes,3,opt,name=name"',
        'UID': 'json:"uid,omitempty" protobuf:"bytes,4,opt,name=uid,casttype=k8s.io/apimachinery/pkg/types.UID"',
        'APIVersion': 'json:"apiVersion,omitempty" protobuf:"bytes,5,opt,name=apiVersion"',
        'ResourceVersion': 'json:"resourceVersion,omitempty" protobuf:"bytes,6,opt,name=resourceVersion"',
        'FieldPath': 'json:"fieldPath,omitempty" protobuf:"bytes,7,opt,name=fieldPath"',
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
       'Component': 'json:"component,omitempty" protobuf:"bytes,1,opt,name=component"',
        'Host': 'json:"host,omitempty" protobuf:"bytes,2,opt,name=host"',
    }

    def __init__(self):
        self.Component = ''
        self.Host = ''

class Event(TypeMeta,ObjectMeta):
    jsonMap = {
        'TypeMeta': 'json:",inline"',
        'ObjectMeta': 'json:"metadata" protobuf:"bytes,1,opt,name=metadata"',
        'InvolvedObject': 'json:"involvedObject" protobuf:"bytes,2,opt,name=involvedObject"',
        'Reason': 'json:"reason,omitempty" protobuf:"bytes,3,opt,name=reason"',
        'Message': 'json:"message,omitempty" protobuf:"bytes,4,opt,name=message"',
        'Source': 'json:"source,omitempty" protobuf:"bytes,5,opt,name=source"',
        'FirstTimestamp': '`json:"firstTimestamp,omitempty" protobuf:"bytes,6,opt,name=firstTimestamp"`',
        'LastTimestamp': 'json:"lastTimestamp,omitempty" protobuf:"bytes,7,opt,name=lastTimestamp"',
        'Count': 'json:"count,omitempty" protobuf:"varint,8,opt,name=count"',
        'Type': 'json:"type,omitempty" protobuf:"bytes,9,opt,name=type"',
    }

    def __init__(self):
        super.__init__(self,TypeMeta).__init__()
        super.__init__(self.ObjectMeta).__init__()

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
    e = Event()
    print e.jsonMap


