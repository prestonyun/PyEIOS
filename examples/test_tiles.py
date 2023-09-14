import src.pyautoeios as pyauto
from src.pyautoeios._internal.rs_client import RSClient


pyauto.inject_clients()
with pyauto.clients.pop(0) as client:
    pyauto.pair_client(client)
    local_player = pyauto.static.me(client)

    ltile = local_player.local_tile()
    tile = local_player.tile()
    print(ltile.x, ltile.y)
    print(tile.x, tile.y)
    print(tile.localToCanvas())
    print(ltile.localToCanvas())