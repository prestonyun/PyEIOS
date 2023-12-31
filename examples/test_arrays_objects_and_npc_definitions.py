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


import src.pyautoeios as pyauto
from src.pyautoeios._internal.rs_client import RSClient
from src.pyautoeios._internal import hooks
from src.pyautoeios._internal.rs_structures import RSObjectArray
from src.pyautoeios._internal.rs_npc import RSNPC

import src.pyautoeios as pyauto
from src.pyautoeios._internal.static import me

pyauto.inject_clients()
client = pyauto.clients[0]
pyauto.pair_client(client)
rs_client = RSClient(client, None)

npcs = rs_client.all_npcs()
# npc = npcs[0]
# definition = npc.definition()
npc_array = []
for npc in rs_client.all_npcs():
    definition = npc.definition()
    if definition:
        npc_array.append(
            {
                "name": definition.name(),
                "oid": definition.oid(),
            }
        )

print(npc_array)
