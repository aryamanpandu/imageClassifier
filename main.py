import tensorflow as tf
import os
 
# sess = tf.Session();
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices());