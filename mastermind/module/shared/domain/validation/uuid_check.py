import re

__uuid_lowercase_regex = re.compile(
    "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")


def is_uuid(string: str) -> bool:
    return __uuid_lowercase_regex.match(string) is not None
