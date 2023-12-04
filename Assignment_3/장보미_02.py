import cv2, time

image = cv2.imread("images/test.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 오류")

start = time.time()

B, G, R = cv2.split(image)

Y = 0.299 * R + 0.587 * G + 0.114 * B
Cb = (B - Y) * 0.564 + 128
Cr = (R - Y) * 0.713 + 128

YCbCr = cv2.merge([Y, Cb, Cr])

Y, Cb, Cr = cv2.split(YCbCr)

R = Y + 1.403 * (Cr - 128)
G = Y - 0.714 * (Cr - 128) - 0.344 * (Cb - 128)
B = Y + 1.773 * (Cb - 128)

image_revised = cv2.merge([B, G, R])

title1,title2 = 'original', "change"

end = time.time()
result = (end-start) * 1000.0
print(f"실행속도:{result: .2f} msec")

cv2.imshow(title1, image)
cv2.imshow(title2, cv2.convertScaleAbs(image_revised))
cv2.waitKey(0)
cv2.destroyAllWindows()


