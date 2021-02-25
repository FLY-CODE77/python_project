# install gpu version
# conda install tensorflow-gpu

# which version check

import tensorflow as tf
print('tf version:', tf.__version__)

# gpu setting check
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
