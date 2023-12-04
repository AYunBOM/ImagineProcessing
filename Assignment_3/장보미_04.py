import numpy as np
import cv2
from Common.filters import filter

image = cv2.imread("images/filter_sharpen.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일 읽기 오류")

B, G, R = cv2.split(image)

mask_blur = np.array([1/25, 1/25, 1/25, 1/25, 1/25,
                     1/25, 1/25, 1/25, 1/25, 1/25,
                     1/25, 1/25, 1/25, 1/25, 1/25,
                     1/25, 1/25, 1/25, 1/25, 1/25,
                     1/25, 1/25, 1/25, 1/25, 1/25], np.float32).reshape(5, 5)

mask_sharpen = np.array([[0, 0, 0, 0, 0],
                   [0, 0, -1, 0, 0],
                   [0, -1, 5, -1, 0],
                   [0, 0, -1, 0, 0],
                   [0, 0, 0, 0, 0]], np.float32).reshape(5, 5)

avg_blur_R = filter(R, mask_blur).astype('uint8')
avg_blur_G = filter(G, mask_blur).astype('uint8')
avg_blur_B = filter(B, mask_blur).astype('uint8')

sharpen_R = filter(R, mask_sharpen).astype('uint8')
sharpen_G = filter(G, mask_sharpen).astype('uint8')
sharpen_B = filter(B, mask_sharpen).astype('uint8')

bluring_User = cv2.merge([avg_blur_B, avg_blur_G, avg_blur_R])
bluring_User = cv2.convertScaleAbs(bluring_User)

sharpen_User = cv2.merge([sharpen_B, sharpen_G, sharpen_R])
sharpen_User = cv2.convertScaleAbs(sharpen_User)

bluring_OpenCV = cv2.convertScaleAbs(cv2.filter2D(image, cv2.CV_16S, mask_blur))

sharpen_OpenCV = cv2.convertScaleAbs(cv2.filter2D(image, cv2.CV_16S, mask_sharpen))

cv2.imshow('image', image)
cv2.imshow('bluring User', bluring_User)
cv2.imshow('bluring OpenCV', bluring_OpenCV)
cv2.imshow('sharpen User', sharpen_User)
cv2.imshow('sharpen OpenCV', sharpen_OpenCV)

cv2.waitKey(0)
