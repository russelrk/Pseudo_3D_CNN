import torch
import torch.nn as nn
import torchvision.models as models


def resnet18_x(in_channels):
  # Load pre-trained ResNet-18 model
  pretrained_resnet = models.resnet18(weights="DEFAULT")
  
  # Define the number of desired input channels for the modified model
  x = in_channels  # Change this to the desired number of input channels
  
  # Modify the original model's first convolutional layer with the desired number of input channels
  modified_resnet = models.resnet18(weights="DEFAULT")
  modified_resnet.conv1 = nn.Conv2d(x, 64, kernel_size=7, stride=2, padding=3, bias=False)
  
  
  with torch.no_grad():
      for i in range(x):
          # Copy weights from the first channel of the original model's first convolutional layer to all channels in the modified layer
          modified_resnet.conv1.weight[:, i, :, :].copy_(pretrained_resnet.conv1.weight[:, 0, :, :])
  
  return modified_resnet
