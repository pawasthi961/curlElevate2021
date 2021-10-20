import numpy as np
from matplotlib import pyplot as plt
from torchvision import datasets, transforms
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
# model runs on GPU if available
device = ("cuda" if torch.cuda.is_available() else "cpu")
