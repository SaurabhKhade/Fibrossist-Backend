from tensorflow.keras.models import model_from_json
import cv2

def validate(img_file):
    with open('models/savedModels/validation/model.json', 'r') as json_file:
        loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)
    model.load_weights('models/savedModels/validation/model.h5')
    model.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])

    img = cv2.imread(img_file)
    img = cv2.resize(img, (224, 224))
    img = img.reshape(1, 224, 224, 3)

    pred = model.predict(img)

    return (pred > 0.5)[0]