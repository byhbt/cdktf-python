from cdktf_cdktf_provider_aws import rds
from cdktf import TerraformVariable

def create_rds(self):
  db_name = TerraformVariable(self, 'db_name',
    type="string",
    description="Postgres Database name"
  )

  username = TerraformVariable(self, 'db_username',
    type="string",
    description="Username for Postgres DB",
    sensitive=True
  )

  password = TerraformVariable(self, 'db_password',
    type="string",
    description="Password for Postgres DB",
    sensitive=True
  )

  rds_instance = rds.DbInstance(self, "centauri-db",
    name=db_name.string_value,
    engine="postgres",
    engine_version="14.1",
    instance_class="db.t3.micro",
    username=username.string_value,
    password=password.string_value,
    allocated_storage=5,
    skip_final_snapshot=True
  )

  return rds_instance

def create_connection_str(rds):
  return "postgres://{username}:{password}@{endpoint}/{db_name}".format(username=rds.username, password=rds.password, endpoint=rds.endpoint, port=rds.port, db_name=rds.name)
