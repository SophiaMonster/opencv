import cv2
import os

# print(os.path)
# print(os.path.exists('/Users/mengting/Desktop/opencv_demo/opencv/fairy.jpeg'))
# color_img = cv2.imread('/Users/mengting/Desktop/opencv_demo/opencv/fairy.jpeg')
# a = color_img.shape

# gray_img = cv2.imread('/Users/mengting/Desktop/opencv_demo/opencv/fairy.jpeg', cv2.IMREAD_GRAYSCALE)
# print(gray_img.shape)
#
# cv2.imwrite('/Users/mengting/Desktop/opencv_demo/opencv/fairy.jpeg', gray_img)
# reload_grayscale = cv2.imread('/Users/mengting/Desktop/opencv_demo/opencv/fairy.jpeg')
# print(reload_grayscale.shape)
# #
# print(cv2.imwrite('anglababy.jpg',color_img,(cv2.IMWRITE_JPEG_QUALITY, 100)))

img_path = '/Users/mengting/Desktop/opencv_demo/opencv/fairy.jpeg'
img = cv2.imread(img_path)
img_200 = cv2.resize(img, (100, 100))
print(img_200.shape)
# img_half=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
cv2.imshow("image", img_200)
cv2.waitKey(0)