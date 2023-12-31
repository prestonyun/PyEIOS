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
from src.pyautoeios._internal.rs_structures import RSType, RSObjectArray


class RSIterableHashTable(RSType):
    def head(self) -> RSNode:
        _ref = self.eios.get_object(self.ref, hooks.ITERABLEHASHTABLE_HEAD)
        return RSNode(self.eios, _ref)

    def tail(self) -> RSNode:
        _ref = self.eios.get_object(self.ref, hooks.ITERABLEHASHTABLE_TAIL)
        return RSNode(self.eios, _ref)

    def bucket(self, index: int) -> RSNode:
        array_ref, size = self.eios.get_array_with_size(self.ref, hooks.ITERABLEHASHTABLE_BUCKETS)
        buckets = RSObjectArray(self.eios, array_ref, size)
        _ref = buckets[index]
        return RSNode(self.eios, _ref)

    def buckets(self) -> List[RSNode]:
        raise NotImplementedError
        # Buckets: Pointer;
        # Nodes: Array of Pointer;
        # I, BucketsSize: int;
        # BucketsSize := 0;
        # Buckets := RGetArray(R_EIOS, ref, BucketsSize, ITERABLEHASHTABLE_BUCKETS);
        # if Buckets = nil then
        #     Exit;

        # Nodes := RGetObjectArray(R_EIOS, Buckets, 0, BucketsSize);
        # RFreeObject(R_EIOS, Buckets);

        # SetLength(Result, BucketsSize);

        # for I := 0 to BucketsSize - 1 do

        #     Result[I].ref := Nodes[I];

    def index(self) -> int:
        return self.eios.get_int(self.ref, hooks.ITERABLEHASHTABLE_INDEX)

    def size(self) -> int:
        return self.eios.get_int(self.ref, hooks.ITERABLEHASHTABLE_SIZE)

    def get_object(self, oid: int) -> RSNode:
        index = oid & (self.size() - 1)
        head = self.bucket(index)
        print("index: ", index)
        print("size: ", self.size())
        if not head.ref:
            print("get_object: head.ref is None")
            return None

        current = head.next()
        head_uid = head.uid()
        print(head_uid)
        print(current.ref, current.uid())
        while current.ref and current.uid() != head_uid:
            current_uid = current.uid()
            if current_uid == oid:
                return current
            elif current_uid == -1:
                break
            current = current.next()
