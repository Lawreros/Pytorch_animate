from manim import *
from utils.shapes.conv_shapes import FeatureMap, GriddedRectangle

class Conv2d(VGroup):

    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                 **kwargs):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size


    def _construct(self, prev_layer = None) -> VGroup:
        """Constructs the layers of the Conv2d module"""
        # prev_layer = the previous layer that the current layer is connected to

        # Store the previous layer for future reference in the animations
        self.prev_layer = prev_layer

        # Calculate size of the current layer
        self._calculate_size()

        # Construct feature map
        fm = FeatureMap(self.out_channels, self._height, self._width)
        
        fm = fm.rotate(about_point=fm.get_center(), axis=[0.02, 1, 0], angle=75*DEGREES)

        self.add(fm)

    def _calculate_size(self):
        """Calculates the size of the current layer based on the previous layer + kernel size"""
        self._height = self.prev_layer._height - self.kernel_size + 1
        self._width = self.prev_layer._width - self.kernel_size + 1


    def make_conv_kernel(self):
        
        # Kernels that are applied to previous layer
        grid_recs = []
        for i in self.prev_layer.submobjects:
            grid_rec = GriddedRectangle(height=self.kernel_size, width=self.kernel_size)
            grid_rec.rotate(about_point=i.get_center(), axis=[0.02, 1, 0], angle=75*DEGREES)
            grid_rec.align_to(i.points[4], direction=UL)

            grid_recs.append(grid_rec)


        # Output of convolution
        out_recs = []
        for i in self.submobjects[0].submobjects: # TODO: Get a better way of getting info about featuremap
            out_rec = GriddedRectangle(height=1, width=1)
            out_rec.rotate(about_point=i.get_center(), axis=[0.02, 1, 0], angle=75*DEGREES)
            out_rec.align_to(i.points[4], direction=UL)
            
            out_recs.append(out_rec)

        return self.make_connection_lines(grid_recs, out_recs)


    @staticmethod
    def make_connection_lines(grid_recs, out_recs=None):
        """Takes the grid rectangles from the previous layer and the current layer and connects them with lines"""
        lines = []
        
        for i in [UL, UR, DL, DR]:
            for j in range(1,len(grid_recs)):
                line = Line(grid_recs[j].get_corner(i), grid_recs[j-1].get_corner(i),
                            stroke_color=ORANGE,
                            stroke_width=10,
                            stroke_opacity = 1)
                lines.append(line)

        if out_recs:
            for i in [UL, UR, DL, DR]:
                for j in range(1,len(out_recs)):
                    line = Line(out_recs[j].get_corner(i), out_recs[j-1].get_corner(i),
                                stroke_color=ORANGE,
                                stroke_width=5,
                                stroke_opacity = 0)
                    lines.append(line)

                line = Line(grid_recs[0].get_corner(i), out_recs[-1].get_corner(i),
                            stroke_color=ORANGE,
                            stroke_width=5,
                            stroke_opacity = 1)
                lines.append(line)


        return VGroup(VGroup(*lines), VGroup(*grid_recs), VGroup(*out_recs))


    def forward_pass(self) -> AnimationGroup:
        """Runs the forward pass of the Conv2d module"""
        kernel_vgroup = self.make_conv_kernel()

        return AnimationGroup(FadeIn(kernel_vgroup))
