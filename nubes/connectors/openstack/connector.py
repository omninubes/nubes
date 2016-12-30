from openstack import connection

from nubes.connectors import base


class OpenstackConnector(base.BaseConnector):

    def __init__(self, auth_url, username, password, project_name=None):
        self.connection = connection.Connection(auth_url=auth_url,
                                                username=username,
                                                password=password,
                                                project_name=project_name)

    def create_server(self, name, image, flavor, network_ids):
        network_ids = network_ids or []
        networks = []
        for network_id in network_ids:
            if isinstance(network_id, str):
                networks.append({'uuid': network_id})
            elif isinstance(network_id, dict) and 'uuid' in network_id:
                networks.append(network_id)
        server = self.connection.compute.create_server(name=name,
                                                       flavor_id=flavor,
                                                       image_id=image,
                                                       networks=networks)
        return server

    def list_servers(self):
        servers = list(self.connection.compute.servers())
        return servers

    def delete_server(self, uuid):
        self.connection.compute.delete_server(uuid)
