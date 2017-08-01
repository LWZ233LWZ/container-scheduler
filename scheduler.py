import os
import argparse
import logging
import factory.plugins as plugins

DefaultHardPodAffinitySymmetricWeight = 1
DefaultFailureDomains = ','.join(["kubernetes.io/hostname",
                                  "failure-domain.beta.kubernetes.io/zone",
                                  "failure-domain.beta.kubernetes.io/region"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port',type=int,
                        help="The port that the scheduler's http service runs on")
    parser.add_argument('--address', type=str,
                        help="The IP address to serve on (set to 0.0.0.0 for all interfaces)")
    parser.add_argument('--algorithm_provider',type=str,
                        help="The scheduling algorithm "
                             "provider to use, one of: " + plugins.ListAlgorithmProviders())
    parser.add_argument('--policy_config_file',
                        type=str,
                        help="File with scheduler policy configuration")
    parser.add_argument('--profiling',default=True,
                        type=bool,
                        help="Enable profiling via web interface host:port/debug/pprof/")
    parser.add_argument('--contention_profiling',default=False,
                        help="Enable lock contention profiling, if profiling is enabled")
    parser.add_argument('--master',type=str,
                        help="The address of the Kubernetes API server (overrides any value in kubeconfig)")
    parser.add_argument('--kube_api_content-type',type=str,
                        help="Content type of requests sent to apiserver.")
    parser.add_argument('--kube_api_qps',type=float,
                        help="QPS to use while talking with kubernetes apiserver")
    parser.add_argument('--kube_api_burst',type=float,
                        help="Burst to use while talking with kubernetes apiserver")
    parser.add_argument("--scheduler_name",type=str,
                        help="Name of the scheduler, used to select which pods will be processed by this "
                             "scheduler, based on pod's \"spec.SchedulerName\".")
    parser.add_argument('--hard_pod_affinity_symmetric_weight',type=int,
                        default=DefaultHardPodAffinitySymmetricWeight,
                        help="RequiredDuringScheduling affinity is not symmetric, but there is an implicit PreferredDuringScheduling affinity rule corresponding "+
			"to every RequiredDuringScheduling affinity rule. --hard-pod-affinity-symmetric-weight represents the weight of implicit PreferredDuringScheduling affinity rule.")
    parser.add_argument('--failure_domains',default=DefaultFailureDomains,
                        help="Indicate the \"all topologies\" set for an empty "
                             "topologyKey when it's used for PreferredDuringScheduling pod anti-affinity.")
    parser.add_argument("--failure_domains", help="Doesn't have any effect. Will be removed in future version.")
    args = parser.parse_args()
