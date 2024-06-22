from manim import *


class NeuralNetwork(Group):
    """Class for representing an entire neural network"""
    def __init__(self,
                 layer_list: List[VGroup],
                 layer_spacing:float = 0.2,
                 debug_mode:bool = False):
        
        super().__init__()
        self.layer_list = layer_list
        self._construct_layers()


    
    def _construct_layers(self):
        """runs the construct method from each layer provided
        also handles the spacing between layers"""
        for i, (prev_layer, layer) in enumerate(zip([None, *(self.layer_list)], self.layer_list)):
            if i == 0:
                layer._construct()
            else:
                layer._construct(prev_layer = prev_layer)

        self.add(VGroup(*self.layer_list))
            

    def make_forward_pass_animation(self):
        """runs the forward_pass method for each layer and aggregates
        a list of animations for each layer"""
        animations = []
        for layer in self.layer_list:
            animations.append(layer.forward_pass())

        return AnimationGroup(*animations)

    
