def generate_predictions(test_image_path, actual_label):

  import numpy as np
  import matplotlib.pyplot as plt
  import tensorflow as tf
  from tensorflow import keras
  from keras.preprocessing.image import ImageDataGenerator
  import warnings
  import cv2 as cv
  warnings.filterwarnings('ignore')

  #Loading the trained cnn model
  model = tf.keras.models.load_model('train_classification.h5')

  # Testing the Model
  #test_image_path = ('Resources\potato.jpg')
 
  #Load and preprocess the image
  test_imge  = test_image_path
  test_img = cv.resize(test_imge,(150,150))
  #test_img = keras.utils.load_img(test_image_path, target_size=(150, 150))
  test_img_arr = keras.utils.img_to_array(test_img)/255.0
  test_img_input = test_img_arr.reshape((1, test_img_arr.shape[0], test_img_arr.shape[1], test_img_arr.shape[2]))

  #Make Predictions
  predicted_label = np.argmax(model.predict(test_img_input))
  class_map = {0: 'Bean', 1: 'Bitter_Gourd', 2: 'Bottle_Gourd', 3: 'Brinjal', 4: 'Broccoli', 
                5: 'Cabbage', 6: 'Capsicum', 7: 'Carrot', 8: 'Cauliflower', 9: 'Cucumber', 
                10: 'Papaya', 11: 'Potato', 12: 'Pumpkin', 13: 'Radish', 14: 'Tomato'}

  predicted_vegetable = class_map[predicted_label]
  '''plt.figure(figsize=(4, 4))
  plt.imshow(test_img_arr)
  plt.title("Predicted: {}, Needed: {}".format(predicted_vegetable, actual_label))
  plt.grid()
  plt.axis('off')
  plt.show()'''

  if predicted_vegetable == actual_label:
    print('Potato Identified !! ')
    print('Proceed for Segregation')
    return 1
    
  else:
    print('Warning !!')
    print('{} identified'.format(predicted_vegetable))
    return 0

    




