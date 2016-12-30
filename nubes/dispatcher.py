from nubes.connectors.openstack import connector as os_connector

# NOTE(blogan): we can probably do a registration of each class that gets
# inherited from via metaclass so we don't have to build this manually.  This
# works for now though.
connectors = {os_connector.OpenstackConnector.name():
              os_connector.OpenstackConnector}


class Dispatcher(object):

    def __init__(self, connector_name, auth_url, username, password,
                 project_name):
        self.connector = connectors.get(connector_name)(auth_url, username,
                                                        password, project_name)

    def create_server(self, name, image, flavor, networks):
        return self.connector.create_server(name, image, flavor, networks)

    def list_servers(self):
        return self.connector.list_servers()

    def delete_server(self, uuid):
        self.connector.delete_server(uuid)
