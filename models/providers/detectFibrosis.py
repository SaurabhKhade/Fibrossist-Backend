from .functions.load_image import load_image
from .functions.predict import predict
from .functions.ResNet34 import Resnet34
import sys
import torch

def detectFibrosis(dir_path):
    img = load_image(dir_path)
    if not hasattr(sys.modules['__main__'], 'Resnet34'):
        sys.modules['__main__'].Resnet34 = Resnet34
    model = torch.load('models/savedModels/detection/model.pt', map_location=torch.device('cpu'))
    return predict(model, img)