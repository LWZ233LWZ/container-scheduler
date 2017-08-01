import time

class Duration(object):
    def __init__(self):
        self.duration = float()

class LeaderElectionConfiguration(object):
    def __init__(self):
        self.LeaderElect = bool()
        self.LeaseDuration = Duration()
        self.RenewDeadline = Duration()
        self.
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

