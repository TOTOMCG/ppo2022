from Identifiable import Identifiable
from Serializable import Serializable
from Password import Password


class User(Identifiable, Serializable):

    def __init__(
        self,
        *,
        uuid=None,
        username,
        password=Password.Null(),
        email,
        first_name="",
        middle_name="",
        last_name="",
    ):
        Identifiable.__init__(self, uuid)
        Serializable.__init__(self, [
            "uuid",
            "username",
            "password",
            "email",
            "first_name",
            "middle_name",
            "last_name",
        ])
        self._username = username
        if isinstance(password, Password):
            self._password = password
        elif isinstance(password, str):
            self._password = Password(password)
        else:
            self._password = None
        self._email = email
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_namee(self):
        return self._middle_name

    @property
    def last_name(self):
        return self._last_name


__all__ = ["User"]


if __name__ == "__main__":
    user = User(username="Mark", email="test@test.com", password="123")
    print(dict(user))