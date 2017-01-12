import mock
import testtools

from nubes.connectors.openstack import connector


class TestConnector(testtools.TestCase):

    def setUp(self):
        super(TestConnector, self).setUp()
        mock.patch.object(connector.connection, 'Connection').start()
        self.os_connector = connector.OpenstackConnector('a_url', 'a_username',
                                                         'a_password',
                                                         'a_project_name')
        self.compute = self.os_connector.connection.compute

    def test_name(self):
        self.assertEqual("openstack", connector.OpenstackConnector.name())

    def test_create_server(self):
        self.os_connector.create_server('test', 'image-1', 'flavor-1',
                                        ['network-1', 'network-2'])
        self.compute.create_server.assert_called_once_with(
            name='test', flavor_id='flavor-1', image_id='image-1',
            networks=[{'uuid': 'network-1'}, {'uuid': 'network-2'}]
        )

    def test_list_servers(self):
        self.os_connector.list_servers()
        self.compute.servers.assert_called_once_with()

    def test_delete_server(self):
        self.os_connector.delete_server('server-1')
        self.compute.delete_server.assert_called_once_with('server-1')
