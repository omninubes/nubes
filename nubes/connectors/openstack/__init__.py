from openstack.compute.v2 import server

from nubes.common import models


def transform_server(from_model):
    return models.Server(uuid=from_model.id, name=from_model.name,
                         flavor=from_model.flavor['id'],
                         image=from_model.image['id'])


models.register_transform(server.Server, transform_server)
models.register_transform(server.ServerDetail, transform_server)
