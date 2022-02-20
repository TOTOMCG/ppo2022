import hashlib


class Password(str):
    
    def __new__(cls, password: str):
        return super(Password, cls).__new__(cls, Password.hash(password).hexdigest())

    @staticmethod
    def hash(data, *, hash_func=hashlib.sha256):
        return hash_func(str(data).encode())

    @staticmethod
    def Null():
        return None


__all__ = ["Password"]
