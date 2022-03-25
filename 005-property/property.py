# pylint: disable=missing-class-docstring
#!/usr/bin/env python3
"""
    Based on Anthony Explains
    https://www.youtube.com/watch?v=orp6bhe4i00&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=6
"""
from functools import cached_property
from typing import List


class Location:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    @cached_property
    def loc_aux(self) -> list:
        """ Tests the cached property.
            Simply in the first runtime the print method and any another
            computation is executed. After this, the another executations only
            returns the same first output (without print method),
            independly the "self" state.

        Returns:
            list: returns the locations attributes.
        """
        print('computing...')
        return [self.x, self.y]

    @property
    def loc(self) -> list:
        return [self.x, self.y]

    @loc.setter
    def loc(self, loc: List[int, int]) -> None:
        self.x , self.y = loc

    @loc.deleter
    def loc(self) -> None:
        self.x = self.y = 0

    def move_left(self) -> None:
        self.x -= 1

    def move_right(self) -> None:
        self.x += 1

    def move_up(self) -> None:
        self.y += 1

    def move_down(self) -> None:
        self.y -= 1

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.x}, {self.y})"
