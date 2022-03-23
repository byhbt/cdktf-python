from cdktf_cdktf_provider_aws import elb
from cdktf import TerraformVariable

def create_alb(self, subnets, target_group):
  aws_lb_app = elb.Lb(self, "app",
    load_balancer_type="application",
    name="centauri-alb",
    subnets=subnets.list_value
  )

  elb.LbListener(self, "app-lb-http-listener",
    default_action=[elb.LbListenerDefaultAction(
      type="forward",
      target_group_arn=target_group.arn
    )],
    load_balancer_arn=aws_lb_app.arn,
    port=80,
    protocol="HTTP",
    depends_on=[aws_lb_app]
  )

  return aws_lb_app

def create_target_group(self):
  vpc_id = TerraformVariable(self, 'vpc_id',
    type="string"
  )

  aws_lb_target_group_app = elb.LbTargetGroup(self, "app-lb-target-group",
    deregistration_delay="100",
    # health_check=[{
    #   "healthy_threshold": 2,
    #   "interval": 70,
    #   "matcher": "200",
    #   "path": "/",
    #   "port": 4000,
    #   "protocol": "HTTP",
    #   "timeout": 65,
    #   "unhealthy_threshold": 2
    # }],
    name="centauri-tg",
    port=4000,
    protocol="HTTP",
    target_type="ip",
    vpc_id=vpc_id.string_value
  )

  return aws_lb_target_group_app
