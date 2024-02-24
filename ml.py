import tensorflow as tf
import keras
import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers.experimental import preprocessing

train_dir = r"C:\5th sem\reasearch\1st internal\2nd internals\retina.csv"
val_dir = r"C:\5th sem\reasearch\1st internal\2nd internals\retina.csv"
test_dir = r"C:\5th sem\reasearch\1st internal\2nd internals\retina.csv"

IMAGE_SIZE = (100,100)
trainDataAll = tf.keras.preprocessing.image_dataset_from_directory (train_dir ,label_mode = "categorical",image_size = IMAGE_SIZE,    shuffle = True )



valDataALL = tf.keras.preprocessing.image_dataset_from_directory(val_dir,label_mode = "categorical",image_size = IMAGE_SIZE,shuffle = False)

testDataALL = tf.keras.preprocessing.image_dataset_from_directory(test_dir,label_mode = "categorical",image_size = IMAGE_SIZE,shuffle = False)

data_augmentation = Sequential([
    preprocessing.RandomFlip("horizontal"),
    preprocessing.RandomRotation(0.2),
    preprocessing.RandomHeight(0.2),
    preprocessing.RandomWidth(0.2),
    preprocessing.RandomZoom(0.2),
    preprocessing.Rescaling(1. /255)
])


y_val_labels = []
for images, labels in valDataALL.unbatch(): 
    y_val_labels.append(labels.numpy().argmax()) 

    y_test_labels = []
for images, labels in testDataALL.unbatch():
    y_test_labels.append(labels.numpy().argmax()) 

    class_names = testDataALL.class_names
class_names

