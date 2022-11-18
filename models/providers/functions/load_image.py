from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from torchvision import transforms


def load_image(img_file):
    img = image.load_img(img_file, target_size=(224,224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

def load_image_as_tensor(img_file):
    img = Image.open(img_file)
    img = img.convert('RGB')
    img = img.resize((150,150))
    img = transforms.ToTensor()(img)
    return img
