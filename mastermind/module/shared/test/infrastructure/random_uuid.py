import uuid


def random_uuid() -> str:
    return uuid.uuid4().__str__()
