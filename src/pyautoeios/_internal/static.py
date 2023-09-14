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

import random
import sys
import time
import math
from typing import Tuple

import pyautogui
from src.pyautoeios._internal.geometry import Rectangle

from src.pyautoeios._internal import hooks
from src.pyautoeios._internal.rs_actor import base_x, base_y
from src.pyautoeios._internal.rs_local_player import RSLocalPlayer
from src.pyautoeios.eios import EIOS

SINE = []
COSINE = []
for i in range(2048):
    SINE.append(int(65536 * math.sin(i * 0.0030679615)))
    COSINE.append(int(65536 * math.cos(i * 0.0030679615)))

_STATES = {
    (0, 10 , False): "WELCOME_SCREEN",
    (0, 10 , True): "WELCOME_SCREEN",
    (0, 30 , False): "TIMEOUT1",
    (0, 10, True): "ENTER_USERNAME",
    (0, 10, False): "ENTER_USERNAME",
    (2, 20, False): "LOADING_PLEASE_WAIT",
    (2, 20, True): "LOADING",
    (2, 25 , False): "MOVING_REGIONS",
    (2, 25 , True): "BETWEEN_STATES",
    (2, 30 , False): "NORMAL",
    (2, 30 , True): "CLICK_TO_PLAY",
    (2, 45 , False): "SWITCHING_WORLD",
    (2, 45 , True): "SWITCHING_WORLD",
    (24, 10 , False): "DISCONNECTED",
    (24, 10 , True): "DISCONNECTED",
}

def game_state(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_GAMESTATE)

def _is_client_loading(eios: EIOS) -> bool:
    return eios.get_bool(None, hooks.CLIENT_ISLOADING)

def r_initialize_constants(eios: EIOS) -> None:
    raise NotImplementedError

def r_initialize_tile_settings(eios: EIOS) -> None:
    raise NotImplementedError

def r_initialize_tile_heights(eios: EIOS) -> None:
    raise NotImplementedError

def r_initialize_varp_masks(eios: EIOS) -> None:
    raise NotImplementedError

def is_client_loading(eios: EIOS) -> bool:
    _game_state = game_state(eios)
    return (
        (_game_state == 25)
        or (_game_state == 40)
        or (_game_state == 45)
        or _is_client_loading(eios)
    )

def update_region_cache(eios: EIOS) -> None:
    raise NotImplementedError

def loop_cycle(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_LOOPCYCLE)

def login_state(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_LOGINSTATE)

def get_client_dimensions(eios: EIOS) -> Tuple[int, int]:
    return eios.get_target_dimensions()

# def base_x(eios: EIOS) -> int:
#     return eios.get_int(None, hooks.CLIENT_BASEX)

# def base_y(eios: EIOS) -> int:
#     return eios.get_int(None, hooks.CLIENT_BASEY)

def shr(x: int, y: int) -> int:
    return x >> y

def shl(x: int, y: int) -> int:
    return x << y


def move_to_spot_in_Rectangle(Rectangle, **kwargs):
    # print(f"Rectangle = {Rectangle}")
    if "duration" not in kwargs:
        kwargs["duration"] = random.uniform(0.3, 1.1)
    if "tween" not in kwargs:
        kwargs["tween"] = pyautogui.easeOutQuad
    #
    cx, cy = pyautogui.center(Rectangle)
    x = random.randint(int(-1 * (Rectangle.width / 3)), int(Rectangle.width / 3)) + cx
    y = random.randint(int(-1 * (Rectangle.height / 3)), int(Rectangle.height / 3)) + cy
    # print(f"x = {x}, y = {y}")
    pyautogui.moveTo(x, y, **kwargs)


def click_on_spot_in_Rectangle(Rectangle, **kwargs):
    move_to_spot_in_Rectangle(Rectangle, **kwargs)
    pyautogui.click(**kwargs)


def click_disconnected(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 285
    left = (width // 2) - 67
    bottom = 317
    right = (width // 2) + 67
    Rectangle = Rectangle(left, top, right - left, bottom - top)
    click_on_spot_in_Rectangle(Rectangle)


def click_existing_user(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 275
    left = (width // 2) + 12
    bottom = 307
    right = (width // 2) + 146
    Rectangle = Rectangle(left, top, right - left, bottom - top)
    click_on_spot_in_Rectangle(Rectangle)


def click_email_prompt(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 245
    left = (width // 2) - 110
    bottom = 254
    right = (width // 2) - 73
    Rectangle = Rectangle(left, top, right - left, bottom - top)
    click_on_spot_in_Rectangle(Rectangle)


def click_password_prompt(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 258
    left = (width // 2) - 108
    bottom = 267
    right = (width // 2) - 44
    Rectangle = Rectangle(left, top, right - left, bottom - top)
    click_on_spot_in_Rectangle(Rectangle)


def click_login_button(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 305
    left = (width // 2) - 148
    bottom = 337
    right = (width // 2) - 14
    Rectangle = Rectangle(left, top, right - left, bottom - top)
    click_on_spot_in_Rectangle(Rectangle)

def click_click_to_play(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 296
    left = (width // 2) - 110
    bottom = 378
    right = (width // 2) + 110
    Rectangle = Rectangle(left, top, right - left, bottom - top)
    click_on_spot_in_Rectangle(Rectangle)


def count_pixels(Rectangle: Rectangle) -> dict:
    """
    Returns a count of pixels per a unique color
    Args:
        Rectangle (Rectangle): the region of the screen to count all colors from
    Returns:
        a key-value pairing of the rgb color value and the number of times the color was present in the image
    """
    color_count = {}
    with pyautogui.screenshot(region=Rectangle) as image:
        width, height = image.size
        rgb_image = image.convert('RGB')
        # iterate through each pixel in the image and keep a count per unique color
        for x in range(width):
            for y in range(height):
                rgb = rgb_image.getpixel((x, y))
                if rgb in color_count:
                    color_count[rgb] += 1
                else:
                    color_count[rgb] = 1
    return color_count


def login(eios: EIOS, username:str, password: str) -> None:

    _state = get_complex_state(eios)
    if _state == "DISCONNECTED":
        click_disconnected(eios)
        time.sleep(0.5)
        while _state not in ("WELCOME_SCREEN", "ENTER_USERNAME"):
            #print(_state)
            _state = get_complex_state(eios)
            time.sleep(0.5)

    if _state == "WELCOME_SCREEN":
        click_existing_user(eios)
        time.sleep(0.5)
        while _state != "ENTER_USERNAME":
            #print(_state)
            _state = get_complex_state(eios)
            time.sleep(.5)

    if _state == "ENTER_USERNAME":

        # enter username if not present
        user_entered = eios.get_string(None, hooks.LOGIN_USERNAME)
        if user_entered != username:
            click_email_prompt(eios)
            eios.send_string("\b" * len(user_entered), 35, 10)
            eios.send_string(username, 100,100)

        # enter password if not present
        pass_entered = eios.get_string(None, hooks.LOGIN_PASSWORD)
        if pass_entered != password:
            click_password_prompt(eios)
            eios.send_string("\b" * len(pass_entered), 35, 10)
            eios.send_string(password, 100,100)

        # click login then wait for lobby
        click_login_button(eios)

        # if delete_username or False
        while _state != "CLICK_TO_PLAY":
            #print(_state)
            _state = get_complex_state(eios)
            time.sleep(.5)
            response1 = eios.get_string(None, hooks.LOGIN_RESPONSE1)
            if 'has been updated!' in response1:
                response2 = eios.get_string(None, hooks.LOGIN_RESPONSE2)
                sys.exit(f"Reopen the client. {response1} {response2}")
            if 'need a members account' in response1:
                response2 = eios.get_string(None, hooks.LOGIN_RESPONSE2)
                sys.exit(f"{response1} Manually set to F2P to continue.")




    # wait for click to play splash screen
    if _state == "CLICK_TO_PLAY":
        click_login_button(eios)
        while _state != "NORMAL":
            #print(_state)
            _state = get_complex_state(eios)
            time.sleep(.5)


def get_complex_state(eios: EIOS):
    _login_state = login_state(eios)
    _game_state = game_state(eios)
    _loading = _is_client_loading(eios)
    _state = _STATES.get((_login_state, _game_state, _loading), None)
    if not _state:
        print(f"{_login_state = }, {_game_state = }, {_loading = }")
        return "UNKNOWN_STATE"
    print(f"{_login_state = }, {_game_state = }, {_loading = }")
    return _state


def me(eios: EIOS) -> RSLocalPlayer:
    return RSLocalPlayer(eios)

def orientation(p, q, r):
    """
    To find the orientation of an ordered triplet (p, q, r).
    Returns:
    0 : Collinear points
    1 : Clockwise points
    2 : Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def jarvis_march(x_points, y_points):
    n = len(x_points)
    if n < 3:
        # Convex hull is not possible with less than 3 points
        return

    points = list(zip(x_points, y_points))

    # Start with the leftmost point
    l = min(range(n), key=lambda i: points[i])

    hull = []
    p = l
    while True:
        hull.append(points[p])

        # Search for a point 'q' such that orientation(p, x, q) is
        # counterclockwise for all points 'x'.
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        # If we're back to the starting point, break
        if p == l:
            break

    return hull