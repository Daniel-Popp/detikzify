from typing import Callable

from tikz_elements.NodeStyle import NodeStyle
from tikz_elements.Line import Line
from collections import defaultdict
from tikz_elements.Point import Point

class Node:

    node_type: NodeStyle
    name: str = ""
    label: str = ""
    screen_location: Point = None
    distance: Callable

    def __init__(self, nt: NodeStyle, name: str, distance: Callable, screen_location: Point = None):
        self.node_type = nt
        self.name = name
        self.screen_location = screen_location
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def get_dragging(self):
        return self.dragging

    def get_node(self):
        return self.rectangle

    # figures out where the mouse is relative to the rectangle center
    def get_mouse_orientation(self, event):
        self.set_dragging(True)
        mouse_x, mouse_y = event.pos

        #generic distance function for weird shapes
        (self.offset_x, self.offset_y) = self.node_type.distance(Point (self.rectangle.x, self.rectange.y), Point(mouse_x, mouse_y))

    # updates the location to the new event location
    def update_location(self, event):
        mouse_x, mouse_y = event.pos
        self.rectangle.x = mouse_x + self.offset_x
        self.rectangle.y = mouse_y + self.offset_y

    def set_dragging(self, mode):
        self.dragging = mode