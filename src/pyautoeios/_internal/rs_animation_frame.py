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
from typing import List

from src.pyautoeios._internal import hooks
from src.pyautoeios._internal.rs_animation import RSAnimation
from src.pyautoeios._internal.rs_structures import RSType


class RSAnimationFrame(RSType):
    def animation(self, index: int) -> RSAnimation:
        raise NotImplementedError

    def animations(self) -> List[RSAnimation]:
        raise NotImplementedError

    def get_frame(self, frame_id: int) -> RSAnimationFrame:
        raise NotImplementedError
