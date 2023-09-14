import time
from src.pyautoeios._internal.rs_structures import get_rs_object_array
from src.pyautoeios.eios import EIOS
import src.pyautoeios as pyauto
from src.pyautoeios._internal.rs_client import RSClient
from src.pyautoeios._internal import hooks

pyauto.inject_clients()
client = pyauto.clients[0]
pyauto.pair_client(client)

rs_client = RSClient(client, None)
reflect = EIOS()
local_player = pyauto.static.me(client)
scene = get_rs_object_array(reflect, None, hooks.REGION_SCENETILES)
print(scene)

ltile = local_player.local_tile()
tile = local_player.tile()
