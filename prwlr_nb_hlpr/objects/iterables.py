"""
This module provides custom objects extending functionalities of the standard
library iterables.
"""


class listx(list):
    """
    Extends the standard list with custom methods
    """
    def __init__(
        self,
        li,
    ):
        self._li = li

    def __repr__(self):
        """
        Reproduce listx exactly like the standard list
        """
        return str(self._li)

    def without(
        self,
        element,
    ):
        """
        Return list without an <element>. The key difference from the standard
        list.remove() method is that this is fruitful.
        """
        return [_ for _ in self._li if _ != element]
