import abc

import six


@six.add_metaclass(abc.ABCMeta)
class BaseConnector(object):

    @abc.abstractmethod
    def create_server(self, *kwargs):
        pass

    @abc.abstractmethod
    def list_servers(self):
        pass

    @abc.abstractmethod
    def delete_server(self, uuid):
        pass
