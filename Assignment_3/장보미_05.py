import numpy as np, cv2

image = cv2.imread("images/cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

def Thresh1(pos):
    global title, thresh1
    thresh1 = pos
    canny = cv2.Canny(image, thresh1, thresh2)
    cv2.imshow(title, canny)

def Thresh2(pos):
    global title, thresh2
    thresh2 = pos
    canny = cv2.Canny(image, thresh1, thresh2)
    cv2.imshow(title, canny)

title = "canny edge"
thresh1_title, thresh2_title = "th1", "th2"
thresh1,thresh2 = 100, 150

canny = cv2.Canny(image, thresh1, thresh2)
cv2.imshow(title, canny)

cv2.createTrackbar(thresh1_title, title, thresh1, 255, Thresh1)
cv2.createTrackbar(thresh2_title, title, thresh2, 255, Thresh2)

cv2.waitKey(0)


