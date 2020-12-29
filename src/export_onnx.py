from pathlib import Path as _P
import os, sys
import torch
import io
import numpy as np

from torch import nn
import torch.utils.model_zoo as model_zoo
import torch.onnx

ROOT = _P(os.path.abspath(__file__)).parents[1]
celeb = ROOT / "celeba-hq_models"
gen_model_path = celeb / "InpaintingModel_gen.pth"

# Load pretrained model weights
# model_url = 'https://s3.amazonaws.com/pytorch/test_data/export/superres_epoch100-44c6958e.pth'
batch_size = 1    # just a random number

# Initialize model with the pretrained weights
map_location = lambda storage, loc: storage
if torch.cuda.is_available():
    map_location = None
torch_model.load_state_dict(model_zoo.load_url(gen_model_path, map_location=map_location))

# set the model to inference mode
torch_model.eval()

