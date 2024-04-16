# Design Notes for Layer Objects
Here's where I'll be recording my thinking about the requirements related to the creation of this repo.

## Class Reuirements:
- Each class should be self contained with respect to its animations
- Each class should be able to be queried for its important geometric information:
    - layer dimensions
    - Whether it is a feature map, as collection of nodes, or a unique shape
- Have visible elements stored in a list for easy access by the proceeding step in the animation

## ML Layer Types:
Different layers I'd like to support:
- Convolutional layer
- MLP

## Layer Mutations/Calculations:
- Padding
- Upsampling
- MaxPooling
- Addition
