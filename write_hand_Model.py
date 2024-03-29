
import cv2
import numpy as np
import matplotlib.pyplot as plt

# lay so dep
# np.random.seed(5)

img = cv2.imread('test_image_cnn.jpg')
img = cv2.resize(img, (200,200))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)/255 # sinh gia tri lớn phải chia để chuẩn hóa dữ liệu -> tràn bộ nhớ
# print(img_gray)

#thiet ke convolution layer
class Conv2d:
    def __init__(self, input, numOfKernel = 8, kernel_size = 3, padding=0, stride=1):
        self.input = np.pad(input, ((padding, padding),(padding, padding)), 'constant')
        self.stride = stride
        # self.height, self.width = input.shape
        self.kernel = np.random.randn(numOfKernel, kernel_size, kernel_size)
        # print(kernel)

        self.results = np.zeros((int((self.input.shape[0] - self.kernel.shape[1])/self.stride) + 1,
                                 int((self.input.shape[1] - self.kernel.shape[2])/self.stride) + 1,
                                self.kernel.shape[0]))

    # roi: region of interest
    def getROI(self):
        for row in range(int((self.input.shape[0] - self.kernel.shape[1])/self.stride) + 1):
            for col in range(int((self.input.shape[1] - self.kernel.shape[2])/self.stride) + 1):
                roi = self.input[row*self.stride: row*self.stride + self.kernel.shape[1],
                      col*self.stride: col*self.stride + self.kernel.shape[2]]
                yield row, col, roi

    # toán tích chập
    def operate(self):
        for layer in range(self.kernel.shape[0]):
            for row, col, roi in self.getROI():
              self.results[row, col, layer] = np.sum(roi * self.kernel[layer])

        return self.results

class Relu:
    def __init__(self, input):
        self.input = input
        self.results = np.zeros((self.input.shape[0],
                                 self.input.shape[1],
                                 self.input.shape[2])) # định trước vùng chứa

    def operate(self):
        for layer in range(self.input.shape[2]):
            for row in range(self.input.shape[0]):
                for col in range(self.input.shape[1]):
                    self.results[row, col, layer] = 0 if self.input[row, col, layer] < 0 else self.input[row, col, layer]

        return self.results

class LeakyRelu:
    def __init__(self, input):
        self.input = input
        self.results = np.zeros((self.input.shape[0], self.input.shape[1])) # định trước vùng chứa

    def operate(self):
        for row in range(self.input.shape[0]):
            for col in range(self.input.shape[1]):
                self.results[row, col] = 0.1*self.input[row, col] if self.input[row, col] < 0 else self.input[row, col]

        return self.results


class MaxPooling:
    def __init__(self, input, poolingSize):
        self.input = input
        self.poolingSize = poolingSize

        self.result = np.zeros((int(self.input.shape[0]/self.poolingSize),
                                int(self.input.shape[1]/self.poolingSize),
                                 self.input.shape[2]))  # định trước vùng chứa

    def operate(self):
        for layer in range(self.input.shape[2]):
            for row in range(int(self.input.shape[0]/self.poolingSize)):
                for col in range(int(self.input.shape[1]/self.poolingSize)):
                    self.result[row, col, layer] = np.max(self.input[row*self.poolingSize: row*self.poolingSize+self.poolingSize,
                        col * self.poolingSize: col * self.poolingSize + self.poolingSize, layer])

        return self.result

img_gray_conv2d = Conv2d(img_gray, 16, 3, padding=0, stride=1).operate()
img_gray_conv2d_relu = Relu(img_gray_conv2d).operate()
img_gray_conv2d_relu_maxpooling = MaxPooling(img_gray_conv2d_relu,3).operate()


fig = plt.figure(figsize=(10,10))
for i in range(16):
    plt.subplot(4,4, i + 1)
    plt.imshow(img_gray_conv2d_relu[:,:,i], cmap='gray')
    plt.axis('off')
#plt.savefig('img_gray_conv2d.jpg')
plt.show()





# # entropy - cross entropy - KL Divergence
# # entropy: mức độ hỗn loạn không đồng nhất của 1 mẫu nào đó.
# # entropy = 0: là đồng nhất => nguyên chất
# # tính entropy: entropy = -sum(P(i)*loge(P(i))) cơ số e => mức độ ko đồng nhất
# # sự đồng nhất: p [1,0,0], thêm số cực nhỏ 0.0000000001 để ko cho x nhận giá trị 0
# # không đồng nhất: p[0.333, 0,33, 0,3333333333]
# p = [0.2, 0.45, 0.35]
# q = [0.31, 0.25, 0.44]
# entropy_p = -sum([p[i]*np.log(p[i]) for i in range(len(p))])
# print(entropy_p)
#
# entropy_q = -sum([q[i]*np.log(q[i]) for i in range(len(q))])
# print(entropy_q)
#
# crossentropy_pq = -sum([p[i]*np.log(q[i]) for i in range(len(p))])
# crossentropy_qp = -sum([q[i]*np.log(p[i]) for i in range(len(q))])
# print(crossentropy_pq, crossentropy_qp)
#
# # crossentropy_pq = np.log(q[i]
#
# # KL Divergence: hệ số phân tán
# KL_Divergence_pq = sum([p[i]*np.log(p[i]/q[i]) for i in range(len(p))])
# print(entropy_q + KL_Divergence_pq)
#
#
# # thông số quan trọng, MSE, likelyhood, crossentropy