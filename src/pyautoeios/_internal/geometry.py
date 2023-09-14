import re
from typing import List, NamedTuple
from .random_util import random_point_in, random_seeds
import mss
import cv2

import numpy as np

Point = NamedTuple("Point", x=int, y=int)

class Rectangle:
    PATTERN = re.compile(r"java.awt.Rectangle\[x=(\d+),y=(\d+),w=(\d+),h=(\d+)\]")
    def __init__(self, left: int, top: int, width: int, height: int, parent: "Rectangle" = None):
        """
        Defines a rectangle area on screen.
        Args:
            left: The leftmost x coordinate of the rectangle.
            top: The topmost y coordinate of the rectangle.
            width: The width of the rectangle.
            height: The height of the rectangle.
            offset: The offset to apply to the rectangle.
        Returns:
            A Rectangle object.
        """
        if isinstance(left, str):
            left = int(float(left))
        if isinstance(top, str):
            top = int(float(top))
        if isinstance(width, str):
            width = int(float(width))
        if isinstance(height, str):
            height = int(float(height))

        if parent:
            left += parent.left
            top += parent.top
        
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle({self.left}, {self.top}, {self.width}, {self.height})"
    
    @staticmethod
    def decode(s):
        match = Rectangle.PATTERN.match(s)
        if match:
            return Rectangle(*map(int, match.groups()))

    @classmethod
    def from_points(cls, start_point: Point, end_point: Point):
        """
        Creates a Rectangle from two points.
        Args:
            start_point: The first point.
            end_point: The second point.
            offset: The offset to apply to the rectangle.
        Returns:
            A Rectangle object.
        """
        return cls(
            start_point.x,
            start_point.y,
            end_point.x - start_point.x,
            end_point.y - start_point.y,
        )

    def screenshot(self) -> cv2.Mat:
        """
        Screenshots the Rectangle.
        Returns:
            A BGR Numpy array representing the captured image.
        """
        with mss.mss() as sct:  # TODO: When MSS bug is fixed, reinstate this.
            # global sct  # TODO: When MSS bug is fixed, remove this.
            monitor = self.to_dict()
            res = np.array(sct.grab(monitor))[:, :, :3]
            if self.subtract_list:
                for area in self.subtract_list:
                    res[
                        area["top"] : area["top"] + area["height"],
                        area["left"] : area["left"] + area["width"],
                    ] = 0
        return res

    def random_point(self, custom_seeds: List[List[int]] = None) -> Point:
        """
        Gets a random point within the Rectangle.
        Args:
            custom_seeds: A list of custom seeds to use for the random point. You can generate
                            a seeds list using RandomUtil's random_seeds() function with args.
                            Default: A random seed list based on current date and object position.
        Returns:
            A random Point within the Rectangle.
        """
        if custom_seeds is None:
            center = self.get_center()
            custom_seeds = random_seeds(mod=(center[0] + center[1]))
        x, y = random_point_in(
            self.left, self.top, self.width, self.height, custom_seeds
        )
        return Point(x, y)

    def get_center(self) -> Point:
        """
        Gets the center point of the rectangle.
        Returns:
            A Point representing the center of the rectangle.
        """
        return Point(self.left + self.width // 2, self.top + self.height // 2)

    def get_top_left(self) -> Point:
        """
        Gets the top left point of the rectangle.
        Returns:
            A Point representing the top left of the rectangle.
        """
        return Point(self.left, self.top)

    def get_top_right(self) -> Point:
        """
        Gets the top right point of the rectangle.
        Returns:
            A Point representing the top right of the rectangle.
        """
        return Point(self.left + self.width, self.top)

    def get_bottom_left(self) -> Point:
        """
        Gets the bottom left point of the rectangle.
        Returns:
            A Point representing the bottom left of the rectangle.
        """
        return Point(self.left, self.top + self.height)

    def get_bottom_right(self) -> Point:
        """
        Gets the bottom right point of the rectangle.
        Returns:
            A Point representing the bottom right of the rectangle.
        """
        return Point(self.left + self.width, self.top + self.height)
    
    def contains(self, x: int, y: int) -> bool:
        """
        Checks if a point exists in the rectangle.
        Args:
            x: The x-coordinate to check.
            y: The y-coordinate to check.
        """
        return (
            self.left <= x <= self.left + self.width and
            self.top <= y <= self.top + self.height
        )
    
    def intersects(self, other: 'Rectangle') -> bool:
        """
        Checks if the current rectangle intersects with another rectangle.
        Returns:
            True if the rectangles intersect, False otherwise.
        """
        return (
            self.left < other.left + other.width and
            self.left + self.width > other.left and
            self.top < other.top + other.height and
            self.top + self.height > other.top
        )
    
    def contains_rect(self, other: 'Rectangle') -> bool:
        # Method to check if another rectangle is contained within the current rectangle
        return (
            self.left <= other.left and
            self.left + self.width >= other.left + other.width and
            self.top <= other.top and
            self.top + self.height >= other.top + other.height
        )