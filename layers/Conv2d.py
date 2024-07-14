from manim import *
from utils.shapes.conv_shapes import FeatureMap, GriddedRectangle

class Conv2d(VGroup):

    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                 padding = 0,
                 **kwargs):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.padding = padding


    def _construct(self, prev_layer = None) -> VGroup:
        """Constructs the layers of the Conv2d module"""
        # prev_layer = the previous layer that the current layer is connected to

        # Store the previous layer for future reference in the animations
        self.prev_layer = prev_layer

        # Calculate size of the current layer
        self._calculate_size()

        # Construct feature map
        fm = FeatureMap(self.out_channels, self._height, self._width)

        self.ancs = fm.ancs

        self.add(fm)
        self.add(self.ancs)

    @property
    def surface_ancs(self):
        return self.ancs.submobjects[-1]

    def _calculate_size(self):
        """Calculates the size of the current layer based on the previous layer + kernel size"""
        self._height = self.prev_layer._height - self.kernel_size + 1
        self._width = self.prev_layer._width - self.kernel_size + 1


    def make_conv_kernel(self, layer_num: int = 0) -> VGroup:
        
        # Kernels that are applied to previous layer
        grid_recs = VGroup()
        for i in self.prev_layer.ancs:
            grid_rec = GriddedRectangle(height=self.kernel_size, width=self.kernel_size)
            grid_rec.rotate(about_point=grid_rec.get_center(), axis=[0.02, 1, 0], angle=75*DEGREES)
            grid_rec.align_to(i[0], direction=UL)


            grid_recs.add(grid_rec)


        # Output of convolution
        out_recs = VGroup()
        i = self.ancs[layer_num]
        out_rec = GriddedRectangle(height=1, width=1)
        out_rec.rotate(about_point=out_rec.get_center(), axis=[0.02, 1, 0], angle=75*DEGREES)
        out_rec.align_to(i, direction=UL)
            
        out_recs.add(out_rec)

        return self.make_connection_lines(grid_recs, out_recs)
    
    def make_conv_animation(self, kernel_vgroup):
        """Create the animation of a kernel passing over the previous layer"""

        animations = []

        # Vector for moving from the left of the layer to the right
        l_r_move_vector = (self.prev_layer.surface_ancs[1].get_center() - self.prev_layer.surface_ancs[0].get_center()) \
            - (kernel_vgroup.submobjects[0][-1].ancs[1].get_center() - kernel_vgroup.submobjects[0][-1].ancs[0].get_center())

        u_d_move_vector = (self.prev_layer.surface_ancs[2].get_center() - self.prev_layer.surface_ancs[0].get_center()) / self.prev_layer._height

        iterations = self.prev_layer._height - self.kernel_size + 1
        for i in range(iterations-1):
            animations.append(ApplyMethod(kernel_vgroup.shift, l_r_move_vector))
            animations.append(ApplyMethod(kernel_vgroup.shift, u_d_move_vector + -l_r_move_vector))
        else:
            animations.append(ApplyMethod(kernel_vgroup.shift, l_r_move_vector))

        return animations


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

                line = Line(grid_recs[-1].get_corner(i), out_recs[-1].get_corner(i),
                            stroke_color=ORANGE,
                            stroke_width=5,
                            stroke_opacity = 1)
                lines.append(line)


        return VGroup(grid_recs, out_recs, VGroup(*lines))


    def forward_pass(self) -> AnimationGroup:
        """Runs the forward pass of the Conv2d module"""

        animations = []

        if self.padding:
            raise NotImplementedError("Padding not yet implemented")
            

        # Iterate through the convolution once for each output channel
        for i in range(self.out_channels):
            kernel_vgroup = self.make_conv_kernel(layer_num=i)
            animations.append(FadeIn(kernel_vgroup))
            animations.append(Wait(0.5))
            animations.extend(self.make_conv_animation(kernel_vgroup))
            animations.append(FadeOut(kernel_vgroup))

        return animations
