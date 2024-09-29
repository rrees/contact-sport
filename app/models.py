from typing import NamedTuple


class Contact(NamedTuple):
    external_id: str
    name: str
    tags: list[str]

    @staticmethod
    def from_dict(a_dict):
        return Contact(a_dict["external_id"], a_dict["name"], a_dict["tags"])
