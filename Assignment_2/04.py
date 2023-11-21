import numpy as np, cv2

image1 = cv2.imread("images/04_1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/04_2.jpg", cv2.IMREAD_GRAYSCALE)

if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

alpha, beta = 0.5, 0.5
image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

def trackbar(value) :
    alpha = cv2.getTrackbarPos('image1', title) / 100
    beta = cv2.getTrackbarPos('image2', title) / 100
    image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)
    result[0:y, x:x * 2] = image3[0:y, 0:x]

    cv2.imshow(title, result)

x, y = image1.shape
result = np.zeros((x, y*3), np.uint8)
result[0:y, 0:x] = image1[0:y, 0:x]
result[ : , x*2: ] = image2[0:y, 0:x]
result[0:y, x:x*2] = image3[0:y, 0:x]

title = 'dst'
cv2.imshow(title, result)
cv2.createTrackbar('image1', title, 50, 100, trackbar)
cv2.createTrackbar('image2', title, 50, 100, trackbar)
cv2.waitKey(0)