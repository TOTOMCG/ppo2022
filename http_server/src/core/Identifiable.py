from uuid import uuid4


class Identifiable:
    def __init__(self, uuid=None):
        self.uuid = uuid if uuid else str(uuid4())


__all__ = ["Identifiable"]
