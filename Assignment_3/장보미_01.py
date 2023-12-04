import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("images/image1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

bins, ranges = [256], [0, 256]
hist = cv2.calcHist([image], [0], None, bins, ranges)

accum_hist = np.cumsum(hist)
accum_hist = (accum_hist / accum_hist[-1]) * 255

dst1 = np.interp(image, range(256), accum_hist).astype(np.uint8)
dst2 = cv2.equalizeHist(image)

hist_ver = cv2.reduce(image, 0, cv2.REDUCE_AVG).ravel().astype(int)
hist_hor = cv2.reduce(image, 1, cv2.REDUCE_AVG).ravel().astype(int)

hist_ver = draw_histo(hist_ver, shape=(400, 300))
hist_hor = draw_histo(hist_hor, shape=(300, 400))
image = cv2.resize(image, (300, 400))

hist_ver = cv2.flip(hist_ver, -1)
hist_hor = cv2.rotate(hist_hor, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("image", image)
cv2.imshow("hist_ver", hist_ver)
cv2.imshow("hist_hor", hist_hor)

cv2.waitKey(0)
cv2.destroyAllWindows()


