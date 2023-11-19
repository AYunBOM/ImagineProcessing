import cv2

image = cv2.imread("Image/image.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise Exception("Error: Failed to load image file")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 0)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]
cv2.imshow("Image", image)
cv2.imwrite("Image/test.jpg", image, params_jpg)
cv2.imwrite("Image/test.png", image, params_png)
cv2.waitKey(0)

