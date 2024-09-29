from typing import NamedTuple


class Contact(NamedTuple):
    name: str
    tags: list[str]

    @staticmethod
    def from_dict(a_dict):
        return Contact(a_dict["name"], a_dict["tags"])
