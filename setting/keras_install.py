# conda install keras

import keras
from keras import backend as K

print("keras_version",keras.__version__)
print(K.tensorflow_backend._get_available_gpus()[0])
