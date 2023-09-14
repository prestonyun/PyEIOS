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

# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
import math
from pyscreeze import Point

from src.pyautoeios._internal import hooks
from src.pyautoeios._internal import static
from src.pyautoeios.eios import EIOS
from src.pyautoeios._internal.rs_structures import RSType


class RSTile(RSType):
    def __init__(self, eios: EIOS, x: int, y: int, z: int = None):
        self.x = x
        self.y = y
        self.z = z
        self.scope = "local"
        super().__init__(eios=eios, ref=None)

    def region_id(self) -> int:
        return static.shl(static.shr(self.x, 6), 8) or (self.y >> 6)

    def to_local(self) -> RSTile:
        x = ((self.x - static.base_x(self.eios)) << 7) + (1 << 6)
        y = ((self.y - static.base_y(self.eios)) << 7) + (1 << 6)
        return RSTile(self.eios, x, y)

    def to_global(self) -> RSTile:
        x = static.base_x(self.eios) + self.x // 128
        y = static.base_y(self.eios) + self.y // 128
        return RSTile(self.eios, x, y)
    
    def localToCanvas(self) -> Point:
        if self.scope != "local":
            raise ValueError("tile must be local")
        cameraX = self.eios.get_int(None, hooks.CLIENT_CAMERAX)
        cameraY = self.eios.get_int(None, hooks.CLIENT_CAMERAY)
        cameraZ = self.eios.get_int(None, hooks.CLIENT_CAMERAZ)
        cameraPitch = self.eios.get_int(None, hooks.CLIENT_CAMERAPITCH)
        cameraYaw = self.eios.get_int(None, hooks.CLIENT_CAMERAYAW)
        pitchSin = static.SINE[cameraPitch]
        pitchCos = static.COSINE[cameraPitch]
        yawSin = static.SINE[cameraYaw]
        yawCos = static.COSINE[cameraYaw]

        _x = self.x - cameraX
        _y = self.y - cameraY
        _z = self.z - cameraZ if self.z else 0

        x1 = _x * yawCos + _y * yawSin >> 16
        y1 = _y * yawCos - _x * yawSin >> 16
        y2 = _z * pitchCos - y1 * pitchSin >> 16
        z1 = y1 * pitchCos + _z * pitchSin >> 16

        if z1 >= 50:
            scale = self.eios.get_int(None, hooks.CLIENT_VIEWPORTSCALE)
            pointX = self.eios.get_int(None, hooks.CLIENT_VIEWPORTWIDTH) // 2 + x1 * scale // z1
            pointY = self.eios.get_int(None, hooks.CLIENT_VIEWPORTHEIGHT) // 2 + y2 * scale // z1
            return Point(pointX, pointY)

    def local_to_world_tile(self) -> RSTile:
        raise NotImplementedError

    def world_to_local_tile(self) -> RSTile:
        raise NotImplementedError

    def tile_to_mm(self) -> Point:
        raise NotImplementedError

    def mm_to_tile(self) -> RSTile:
        raise NotImplementedError

    def tile_to_ms(self) -> Point:
        raise NotImplementedError

    def get_height(self, plane: int = None) -> int:
        raise NotImplementedError
