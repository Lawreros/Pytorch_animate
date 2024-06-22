from manim import BLUE
from manim import Rectangle, Line, VGroup
import numpy as np

class Input(VGroup):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self._width = width
        self._height = height


    def _construct(self):
        rect = Rectangle(width=self._width, height=self._height, color=BLUE)
        self.add(rect)