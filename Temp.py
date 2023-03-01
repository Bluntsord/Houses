import tensorflow as tf
import numpy as np
import pandas as pd
#
# data1 = [(1, 0, 0, 0),
#         (0, 0, 1, 0),
#         (0, 1, 0, 0),
#         (0, 0, 0, 1)]
#
# data2 = data1.copy()
#
# df = pd.DataFrame(data1, columns=['Column 1', 'Column 2', 'Column 3', 'Column 4'])
# df = pd.concat([data1, data2], axis=1)
#
# def custom_activation(x):
#     return 1 if x > 0 else 0
#
# # Create a 2 layer neural network
# model = tf.keras.models.Sequential()
#
# # Input layer
# model.add(tf.keras.layers.Dense(4, input_shape=(4, 2), activation=custom_activation))
#
# # First hidden layer
# model.add(tf.keras.layers.Dense(2, activation=custom_activation))
#
# # Output layer
# model.add(tf.keras.layers.Dense(4, activation=custom_activation))
#
# weights_1 = tf.Variable([[1, 0],
#                        [1, 1],
#                        [0, 0],
#                        [0, 1]], dtype=tf.int8)
# bias_1 = tf.Variable([0, 0], dtype=tf.int8)
#
#
# weights_2 = tf.Variable([[1, 1, -1, -1],
#                        [1, 0, 1, -1]], dtype=tf.int8)
# bias_2 = tf.Variable([-1, 0, 1 , 1], dtype=tf.int8)
#
# model.layers[0].set_weights([weights_1, bias_1])
# model.layers[1].set_weights([weights_2, bias_2])
#
# model.predict(data1)