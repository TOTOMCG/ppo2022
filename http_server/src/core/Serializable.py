import json


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class Serializable():

    __encoder = JSONEncoder()

    def __init__(self, keys):
        self.__keys = keys
        for key in keys:
            if key != "__keys":
                try:
                    setattr(self, key, None)
                except Exception:
                    pass

    def keys(self):
        return self.__keys[:]

    def serialize(self, to=json):
        data = {}
        for key in self.__keys:
            value = getattr(self, key)
            if isinstance(value, Serializable):
                data[key] = value.serialize()
            else:
                data[key] = value
        return json.dump(data) if to == json else data

    def __getitem__(self, key):
        if key in self.__keys:
            return getattr(self, key)
        else:
            return None


__all__ = ["Serializable"]
