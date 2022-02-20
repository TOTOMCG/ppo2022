from Identifiable import Identifiable
from Serializable import Serializable
from User import User


class Group(Identifiable, Serializable):

    def __init__(self, *, uuid=None, name):
        Serializable.__init__(self, ["uuid", "name"])
        Identifiable.__init__(self, uuid)
        self._name = name
        self._users = {}

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password

    def add_user(self, user: User):
        self._users[user.uuid] = user


__all__ = ["Group"]
