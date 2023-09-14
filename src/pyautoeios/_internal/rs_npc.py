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

from typing import List, Optional

from pyscreeze import Point

from src.pyautoeios._internal import hooks
from src.pyautoeios._internal.rs_actor import RSActor
from src.pyautoeios._internal.rs_model import RSModel
from src.pyautoeios._internal.rs_npc_definition import RSNPCDefinition
from src.pyautoeios._internal.rs_animated_model import RSAnimatedModel


class RSNPC(RSActor):
    def definition(self) -> RSNPCDefinition:
        _ref = self.eios.get_object(self.ref, hooks.NPC_DEFINITION)
        return RSNPCDefinition(self.eios, _ref)

    def all_npcs(self):
        raise NotImplementedError(
            "moved to RSClient in python verison, to prevent circular imports"
        )

    def model(self) -> RSModel:
        raise NotImplementedError

    def animated_model(self) -> RSAnimatedModel:
        raise NotImplementedError

    def transformed_definition(self) -> Optional[RSNPCDefinition]:
        definition = self.definition()
        if not definition.ref:
            return None

        bit = -1
        transform_id = definition.transform_varbit()

        if transform_id != -1:
            bit = self.eios.client.get_varbit(transform_id)
        else:
            bit = self.eios.varps.varp_main(definition.transform_varp())

        transformations = definition.transformations()
        if 0 <= bit < len(transformations) - 1:
            definition_id = transformations[bit]
        elif transformations:
            definition_id = transformations[-1]

        if definition_id != -1:
            return RSNPCDefinition.definition_cache(self.eios, definition_id)

        return definition

    def model(self) -> Optional[RSModel]:
        definition = self.transformed_definition()
        if not definition:
            return None
        return definition.cached_model()

    def animated_model(self) -> Optional[RSAnimatedModel]:
        model = self.model()
        if not model:
            return None

        # ... [You'll need to fill in the logic for retrieving the animation sequences and transforming the model]

        #return RSNPCDefinition.get_model(self.eios, model, idle_sequence, animation_frame, movement_sequence, movement_frame)

    def to_tpa(self) -> List[Point]:
        obj_model = self.model()
        obj_tile = self.local_tile()
        triangles = obj_model.project(obj_tile.x, obj_tile.y, obj_tile.get_height(), 0)
        points = []
        for triangle in triangles:
            points.extend([triangle.a, triangle.b, triangle.c])
        return points