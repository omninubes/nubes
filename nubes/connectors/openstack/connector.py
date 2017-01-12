from openstack import connection

from nubes.common import models
from nubes.connectors import base


class OpenstackConnector(base.BaseConnector):

    def __init__(self, auth_url, username, password, project_name=None):
        self.connection = connection.Connection(auth_url=auth_url,
                                                username=username,
                                                password=password,
                                                project_name=project_name)

    @classmethod
    def name(cls):
        return "openstack"

    def create_server(self, name, image, flavor, networks):
        networks = networks or []
        dict_networks = []
        for network in networks:
            if isinstance(network, str):
                dict_networks.append({'uuid': network})
            elif isinstance(network, dict) and 'uuid' in network:
                dict_networks.append(network)
        server = self.connection.compute.create_server(name=name,
                                                       flavor_id=flavor,
                                                       image_id=image,
                                                       networks=dict_networks)
        return models.Server.transform(server)

    def list_servers(self):
        servers = list(self.connection.compute.servers())
        return models.Server.transform(servers)

    def delete_server(self, uuid):
        self.connection.compute.delete_server(uuid)
