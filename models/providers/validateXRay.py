from .functions.load_image import load_image
from keras.models import model_from_json
import numpy as np 

def validateXRay(img_file):
    img = load_image(img_file)
    with open('models/savedModels/validation/model.json', 'r') as json_file:
        loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)
    model.load_weights('models/savedModels/validation/model.h5')
    model.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])
    pred = model.predict(img)

    return np.argmax(pred)