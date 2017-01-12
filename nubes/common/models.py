import json
import six

_transform_registry = {}


def register_transform(from_type, func):
    _transform_registry[from_type] = func


class BaseModel(object):

    def __str__(self):
        str_dict = {}
        for key, value in six.iteritems(self.__dict__):
            if key.startswith('_'):
                continue
            str_dict[key] = value
        return json.dumps(str_dict)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def transform(cls, from_model):
        if isinstance(from_model, list):
            if from_model:
                key = type(from_model[0])
            else:
                return []
        elif not from_model:
            return
        else:
            key = type(from_model)
        func = _transform_registry[key]
        if isinstance(from_model, list):
            return [func(item) for item in from_model]
        return func(from_model)


class Server(BaseModel):

    def __init__(self, uuid=None, name=None, flavor=None, image=None,
                 networks=None):
        self.uuid = uuid
        self.name = name
        self.flavor = flavor
        self.image = image
        self.networks = networks or []
