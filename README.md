## Up and running

First, you need to setup the necessary environment variables on Terraform cloud.

![image](https://user-images.githubusercontent.com/948856/159622273-4e8ffcaa-dbb5-45cb-be0f-1f2db6b0c8cc.png)

Then install `pipenv` as package management, for installing the dependencies:

```sh
pipenv install
```

Run `synth` command to verify if the source code is ready.

```sh
cdktf synth
```

Start deploy the infrastructure

```sh
cdktf deploy --auto-approve
```

Clean up command if no longer in use.

```sh
cdktf destroy --auto-approve
```

## CDKTF Library Reference

From the CLI:

```
pipenv shell

import cdktf_cdktf_provider_aws

help(cdktf_cdktf_provider_aws.AwsProvider)

help(cdktf_cdktf_provider_aws.ecs)
```

From the Constructs website:

https://constructs.dev/packages/@cdktf/provider-aws/v/5.0.48/api/EcsCluster?lang=python&submodule=ecs

## Tutorials

- Getting Started With CDK for Terraform and Python: https://www.youtube.com/watch?v=Ee2qh-pEC5k
- Unboxing the CDK to Terraform output format: https://www.youtube.com/watch?v=9s_BAyQIAhs
  - https://github.com/adamjkeller/ContainersFromTheCouch-terraform-cdk-example
- https://github.com/hashicorp/terraform-cdk/blob/main/docs/getting-started/python.md
- `tfcdk` Deep Dive: https://www.youtube.com/watch?v=nNr8JrN-9HE
- AWS CDK: https://www.youtube.com/watch?v=NkI5yeMFRK8

Python self: https://www.programiz.com/article/python-self-why

## Common errors

### Missing the ENV variables for AWS Authentication

```bash
╷
│ Error: error configuring Terraform AWS Provider: no valid credential sources for Terraform AWS Provider found.
│
│ Please see https://registry.terraform.io/providers/hashicorp/aws
│ for more information about providing credentials.
│
│ Error: NoCredentialProviders: no valid providers in chain
│ caused by: EnvAccessKeyNotFound: failed to find credentials in the environment.
│ SharedCredsLoad: failed to load profile, .
│ EC2RoleRequestError: no EC2 instance role found
│ caused by: RequestError: send request failed
│ caused by: Get "http://169.254.169.254/latest/meta-data/iam/security-credentials/": dial tcp 169.254.169.254:80: connect: no route to host
│
│
│   with provider["registry.terraform.io/hashicorp/aws"],
│   on cdk.tf.json line 23, in provider.aws[0]:
│   23:       }
│
```
