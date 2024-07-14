from manim import BLUE, DEGREES, VGroup, UL, UR, DL, DR
from manim import Rectangle, Line, AnimationGroup, Dot
import numpy as np

class Input(VGroup):
    def __init__(self, channels, width, height, **kwargs):
        super().__init__(**kwargs)
        self.channels = channels
        self._width = width
        self._height = height
        self.ancs = None


    def _construct(self):
        """Constructs the layers of the Input module"""

        z_lvl = 0
        layers = VGroup()

        for i in range(self.channels):
            rectangle = Rectangle(width=self._width, height=self._height, color=BLUE)
            rectangle.set_fill(BLUE, opacity=0.2)
            rectangle.move_to([0, 0, z_lvl+(i/2)])

            layers.add(rectangle)

        self.ancs = self._generate_ancs(layers)
       
        self.add(layers)
        self.add(self.ancs)


    def _generate_ancs(self, layers) -> VGroup:
        """Generates the anchor points for each layer"""
        ancs = VGroup()
        for layer in layers.submobjects:
            ancs.add(
                VGroup(
                Dot(layer.get_corner(UL), fill_opacity=0.0, radius=0.0),
                Dot(layer.get_corner(UR), fill_opacity=0.0, radius=0.0),
                Dot(layer.get_corner(DL), fill_opacity=0.0, radius=0.0),
                Dot(layer.get_corner(DR), fill_opacity=0.0, radius=0.0)
                )
            )
        return ancs
    
    @property
    def surface_ancs(self):
        return self.ancs.submobjects[-1]


    def forward_pass(self) -> AnimationGroup:
        """Runs the forward pass of the Input module"""