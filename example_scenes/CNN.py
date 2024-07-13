from manim import Scene, Circle, VGroup, Rectangle, BLUE
from neural_network.neural_network import NeuralNetwork
from layers.Conv2d import Conv2d
from layers.Input import Input
import os


class example_scene(Scene):

    def construct(self):
        nn = NeuralNetwork(
            layer_list=[
                Input(channels=3, width=5, height=5),
                Conv2d(in_channels=1, out_channels=3, kernel_size=3),
                Conv2d(in_channels=3, out_channels=2, kernel_size=2)
            ]
        )

        self.add(nn)

        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation()
        
        # Play animation
        for i in forward_pass:
            self.play(i)
        # self.play(forward_pass)

# run command line from string
if __name__ == "__main__":
    # command = f"manim -pql /manim/Pytorch_animate/example_scenes/CNN.py example_scene"
    # os.system(command)

    example_scene().construct()
