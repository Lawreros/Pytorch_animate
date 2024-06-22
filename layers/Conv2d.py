from manim import *
from utils.shapes.conv_shapes import FeatureMap, GriddedRectangle

class Conv2d(VGroup):

    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                #  height=4,
                #  width=5,
                 **kwargs):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        # self.height = height
        # self.width = width


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

        # Create gridded rectangle for animation
        gr = GriddedRectangle(height=self.kernel_size, width=self.kernel_size)

    def _calculate_size(self):
        """Calculates the size of the current layer based on the previous layer + kernel size"""
        self._height = self.prev_layer.height - self.kernel_size + 1
        self._width = self.prev_layer.width - self.kernel_size + 1

    def forward_pass(self) -> AnimationGroup:
        """Runs the forward pass of the Conv2d module"""
