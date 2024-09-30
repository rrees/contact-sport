from typing import NamedTuple, Optional


class Address(NamedTuple):
    external_id: str
    label: str
    address: str

    def from_list(l):
        [external_id, label, address] = l
        return Address(external_id, label, address)


class Contact(NamedTuple):
    external_id: str
    name: str
    tags: list[str]
    addresses: Optional[list[Address]]

    @staticmethod
    def from_dict(a_dict):
        return Contact(
            a_dict["external_id"],
            a_dict["name"],
            a_dict["tags"],
            [Address.from_list(a) for a in a_dict.get("addresses", [])],
        )
