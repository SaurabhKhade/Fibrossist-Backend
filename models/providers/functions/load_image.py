import torchvision.transforms as tt
from PIL import Image
from torchvision.datasets import ImageFolder

transform = tt.Compose([   
    tt.Resize(size=(150,150)),
    tt.ToTensor(),
])

def load_image(dir_path):
    test_ds = ImageFolder(dir_path,transform)
    return test_ds[0][0]
