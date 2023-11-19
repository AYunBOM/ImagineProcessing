import numpy as np
import cv2

mat1 = np.full ((200,300), 100, np.uint8)
mat2 = np.full ((200,300), 100, np.uint8)

cv2.imshow('win mode1', mat1)
cv2.imshow('win mode2', mat2)
cv2.moveWindow('win mode1', 0, 0)
cv2.moveWindow('win mode2', 300, 200)
cv2.waitKey(0)
cv2.destroyAllWindows()


