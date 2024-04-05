import os
import cv2
from random import shuffle
import pickle

data_and_labels = []
data = []
labels = []

object_folders = os.listdir('rgbd-dataset')

object = 0

if '.DS_Store' in object_folders: 
  object_folders.remove('.DS_Store')
for folder in object_folders:
  object+=1
  print(object)
  object_path = os.path.join('rgbd-dataset', folder)
  
  each_object_folders = os.listdir(object_path)
  
  if '.DS_Store' in each_object_folders: 
    each_object_folders.remove('.DS_Store')
    
  for each_object_folder in each_object_folders:
    each_object_path = os.path.join(object_path, each_object_folder)
    
    image_files = os.listdir(each_object_path)
        
    colour_images = [img for img in image_files if img.endswith("_crop.png")]
    
    for img_file in colour_images:
      image_path = os.path.join(each_object_path, img_file)
      
      img = cv2.imread(image_path)
      
      data_and_labels.append((img, folder))
      
shuffle(data_and_labels)

for each in data_and_labels:
  data.append(each[0])
  labels.append(each[1])

data = [cv2.resize(image, (64, 64)) for image in data]
  
with open('data.pkl', 'wb') as f:
  pickle.dump(data, f)
  
with open('labels.pkl', 'wb') as f:
  pickle.dump(labels, f)

