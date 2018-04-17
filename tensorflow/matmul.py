import tensorflow as tf

matrix1 = tf.constant([[2.,3.]])

matrix2 = tf.constant([[2.],[1.]])

product = tf.matmul(matrix1,matrix2)

with tf.Session() as sess:
	result = sess.run(product)
	print(result)