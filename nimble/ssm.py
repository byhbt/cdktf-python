from cdktf_cdktf_provider_aws import ssm

def create_new_string_parameter(scope, id, name, value):
    return ssm.SsmParameter(scope, id, name=name, type="String", value=value)
