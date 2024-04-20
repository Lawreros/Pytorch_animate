from manim import Scene
from ..neural_network.neural_network import NeuralNetwork
from ..layers.Conv2d import Conv2d
import os


class example_scene(Scene):

    def construct(self):
        nn = NeuralNetwork(
            layers=[
                Conv2d(in_channels=1, out_channels=3, kernel_size=3),
                Conv2d(in_channels=3, out_channels=5, kernel_size=3)
            ]
        )

        self.add(nn)

        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation()
        
        # Play animation
        self.play(forward_pass)

# run command line from string
command = f"manim -pql CNN.py"
os.system(command)
