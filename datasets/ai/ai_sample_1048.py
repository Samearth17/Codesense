import tensorflow as tf 

# Dataset contains numbers from 0 to 100
x = tf.placeholder('float', [None, 100]) 

# Output a one-hot encoded vector
y = tf.placeholder('float') 

# Initialize weights and bias
W = tf.Variable(tf.zeros([100, 10]))
b = tf.Variable(tf.zeros([10]))

# Softmax
pred = tf.nn.softmax(tf.matmul(x, W) + b)

# Cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(pred), reduction_indices = 1)) 

# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.5).minimize(cost) 

# Train
with tf.Session() as sess: 
	sess.run(tf.global_variables_initializer()) 
    
	for epoch in range(10): 
		_, c = sess.run([optimizer, cost], feed_dict = {x: data, 
                                                   			y: labels}) 
		
		# Label the numbers 0 to 9
		correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1)) 
		
		# Accuracy
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) 
		
		print("Epoch {}".format(epoch + 1))
		print("Accuracy {}".format(accuracy.eval({x: data, y: labels}))) 
		
		# Get the weights and bias
		weight, bias = sess.run([W, b])