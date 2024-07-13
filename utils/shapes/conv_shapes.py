from manim import BLUE, ORANGE, RIGHT, DOWN, UL, UR, DL, DR
from manim import Rectangle, Line, VGroup, Dot
import numpy as np

class FeatureMap(VGroup):
    def __init__(self, num_layers, height, width, color=BLUE):
        super().__init__()
        self.num_layers = num_layers
        self._height = height
        self._width = width
        self.ancs = None

        z_lvl = 0
        # Define the shapes and add them to self
        layers = VGroup()

        for i in range(num_layers):
            rectangle = Rectangle(height=height, width=width, stroke_color=color)
            rectangle.set_fill(color, opacity=0.2)
            rectangle.move_to([0, 0, z_lvl+(i/3)])
            
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




class GriddedRectangle(VGroup):
    """A rectangle with a grid drawn on it."""

    def __init__(self, height=3, width=3, color=ORANGE, **kwargs):
        super().__init__()
        rectangle = Rectangle(height=height, width=width,
                              stroke_color=color)
        rectangle.set_fill(color, opacity=0.2)

        grid_lines = VGroup()
        v = rectangle.get_vertices()
        grid_xstep = 1
        grid_ystep = 1
        countx = width / grid_xstep

        gridx = VGroup(
            *(
                Line(
                    v[1] + i * grid_xstep * RIGHT,
                    v[1] + i * grid_xstep * RIGHT + height * DOWN,
                    stroke_color = color,
                    stroke_width = 1,
                    stroke_opacity = 1,
                    shade_in_3d = True,
                )
                for i in range(1, int(countx))
            )
        )

        grid_lines.add(gridx)

        county = height / grid_ystep
        gridy = VGroup(
            *(
                Line(
                    v[1] + i * grid_xstep * DOWN,
                    v[1] + i * grid_xstep * DOWN + width * RIGHT,
                    stroke_color = color,
                    stroke_width = 1,
                    stroke_opacity = 1,
                    shade_in_3d = True,
                )
                for i in range(1, int(county))
            )
        )

        grid_lines.add(gridy)
        
        self.add(grid_lines)
        self.add(rectangle)