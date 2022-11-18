import torch

def preprocess(image):
    device = getDevice()
    image = to_device(image.unsqueeze(0),device)
    return image

def to_device(data, device):
    if isinstance(data, (list,tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)
    # print(data)
    # return data
    
def getDevice():
    if torch.cuda.is_available():
        return torch.device('cuda')
    else:
        return torch.device('cpu')