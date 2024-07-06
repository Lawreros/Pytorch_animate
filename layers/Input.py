from manim import BLUE, DEGREES, VGroup
from manim import Rectangle, Line, AnimationGroup
import numpy as np

class Input(VGroup):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self._width = width
        self._height = height


    def _construct(self):
        rect = Rectangle(width=self._width, height=self._height, color=BLUE).copy()
        rect.set_fill(BLUE, opacity=0.2)
        
        rect = rect.rotate(about_point=rect.get_center(), axis=[0.02, 1, 0], angle=75*DEGREES)

        self.add(rect)


    def forward_pass(self) -> AnimationGroup:
        """Runs the forward pass of the Input module"""