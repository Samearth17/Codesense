"""Implement a random forest classifier in Python using TensorFlow"""

import tensorflow as tf
from tensorflow.contrib.tensor_forest.python import tensor_forest

# Parameters
num_classes = 2  # binary classification
num_features = 14
total_samples = 4500
num_trees = 8
max_nodes = 10

# Building the Random Forest
# Input and Target data
X = tf.placeholder(tf.float32, shape=[None, num_features])
Y = tf.placeholder(tf.int32, shape=[None])

# Random Forest Parameters
hparams = tensor_forest.ForestHParams(num_classes=num_classes, num_features=num_features, num_trees=num_trees, max_nodes=max_nodes).fill()

# Build the Random Forest
forest_graph = tensor_forest.RandomForestGraphs(hparams)
# Get training graph and loss
train_op = forest_graph.training_graph(X, Y)
loss_op = forest_graph.training_loss(X, Y)

# Measure the accuracy
infer_op, _, _ = forest_graph.inference_graph(X)
correct_prediction = tf.equal(tf.argmax(infer_op, 1), tf.cast(Y, tf.int64))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Initialize the variables (i.e. assign their default value)
init_vars = tf.group(tf.global_variables_initializer(), resources.initialize_resources(resources.shared_resources()))

# Run the session
with tf.Session() as sess:
    # Run the initializer
    sess.run(init_vars)
    # Training
    for i in range(1000):
        # Get next batch
        batch_x, batch_y = get_batch_data(total_samples, batch_size)
        _, l = sess.run([train_op, loss_op], feed_dict={X: batch_x, Y: batch_y})
    # Test Model
    test_x, test_y = get_batch_data(total_samples, batch_size)
    accuracy = sess.run(accuracy_op, feed_dict={X: test_x, Y: test_y})