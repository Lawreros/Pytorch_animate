from manim import *
from layers.Input import Input


class NeuralNetwork(Group):
    """Class for representing an entire neural network"""
    def __init__(self,
                 layer_list: List[VGroup],
                 layer_spacing:float = 0.2,
                 debug_mode:bool = False):
        
        super().__init__()
        self.layer_spacing = layer_spacing
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

        self._position_layers()

        self.add(VGroup(*self.layer_list))
            

    def _position_layers(self):
        """positions the layers in the scene"""
        for i, layer in enumerate(self.layer_list):
            if i == 0:
                layer.move_to(ORIGIN - [5, 0, 0])
            else:
                layer.next_to(self.layer_list[i-1], RIGHT, buff=self.layer_spacing)
        

    def make_forward_pass_animation(self):
        """runs the forward_pass method for each layer and aggregates
        a list of animations for each layer"""
        animations = []
        for layer in self.layer_list:
            if isinstance(layer, Input): # TODO: Make a global list of layers without animations
                continue
            else:
                animations.extend(layer.forward_pass())

        return animations  
