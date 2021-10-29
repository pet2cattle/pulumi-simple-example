import pulumi
from pulumi_kubernetes.core.v1 import Namespace

config = pulumi.Config()
demoNS = Namespace("test1",
                    metadata={
                        "name": "test1"
                        })

pulumi.export("demoNS", demoNS.metadata.apply(lambda m: m.name))