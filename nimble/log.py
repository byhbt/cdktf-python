from cdktf_cdktf_provider_aws import AwsProvider, cloudwatch

def create_log_group(self):
  log_group = cloudwatch.CloudwatchLogGroup(
    self,
    'centauri-python-log-group',
    name='centauri-python-log-group',
    retention_in_days=14
  )

  return log_group
