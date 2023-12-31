#    Copyright 2020 by Brett J. Moan
#
#    This file is part of pyautoeios.
#
#    pyautoeios is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyautoeios is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.

from typing import List

from src.pyautoeios._internal import hooks
from src.pyautoeios._internal.rs_node import RSNode
from src.pyautoeios._internal.rs_structures import RSType


class RSHashTable(RSType):
    def head(self) -> RSNode:
        _ref = self.eios.get_object(self.ref, hooks.HASHTABLE_HEAD)
        return RSNode(self.eios, _ref)

    def tail(self) -> RSNode:
        _ref = self.eios.get_object(self.ref, hooks.HASHTABLE_TAIL)
        return RSNode(self.eios, _ref)

    def bucket(self, index: int) -> RSNode:
        raise NotImplementedError

    def buckets(self) -> List[RSNode]:
        raise NotImplementedError

    def index(self) -> int:
        return self.eios.get_int(self.ref, hooks.HASHTABLE_INDEX)

    def size(self) -> int:
        return self.eios.get_int(self.ref, hooks.HASHTABLE_SIZE)

    def get_object(self, oid: int) -> RSNode:
        index = oid & (self.size() - 1)
        head = self.bucket(index)
        if not head.ref:
            return None

        current = head.next()
        if not current.ref:
            return None

        current_uid = None
        while True:
            current_uid = current.uid()
            if current_uid in (0, -1):
                return None
            if current_uid == oid:
                return current
            current = current.next()
