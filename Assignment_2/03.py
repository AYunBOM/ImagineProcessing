import numpy as np,cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상 읽기 오류")

blue, green, red = cv2.split(logo)

image = np.zeros_like(blue)
blue_img = cv2.merge([blue, image, image])
green_img = cv2.merge([image, green, image])
red_img = cv2.merge([image, image, red])

cv2.imshow('logo', logo)
cv2.imshow('blue_img', blue_img)
cv2.imshow('green_img', green_img)
cv2.imshow('red_img', red_img)
cv2.waitKey(0)

