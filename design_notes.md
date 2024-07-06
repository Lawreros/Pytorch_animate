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


## Development Plan:
### Pipeline v0.0:
- [ ] Add forward pass animation to conv2d model
- [ ] Add ability to customize input layer
- [ ] Add MaxPooling2DLayer
- [ ] Complete forward pass animation for simple CNN

### Pipeline v0.1:
- [ ] Add MLP support
    - [ ] Add FeedForwardLayer
    - [ ] Add FeedForward animation
    - [ ] Add conv layer to MLP animation
    - [ ] Add dropout support
- [ ] Flesh out layer positioning
- [ ] Standardize layer attributes

### Pipeline v0.2:
- [ ] Add activation function support
- [ ] Add batch/layer/instance normalization support
- [ ] Add customization options (color, speed, etc.)

### Pipeline v0.3:
- [ ] Add layer addition support
- [ ] Add model compression support (replacing chunks of model with shapes / black boxes)