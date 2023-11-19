import numpy as np
import cv2

white, blue, red = (255,255,255), (255, 0, 0), (0, 0, 255)
ratio = 200
height, width = ratio*2, ratio*3

image = np.full((height, width, 3), white, np.uint8)

title = 'image'
cv2.imshow(title, image)

st_radius, md_radius = height//4, height//8
center = (image.shape[1]//2, image.shape[0]//2)
lf_center = (center[0]-md_radius, center[1])
rg_center = (center[0]+md_radius, center[1])

cv2.ellipse(image, center, (st_radius, st_radius), 0, 180, 360, red, -1)
cv2.ellipse(image, center, (st_radius, st_radius), 0, 0, 180, blue, -1)
cv2.ellipse(image, lf_center, (md_radius, md_radius), 0, 0, 180, red, -1)
cv2.ellipse(image, rg_center, (md_radius, md_radius), 0, 180, 360, blue, -1)
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)


