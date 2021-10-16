#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import pickle
import tensorflow as tf

#Loading MNIST dataset
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

#Names for Labels in the MNIST Dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#train_images.shape

#train_labels.shape

#test_images.shape

#test_labels.shape

#plt.figure()
#plt.imshow(train_images[0])
#plt.colorbar()
#plt.grid(False)

train_images = train_images/255.0
test_images = test_images/255.0

#plt.figure(figsize=(10,10))
#for i in range(25):
#  plt.subplot(5,5,i+1)
#  plt.xticks([])
#  plt.yticks([])
#  plt.grid(False)
#  plt.imshow(train_images[i],cmap = plt.cm.binary)
#  plt.xlabel(class_names[train_labels[i]])

model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(128,activation='relu'),tf.keras.layers.Dense(10)])

model.compile(optimizer='adam',loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics = ['accuracy'])

model.fit(train_images,train_labels,epochs = 50)

# model.save(mnist_model.h50)
tf.keras.models.save_model(model,"backend_flask/mnist_model")


print("done")


#returns Loss and Accuracy of the model


#predictions[0]

#np.argmax(predictions[0])

#plt.imshow(test_images[0],cmap = plt.cm.binary)

#test_labels[0]

#To plot the Prediction along with the Confidence score and the True Label
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
  mp = tf.keras.models.load_model("mnist_model")

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
  print(i)
  print('Confidence % = ',100*np.max(predictions[i]))

  return (100*np.max(predictions[i]))



#testing using index values of test_images
#i = 0
#plt.figure(figsize = (10,3))
#plt.subplot(1,2,1)
#plt.imshow(test_images[i],cmap = plt.cm.binary)
#plt.xlabel("{} ({})".format(class_names[np.argmax(predictions[i])],class_names[test_labels[i]]))
#plt.subplot(1,2,2)
#plot_value_array(i,predictions[i],test_labels[i])
#print('Confidence % = ',100*np.max(predictions[i]))

#i = 12
#plt.figure(figsize = (10,3))
#plt.subplot(1,2,1)
#plt.imshow(test_images[i],cmap = plt.cm.binary)
#plt.xlabel("{} ({})".format(class_names[np.argmax(predictions[i])],class_names[test_labels[i]]))
#plt.subplot(1,2,2)
#plot_value_array(i,predictions[i],test_labels[i])
#print('Confidence % = ',100*np.max(predictions[i]))

#i = 25
#plt.figure(figsize = (10,3))
#plt.subplot(1,2,1)
#plt.imshow(test_images[i],cmap = plt.cm.binary)
#plt.xlabel("{} ({})".format(class_names[np.argmax(predictions[i])],class_names[test_labels[i]]))
#plt.subplot(1,2,2)
#plot_value_array(i,predictions[i],test_labels[i])
#print('Confidence % = ',100*np.max(predictions[i]))



#Test the model by generating a randint



#Test the model by taking input from the user along with the plots


# i = int(input("Enter an index value in the range 0-10000"))
# plt.figure(figsize = (10,3))
# plt.subplot(1,2,1)
# plt.imshow(test_images[i],cmap = plt.cm.binary)
# plt.xlabel("{} ({})".format(class_names[np.argmax(predictions[i])],class_names[test_labels[i]]))
# plt.subplot(1,2,2)
# plot_value_array(i,predictions[i],test_labels[i])
# print(i)
# print('Confidence % = ',100*np.max(predictions[i]))

#Test the model by taking input from the user (without plots)


# i = int(input("Enter an index value in the range 0-10000"))
# plt.imshow(test_images[i],cmap = plt.cm.binary)
# predicted_label = np.argmax(predictions[i])
# print('Predicted Label :',class_names[predicted_label],'\t','True Label :',class_names[test_labels[i]])
# print('Confidence % :',100*np.max(predictions[i]))