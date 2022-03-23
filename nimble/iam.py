from cdktf_cdktf_provider_aws import iam

def create_task_role(self):
  data_aws_iam_policy_document_ecs_task_execution = iam.DataAwsIamPolicyDocument(self, "ecs_task_execution",
    statement=[
      {
        "actions": ["sts:AssumeRole"],
        "principals": [
          {
            "identifiers": ["ecs-tasks.amazonaws.com"],
            "type": "Service"
          }
        ]
      }
    ]
  )

  aws_iam_role_ecs_task_execution = iam.IamRole(self, "ecs_task_execution_2",
    assume_role_policy=data_aws_iam_policy_document_ecs_task_execution.json,
    name="ecs_task_execution",
    path="/"
  )

  iam.IamRolePolicyAttachment(self, "ecs-task-execution-role-policy-attachment",
    policy_arn="arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy",
    role=aws_iam_role_ecs_task_execution.name
  )

  return aws_iam_role_ecs_task_execution
