#session会话学习
import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],[2]])
product = tf.matmul(matrix1,matrix2)
#matrix multiply np.dot(m1,m2)
#method 1 
# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True

# sess = tf.Session(config=config)
# result = sess.run(product)
# print(result)
# sess.close()

#method 2
config = tf.ConfigProto()
config.gpu_options.allow_growth = True

with tf.Session(config=config) as sess:
    result=sess.run(product)
    print(result)