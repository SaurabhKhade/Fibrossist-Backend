import torch
from .preprocess import preprocess

def predict(model, img):
    img = preprocess(img)
    yb = model(img)
    _, preds  = torch.max(yb, dim=1)
    print(yb,preds,torch.max(yb, dim=1))
    return preds[0].item() == 0