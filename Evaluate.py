# import required packages
import numpy as np
from keras.models import model_from_json
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report,ConfusionMatrixDisplay
import tensorflow as tf

# output labels
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# load json and create model
json_file = open('model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("model/emotion_model.h5")
print("Loaded model from disk")

# Initialize image data generator with rescaling
test_data_gen = ImageDataGenerator(rescale=1./255)

# Preprocess all test images
test_generator = test_data_gen.flow_from_directory(
        'data/test',
        target_size=(48, 48),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')




# doing prediction on test data

predictions = np.array([])
labels =  np.array([])

I = 0
for x, y in test_generator:
  predictions = np.concatenate([predictions, np.argmax(emotion_model.predict(x),axis=-1)])
  labels = np.concatenate([labels, np.argmax(y,axis=-1)])
  I += 1
  if I > 100:  # this if-break statement reduces the running time.
    break       
ConfusionMatrixDisplay(
    confusion_matrix=tf.math.confusion_matrix(
        labels=labels, predictions=predictions)
    .numpy(), display_labels=emotion_dict).plot(cmap=plt.cm.Blues)
plt.show()
print(tf.math.confusion_matrix(labels=labels, predictions=predictions).numpy())

print("-----------------------------")
print(classification_report(labels, predictions))
