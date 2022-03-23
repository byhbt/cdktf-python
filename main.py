#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformVariable, TerraformStack, TerraformOutput, RemoteBackend, NamedRemoteWorkspace
from cdktf_cdktf_provider_aws import AwsProvider, cloudwatch
from cdktf_cdktf_provider_random import RandomProvider
from nimble.ecs import create_ecs_cluster, create_task_definition, create_ecs_service
from nimble.iam import create_task_role
from nimble.rds import create_rds, create_connection_str
from nimble.alb import create_alb, create_target_group
from nimble.log import create_log_group

class MyStack(TerraformStack):
  def __init__(self, scope: Construct, ns: str):
    super().__init__(scope, ns)

    region = TerraformVariable(self, 'region',
      type="string",
      description="Region to deploy to",
      default="ap-southeast-1"
    )

    subnets = TerraformVariable(self, 'subnets',
      type="list(string)"
    )

    security_group = TerraformVariable(self, 'security_group',
      type="list(string)"
    )

    # Provider
    AwsProvider(self, "AWS", region=region.string_value)

    # Init RDS
    rds = create_rds(self)
    db_connection_str = create_connection_str(rds)

    # Init RDS
    ecs_cluster = create_ecs_cluster(self)
    aws_iam_role_ecs_task_execution = create_task_role(self)

    target_group = create_target_group(self)
    alb = create_alb(self, subnets, target_group)

    # Init Log group
    log_group = create_log_group(self)

    task_definition = create_task_definition(self,
                                    aws_iam_role_ecs_task_execution,
                                    db_connection_str,
                                    alb.dns_name,
                                    log_group)

    ecs_service = create_ecs_service(self,
                                    ecs_cluster,
                                    task_definition,
                                    security_group,
                                    subnets,
                                    target_group)

    TerraformOutput(self, "alb_target_group_arn",
      value=alb.dns_name
    )

app = App()
stack = MyStack(app, "cdktf")

RemoteBackend(stack,
  hostname='app.terraform.io',
  organization='byhbt',
  workspaces=NamedRemoteWorkspace('python')
)

app.synth()
