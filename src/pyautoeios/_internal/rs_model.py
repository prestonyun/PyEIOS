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

from typing import List, Tuple

from src.pyautoeios._internal import hooks
from src.pyautoeios._internal.rs_structures import RSType, get_rs_int_array
from src.pyautoeios._internal import static


class RSModel(RSType):
    def raw_vertices(self) -> List[List[int]]:
        x = get_rs_int_array(self.eios, self.ref, hooks.MODEL_VERTICESX)
        y = get_rs_int_array(self.eios, self.ref, hooks.MODEL_VERTICESY)
        z = get_rs_int_array(self.eios, self.ref, hooks.MODEL_VERTICESZ)
        return [x, y, z]

    def raw_indices(self) -> List[List[int]]:
        x = get_rs_int_array(self.eios, self.ref, hooks.MODEL_INDICESX)
        y = get_rs_int_array(self.eios, self.ref, hooks.MODEL_INDICESY)
        z = get_rs_int_array(self.eios, self.ref, hooks.MODEL_INDICESZ)
        return [x, y, z]

    def fits_single_tile(self) -> bool:
        return self.eios.get_bool(self.ref, hooks.MODEL_FITSSINGLETILE)

    def height(self) -> int:
        return self.eios.get_int(self.ref, hooks.RENDERABLE_MODELHEIGHT)

    def bounds(self) -> List[Tuple[int, int, int]]:
        vertices = self.raw_vertices()
        x_points, y_points, _ = vertices  # We only need x and y for 2D convex hull

        # Get the convex hull using jarvis_march
        hull = static.jarvis_march(x_points, y_points)

        if not hull:
            return []

        # Find the bounding rectangle of the convex hull
        min_x = min([point[0] for point in hull])
        max_x = max([point[0] for point in hull])
        min_y = min([point[1] for point in hull])
        max_y = max([point[1] for point in hull])

        # Return the four corners of the bounding rectangle
        return [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]
