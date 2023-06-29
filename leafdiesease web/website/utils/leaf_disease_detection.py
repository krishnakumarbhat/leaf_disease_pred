import tensorflow as tf

def detect_leaf_disease(image_path, model_path):
    # Load the model
    model = tf.keras.models.load_model(model_path)

    # Preprocess the image
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array /= 255.0

    # Make the prediction
    prediction = model.predict(img_array)

    # Retrieve the predicted class
    predicted_class = tf.argmax(prediction[0]).numpy()

    # Return the predicted class (you can modify this part based on your use case)
    return predicted_class

# import tensorflow as tf
# import numpy as np

# def detect_leaf_disease(image_path, model_path):
#     # Load the model
#     model = tf.keras.models.load_model(model_path)

#     # Preprocess the image
#     img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
#     img_array = tf.keras.preprocessing.image.img_to_array(img)
#     img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
#     img_array = np.expand_dims(img_array, axis=0)

#     # Make the prediction
#     prediction = model.predict(img_array)

#     # Retrieve the predicted class
#     predicted_class = tf.argmax(prediction[0]).numpy()

#     # Return the predicted class (you can modify this part based on your use case)
#     return predicted_class
