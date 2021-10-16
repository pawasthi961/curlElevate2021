import numpy as np
import matplotlib.pyplot as plt
import random
import tensorflow as tf
import io


fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images/255.0
test_images = test_images/255.0

def plot_value_array(i,predictions_array,true_label):

  #plt.xticks(range(10))
  #plt.yticks([])
  plt.ylim([0,1])
  barplot = plt.bar(class_names,predictions_array,color="#FFFFFF")
  plt.xticks(rotation =45)
  predicted_label = np.argmax(predictions_array)
  barplot[true_label].set_color('blue')
  barplot[predicted_label].set_color('red')
  print('Predicted Label = ',predicted_label)
  print('True Label = ',true_label)
  
def test():
  mp = tf.keras.models.load_model("backend_flask/mnist_model")
  test_loss,test_acc = mp.evaluate(test_images,test_labels)
  #Returns predictions as a probability Distribution
  prob_dist_model = tf.keras.Sequential([mp,tf.keras.layers.Softmax()])

  predictions = prob_dist_model.predict(test_images)
  plt.grid(False)
  i = random.randint(0,10) 
  plt.figure(figsize = (10,3))
  plt.subplot(1,2,1)
  plt.imshow(test_images[i],cmap = plt.cm.binary)
  plt.xlabel("{} ({})".format(class_names[np.argmax(predictions[i])],class_names[test_labels[i]]))
  plt.subplot(1,2,2)
  plot_value_array(i,predictions[i],test_labels[i])

  bytes_image = io.BytesIO()
  plt.savefig(bytes_image, format='png')
  bytes_image.seek(0)
  print(i)

  confidence = 100*np.max(predictions[i])
  print('Confidence % = ',confidence)
  return [bytes_image,confidence]
  