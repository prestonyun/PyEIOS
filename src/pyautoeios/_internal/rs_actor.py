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

from src.pyautoeios._internal import hooks
from src.pyautoeios._internal.rs_structures import RSType
from src.pyautoeios._internal.rs_tile import RSTile

from src.pyautoeios.eios import EIOS

def base_x(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_BASEX)

def base_y(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_BASEY)


class RSActor(RSType):
    def spoken_text(self) -> str:
        return self.eios.get_string(self.ref, hooks.ACTOR_SPOKENTEXT)

    def orientation(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_ORIENTATION)

    def local_x(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_LOCALX)

    def local_y(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_LOCALY)

    def local_tile(self) -> RSTile:
        return RSTile(eios=self.eios, x=self.local_x(), y=self.local_y())

    def tile(self) -> RSTile:
        x = base_x(self.eios) + ((self.local_x() % 0x100000000) >> 7)
        y = base_y(self.eios) + ((self.local_y() % 0x100000000) >> 7)
        return RSTile(eios=self.eios, x=x, y=y)

    def animation_id(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_ANIMATION)

    def is_animating(self) -> bool:
        return self.animation_id() > -1

    def spot_animation(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_SPOTANIMATION)

    def spot_animation_frame(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_SPOTANIMATIONFRAME)

    def spot_animation_frame_cycle(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_SPOTANIMATIONFRAMECYCLE)

    def graphics_id(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_GRAPHICSID)

    def animation_frame(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_ANIMATIONFRAME)

    def movement_sequence_id(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_MOVEMENTSEQUENCE)

    def movement_frame(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_MOVEMENTFRAME)

    def current_sequence_id(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_CURRENTSEQUENCE)

    def is_idle(self) -> bool:
        return not self.is_animating()

    def interacting_index(self) -> int:
        return self.eios.get_int(self.ref, hooks.ACTOR_INTERACTINGINDEX)

    def health(self) -> int:
        raise NotImplementedError

    def health_ratio(self) -> int:
        raise NotImplementedError

    def health_scale(self) -> int:
        raise NotImplementedError

    def health_percentage(self):
        raise NotImplementedError

    def is_in_combat(self):
        raise NotImplementedError

    def get_interacting(self):
        raise NotImplementedError

    def in_Rectangle(self):
        raise NotImplementedError
