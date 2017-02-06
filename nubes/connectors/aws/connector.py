import boto3.session

from nubes.common import models
from nubes.connectors import base


def transform_server(from_model):
    return models.Server(uuid=from_model.instance_id, name='',
                         flavor=from_model.instance_type,
                         image=from_model.image_id)


class AWSConnector(base.BaseConnector):

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.connection = boto3.session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name)

        self.ec2_resource = self.connection.resource("ec2")
        self.ec2_client = self.connection.client("ec2")

    @classmethod
    def name(cls):
        return "aws"

    def create_server(self, image_id, min_count, max_count, **kwargs):
        server = self.ec2_resource.create_instances(ImageId=image_id,
                                                    MinCount=min_count,
                                                    MaxCount=max_count,
                                                    **kwargs)
        if not server:
            return
        return transform_server(server[0])

    def list_servers(self):
        desc = self.ec2_client.describe_instances()
        return desc['Reservations']['Instances']

    def delete_server(self, instance_id):
        self.ec2_resource.instances.filter(
            InstanceIds=[instance_id]).stop()
        self.ec2_resource.instances.filter(
            InstanceIds=[instance_id]).terminate()
