import json
from cdktf_cdktf_provider_aws import ecs
from cdktf import TerraformVariable


def create_ecs_cluster(self):
  cluster = ecs.EcsCluster(self, "centauri-cluster", name="Centauri")

  return cluster

def parse_container_definition(self, db_connection_str, alb_dns_name, log_group):
  container_name = TerraformVariable(self, 'container_name',
    type="string"
  )

  docker_image = TerraformVariable(self, 'docker_image',
    type="string"
  )

  secret_key_base = TerraformVariable(self, 'secret_key_base',
    type="string"
  )

  container_definitions = {
    'name': container_name.string_value,
    'image': docker_image.string_value,
    'essential': True,
    'portMappings': [
      {
        'containerPort': 4000,
        'hostPort': 4000
      }
    ],
    'environment': [
      {
        'name': 'DATABASE_URL',
        'value': db_connection_str
      },
      {
        'name': 'HOST',
        'value': alb_dns_name
      },
      {
        'name': 'SECRET_KEY_BASE',
        'value': secret_key_base.string_value
      },
      {
        'name': 'PORT',
        'value': '4000'
      }
    ],
    'logConfiguration': {
      'logDriver': 'awslogs',
      'options': {
        'awslogs-group': log_group.name,
        'awslogs-stream-prefix': 'ecsFargate',
        'awslogs-region': 'ap-southeast-1'
      }
    }
  }

  container_definition_json_content = "[{content}]".format(content=json.dumps(container_definitions))

  return container_definition_json_content

def create_task_definition(self, aws_iam_role_ecs_task_execution, db_connection_str, alb_dns_name, log_group):
  task_definition = ecs.EcsTaskDefinition(self, "centauri-task-def",
    container_definitions=parse_container_definition(self, db_connection_str, alb_dns_name, log_group),
    family="centauri-service-latest",
    requires_compatibilities=["FARGATE"],
    network_mode="awsvpc",
    cpu="256",
    memory="512",
    task_role_arn=aws_iam_role_ecs_task_execution.arn,
    execution_role_arn=aws_iam_role_ecs_task_execution.arn
  )

  return task_definition

def create_ecs_service(self, ecs_cluster, task_definition, security_group, subnets, target_group):
  ecs_service = ecs.EcsService(
      self, "centauri",
      cluster=ecs_cluster.id,
      deployment_maximum_percent=100,
      deployment_minimum_healthy_percent=0,
      desired_count=1,
      launch_type="FARGATE",
      name="centauri-service",
      scheduling_strategy="REPLICA",
      task_definition=task_definition.arn,
      network_configuration=ecs.EcsServiceNetworkConfiguration(
          subnets=subnets.list_value,
          security_groups=security_group.list_value,
          assign_public_ip=True
      ),
      load_balancer=[ecs.EcsServiceLoadBalancer(
        container_name="centauri-app",
        container_port=4000,
        target_group_arn=target_group.arn
      )]
  )

  return ecs_service
