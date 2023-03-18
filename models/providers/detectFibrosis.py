from .functions.load_image import load_image_as_tensor
# from .functions.ResNet34 import Resnet34
from .functions.Googlenet import googlenet
from .functions.preprocess import preprocess
import sys
import os
import torch
# import tensorflow as tf


def detectFibrosis(img_path):
    img = load_image_as_tensor(img_path)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    if not hasattr(sys.modules['__main__'], 'googlenet'):
        sys.modules['__main__'].googlenet = googlenet
    model = torch.load('models/savedModels/detection/googlenet.pt',
                       map_location=torch.device('cpu'))
    yb = model(img.unsqueeze(0))
    _, preds = torch.max(yb, dim=1)
    return preds[0].item()


def predict(model, img):
    # print(type(img))
    img = preprocess(img)
    yb = model(img)
    _, preds = torch.max(yb, dim=1)
    # print(yb, preds, torch.max(yb, dim=1))
    return preds[0].item() == 0
