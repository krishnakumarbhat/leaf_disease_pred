import numpy as np
from tensorflow.keras.preprocessing import image

def detect_leaf_disease(image_path, model):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image

    # Use the loaded model to make predictions
    prediction = model.predict(img_array)
    # Perform any post-processing or formatting of the prediction as required

    return prediction
