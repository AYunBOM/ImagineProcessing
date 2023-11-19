import numpy as np
import cv2

blue, red = (255, 0, 0), (0, 0, 255)
pt = (-1, -1)
title = "Draw Event"
bar_name = 'Thickness'
def onChange(x):
    pass
def onMouse(event, x, y, flags, param):
    global title, pt, bar_name, pnt
    tcs = int(cv2.getTrackbarPos(bar_name, title))

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            pnt = pt[0] + (pt[0] - x), pt[1] + (pt[1] - y)
            cv2.rectangle(image, pnt, (x, y), blue, tcs)
            cv2.imshow(title, image)
            pt = (-1, -1)

    if event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = (pt[0] - x)//2, (pt[1] - y)//2
            pnt = (pt[0] - dx, pt[1] - dy)
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.circle(image, pnt, radius, red, tcs)
            cv2.imshow(title, image)
            pt = (-1, -1)

image = np.full((300, 500, 3),(255, 255, 255), np.uint8)

cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, 1, 10, onChange)
cv2.setMouseCallback(title, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()


