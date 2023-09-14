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
from src.pyautoeios._internal.rs_node import RSNode
from src.pyautoeios._internal.rs_structures import RSType


class RSCombatInfoList(RSType):
    def head(self) -> RSNode:
        _ref = self.eios.get_object(self.ref, hooks.COMBATINFOLIST_HEAD)
        return RSNode(self.eios, _ref)


class RSCombatInfo(RSType):
    def health(self) -> int:
        return self.eios.get_int(self.ref, hooks.COMBATINFO1_HEALTH)

    def health_ratio(self) -> int:
        return self.eios.get_int(self.ref, hooks.COMBATINFO1_HEALTHRATIO)

    def health_scale(self) -> int:
        return self.eios.get_int(self.ref, hooks.COMBATINFO2_HEALTHSCALE)
