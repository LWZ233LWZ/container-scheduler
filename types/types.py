import time

NamespaceDefault = "default"
NamespaceAll = ''
NamespaceNone = ''
NamespaceSystem = "kube-system"
NamespacePublic = "kube-public"

EventTypeNormal = 'Normal'
EventTypeWarning = 'Warning'

class TypeMeta(object):
    def __init__(self):
        self.Kind = ''
        self.APIVersion = ''

class OwnerReference(object):
    def __init__(self):
        self.APIVersion = None
        self.Kind = None
        self.Name = None
        self.UID = None
        self.Controller = None
        self.BlockOwnerDeletion = None

class ObjectMeta(object):
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
    def __init__(self):
        self.Kind = ''
        self.Namespace = ''
        self.Name = ''
        self.UID = ''
        self.APIVersion = ''
        self.ResourceVersion = ''
        self.FieldPath = ''

class EventSource(object):
    def __init__(self):
        self.Component = ''
        self.Host = ''

class Event(TypeMeta,ObjectMeta):
    def __init__(self):
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

class TypeMeta(object):
    def __init__(self):
        self.Kind = ''
        self.APIVersion = ''

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


