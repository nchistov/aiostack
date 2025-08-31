from typing import NamedTuple
from .item import Item


class RawResponseDict(NamedTuple):
    items: list[Item]
    has_more: bool
    quota_max: int
    quota_remaining: int
