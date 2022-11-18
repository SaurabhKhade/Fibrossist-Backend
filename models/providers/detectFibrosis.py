from .functions.load_image import load_image_as_tensor
from .functions.ResNet34 import Resnet34
from .functions.preprocess import preprocess
import sys
import torch
import tensorflow as tf


def detectFibrosis(img_path):
    img = load_image_as_tensor(img_path)
    if not hasattr(sys.modules['__main__'], 'Resnet34'):
        sys.modules['__main__'].Resnet34 = Resnet34
    model = torch.load('models/savedModels/detection/model.pt', map_location=torch.device('cpu'))
    return predict(model, img)

def predict(model, img):
    print(type(img))
    img = preprocess(img)
    yb = model(img)
    _, preds  = torch.max(yb, dim=1)
    print(yb,preds,torch.max(yb, dim=1))
    return preds[0].item() == 0