## Setup credentials

Using https://direnv.net/

Example `.envrc`

```bash
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
```

## Explore docs:

```
pipenv shell

import cdktf_cdktf_provider_aws

help(cdktf_cdktf_provider_aws.AwsProvider)

```

## Tutorials

- Getting Started With CDK for Terraform and Python: https://www.youtube.com/watch?v=Ee2qh-pEC5k
- Unboxing the CDK to Terraform output format: https://www.youtube.com/watch?v=9s_BAyQIAhs
  - https://github.com/adamjkeller/ContainersFromTheCouch-terraform-cdk-example
- https://github.com/hashicorp/terraform-cdk/blob/main/docs/getting-started/python.md
- `tfcdk` Deep Dive: https://www.youtube.com/watch?v=nNr8JrN-9HE
- AWS CDK: https://www.youtube.com/watch?v=NkI5yeMFRK8

## Initialize a new project

Using Python as primary language CDK

```bash
cdktf init --template="python"
```

```bash
cdktf deploy
```

## Step:

- synthesizing
- initializing
- planning
- deploying

## Common errors

### Missing the ENV variables for AWS Authentication.

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
