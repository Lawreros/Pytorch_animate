from manim import BLUE, RIGHT, DOWN, UL, UR, DL, DR
from manim import Rectangle, Line, VGroup
import numpy as np

class FeatureMap(VGroup):
    def __init__(self, num_layers, height, width):
        super().__init__()
        self.num_layers = num_layers
        self.height = height
        self.width = width

        self.ancs = np.full((num_layers, 4, 3), np.nan)
        # Define the shapes and add them to self
        for i in range(num_layers):
            rectangle = Rectangle(height=height, width=width, stroke_color=BLUE)
            rectangle.set_fill(BLUE, opacity=0.2)
            # rectangle.rotate(about_point=rectangle.get_center(),axis = [0.02, 1, 0], angle=75*DEGREES)
            rectangle.move_to([0, 0, z_lvl-(i/3)])

            self.ancs[i,:,:] = self.get_corners_of_rectangle(rectangle)
            
            self.add(rectangle)
    
    @property
    def ancs(self):
        return self.get_corners_of_rectangle(self.submobjects[self.num_layers - 1])


    @staticmethod
    def get_corners_of_rectangle(rectangle):
        
        corners = np.full((4,3), np.nan)

        for i in enumerate([UL, UR, DL, DR]):
            corners[i[0],:] = rectangle.get_corner(i[1])
        
        return corners




class GriddedRectangle(VGroup):
    """A rectangle with a grid drawn on it."""

    def __init__(self, height=3, width=3, **kwargs):
        super().__init__()
        rectangle = Rectangle(height=height, width=width,
                              stroke_color=BLUE)
        rectangle.set_fill(BLUE, opacity=0.2)

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
                    stroke_color = BLUE,
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
                    stroke_color = BLUE,
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