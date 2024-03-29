import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# from tensorflow.keras.utils import to_categorical
# tf.keras.utils.to_categorical


(xtrain, ytrain), (xtest, ytest) = tf.keras.datasets.cifar10.load_data()
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
print(xtrain.shape)

# chuẩn hóa dữ liệu
xtrain, xtest = xtrain/255, xtest/255 # những data của ytrain thuộc dạng nhãn

ytrain_ohc, ytest_ohc = tf.keras.utils.to_categorical(ytrain), tf.keras.utils.to_categorical(ytest)
# => phải chuẩn hóa dữ liệu sang one hot coding :
# 0000000000, 100000000, 0001000000, ... 10 số 0

# mạng fully connected
model_training_first = tf.keras.models.Sequential([
    # lan 1
    tf.keras.layers.Conv2D(32, (3,3), input_shape=(64,64,3), activation='relu'),
    tf.keras.layers.MaxPool2D((32,32)),
    # tf.keras.layers.Dropout(0.15),

    # lan 2
    tf.keras.layers.Conv2D(64, (3,3), input_shape=(32,32,3), activation='relu'),
    tf.keras.layers.MaxPool2D((16,16)),
    # tf.keras.layers.Dropout(0.20),

    # lan 3
    tf.keras.layers.Conv2D(128, (3,3), input_shape=(32,32,3), activation='relu'),
    # tf.keras.layers.MaxPool2D((16,16)),
    # tf.keras.layers.Dropout(0.2),

    # tf.keras.layers.Flatten(input_shape=(32,32,3)),# 32 x 32 x 3 = 3072
    tf.keras.layers.Flatten(input_shape=(64,64,8)),
    # tf.keras.layers.Dense(1000, activation='relu'),# tạo lưới 3000 node
    tf.keras.layers.Dense(128, activation='relu'),# tạo lưới 3000 node
    tf.keras.layers.Dense(10, activation='softmax')# tạo lưới 3000 node
])

# tổng hợp
model_training_first.summary()

# # compile model
# # SGD = stochastic gradient decent
# # adam
# model_training_first.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])
#
# # train model
# model_training_first.fit(xtrain, ytrain, epochs=10)
#
# # save model => để có chạy lại hông cần train nữa chỉ cần log ra chạy luôn    
# model_training_first.save('model-cifar10.h5')



# models = tf.keras.models.load_model('model-cifar10.h5')

# pred = models.predict(xtest[105].reshape((-1,32,32,3)))
# print(classes[np.argmax(pred)])
# plt.imshow(xtest[105])
# plt.show()

# np.random.shuffle(xtest)
#
# for i in range(50):
#     plt.subplot(10, 10, i+1)
#     plt.imshow(xtest[i])
#     pred = models.predict(xtest[i].reshape((-1, 32, 32, 3)))
#     plt.title(classes[np.argmax(pred)])
#     plt.axis('off')
# plt.show()


# models = tf.keras.models.load_model('model-cifar10.h5')
# acc = 0
# for i in range(100):
#     plt.subplot(10, 10, i+1)
#     plt.imshow(xtest[500+i])
#     if (np.argmax(models.predict(xtest[500+i].reshape((-1, 32, 32, 3)))) == ytest[500+i][0]):
#         acc += 1
#     plt.title(classes[np.argmax(models.predict(xtest[i].reshape((-1, 32, 32, 3))))])
#     plt.axis('off')
# plt.show()
# print(acc)



"""
    điều kiện 1:
        để tính cross entropy => thì phải có hàm trả về kiểu xác suất
        => đó chính là activation: 'soft max'
    điều kiện 2: dự đoán được cái vị trí trong kết quả xác suất của mình 
            cái số nào ở ví trí lớn nhất so sánh với vị trí thật sự của nó
            => để biết hình mình đúng hay hình mình sai
"""
