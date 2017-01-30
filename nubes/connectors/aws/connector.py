import boto3.session

from nubes.connectors import base


class AWSConnector(base.BaseConnector):

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.connection = boto3.session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name)

    @classmethod
    def name(cls):
        return "aws"

    def create_server(self, image_id, min_count, max_count, **kwargs):
        ec2_resource = self.connection.resource("ec2")
        server = ec2_resource.create_instances(ImageId=image_id,
                                               MinCount=min_count,
                                               MaxCount=max_count,
                                               **kwargs)
        return server

    def list_servers(self):
        ec2_client = self.connection.client("ec2")
        desc = ec2_client.describe_instances()
        return desc

    def delete_server(self, instance_id):
        ec2_resource = self.connection.resource("ec2")
        ec2_resource.instances.filter(
            InstanceIds=[instance_id]).stop()
        ec2_resource.instances.filter(
            InstanceIds=[instance_id]).terminate()
