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
from src.pyautoeios._internal.rs_cache import RSCache
from src.pyautoeios._internal.rs_model import RSModel
from src.pyautoeios._internal.rs_structures import RSType, get_rs_int_array
from src.pyautoeios._internal.rs_animated_model import RSAnimatedModel
from src.pyautoeios._internal.rs_animation_sequence import RSAnimationSequence


class RSPlayerDefinition(RSType):
    def oid(self) -> int:
        return self.eios.get_int(self.ref, hooks.PLAYERDEFINITION_NPCTRANSFORMID)

    def is_female(self) -> bool:
        return self.eios.get_bool(self.ref, hooks.PLAYERDEFINITION_ISFEMALE)

    def model_id(self) -> int:
        return self.eios.get_long(self.ref, hooks.PLAYERDEFINITION_MODELID)

    def animated_model_id(self) -> int:
        return self.eios.get_long(self.ref, hooks.PLAYERDEFINITION_ANIMATEDMODELID)

    def equipment(self) -> List[int]:
        return get_rs_int_array(
            self.eios, ref=self.ref, hook=hooks.PLAYERDEFINITION_EQUIPMENT
        )

    def model_cache(self) -> RSCache:
        _ref = self.eios.get_object(self.ref, hooks.PLAYERDEFINITION_MODELCACHE)
        return RSCache(eios=self.eios, ref=_ref)

    def cached_model(self) -> RSModel:
        cache = self.model_cache()
        if not self.ref or not cache.ref:
            print("cached_model: self.ref or cache.ref is None")
            return None
        
        model_id = self.animated_model_id()
        node = cache.hash_table().get_object(model_id)
        print(node)
        return RSModel(eios=self.eios, ref=node.ref)

    def get_model(
        self,
        model: RSModel,
        idle_sequence: RSAnimationSequence,
        animation_frame: int,
        movement_sequence: RSAnimationSequence,
        movement_frame: int,
    ) -> RSAnimatedModel:
        raise NotImplementedError
