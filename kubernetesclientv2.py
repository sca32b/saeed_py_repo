from kubernetes import client, config

config.load_kube_config()
clientv1 = client.CoreV1Api()

print("Listing deployment details:")
ret = clientv1.list_pod_for_all_namespaces(watch=False)
print(ret)

pod_manifest = {
    "apiVersion":"v1",
    "kind":"Pod",
    "metadata":{
        "name":"nginx",
        "labels":{
            "app":"nginx"
        }
    },
    "spec":{
        "containers":[
            {
                "name":"nginx",
                "image":"nginx",
                "ports":[
                    {
                        "containerPort":80
                    }
                ]
            }
        ]
    }
}
#resp = clientv1.create_namespaced_pod(body=pod_manifest, namespace="default")
#print(resp)
#delete the pod
resp = clientv1.delete_namespaced_pod(name="nginx",namespace="default")
print(resp)