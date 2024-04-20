from manim import *
from ..utils.shapes.conv_shapes import FeatureMap, GriddedRectangle

class Conv2d(VGroup):

    def __init__(self,
                 in_channels,
                 out_channels,
                 height=4,
                 width=5,
                 **kwargs):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.height = height
        self.width = width


    def _construct(self, prev_layer = None) -> VGroup:
        """Constructs the layers of the Conv2d module"""
        # prev_layer = the previous layer that the current layer is connected to

        # Store the previous layer for future reference in the animations
        self.prev_layer = prev_layer

        # Construct feature map
        fm = FeatureMap(self.in_channels, self.height, self.width)

        # Create gridded rectangle for animation
        gr = GriddedRectangle(height=self.height, width=self.width)
    

    def forward_pass(self) -> AnimationGroup:
        """Runs the forward pass of the Conv2d module"""
