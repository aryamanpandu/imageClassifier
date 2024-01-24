import tensorflow as tf
import os
import cv2 #import this to remove dodgy (corrupted images, not able to open on python images, incorrect extension images)
from matplotlib import pyplot as plt
 
# Avoid out of memory errors by setting GPU Memory Consumption Growth
#This block of code is only useful for computers using tensorflow gpu
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu,True)



data_dir = 'data'
image_exts = ['.jpeg', '.jpg', '.bmp', '.png'] #common image extensions

os.listdir(os.path.join(data_dir,'happy_people_dataset'))
#Remember to get rid of all the weird really small images as they are probably not relevant

#block of code to remove all the weird images which are not supported
for folder in os.listdir(data_dir): 
    for image in os.listdir(os.path.join(data_dir,folder)): 
        image_path = os.path.join(data_dir,folder,image) 
        try:
            img = cv2.imread(image_path) #checking if the image file is supported. You can also use img.shape to see (rows[height],columns[width],no_of_channels)
            file_name_ext_tuple = os.path.splitext(image_path) 
            file_ext = file_name_ext_tuple[1]
            if len(img) == 0:
                print('Image not in extension list {}'.format(image_path))
                os.remove(image_path)
            if file_ext not in image_exts: #second check to see if the file extension is supported
                print('Image not in extension list {}'.format(image_path))
                os.remove(image_path) #function to remove the image if is not supported

        except Exception as e:
            print('Issue with image {}'.format(image_path))
