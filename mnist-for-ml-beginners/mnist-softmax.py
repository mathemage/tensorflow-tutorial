import tensorflow as tf

# data
from tensorflow.examples.tutorials.mnist import input_data
# TODO include MNIST_data/ to Git due to mailfucntioning MNIST URL
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# declarations
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
weighted_output = tf.matmul(x, W) + b
y = tf.nn.softmax(weighted_output)          # softmax regression
y_ = tf.placeholder(tf.float32, [None, 10])
# cross_entropy_custom = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=1))
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=weighted_output)
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# training
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# evaluation
correct_predictions = tf.equal(tf.argmax(y,1), tf.arg_max(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
