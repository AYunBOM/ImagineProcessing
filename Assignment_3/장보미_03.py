import numpy as np, cv2, time

image = cv2.imread("images/image3.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 오류")
if image.ndim != 3:
    raise Exception("영상파일 차원 오류")

start = time.time()

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

num_hue_bins = 30
num_saturation_bins = 48
two_dim_histo = np.zeros((num_hue_bins, num_saturation_bins))

for row in range(hsv_img.shape[0]):
    for col in range(hsv_img.shape[1]):
        hue_bin = int(hsv_img[row, col, 0] / 180 * num_hue_bins)
        sat_bin = int(hsv_img[row, col, 1] / 256 * num_saturation_bins)
        if hue_bin < num_hue_bins and sat_bin < num_saturation_bins:
            two_dim_histo[hue_bin, sat_bin] += 1

hist_image = cv2.normalize(two_dim_histo, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
hist_image = cv2.resize(hist_image, (480, 300), interpolation=cv2.INTER_AREA)

color_histo = np.zeros(image.shape, np.uint8)
color_histo = cv2.resize(color_histo, (480, 300), interpolation=cv2.INTER_AREA)

for row in range(color_histo.shape[0]):
    for col in range(color_histo.shape[1]):
        hue_bin = int(row * num_hue_bins / 300)
        sat_bin = int(col * num_saturation_bins / 480)

        if hue_bin < num_hue_bins and sat_bin < num_saturation_bins:
            if two_dim_histo[hue_bin, sat_bin] > 10:
                color_histo[row, col] = [hue_bin * 180 // num_hue_bins, sat_bin * 256 // num_saturation_bins, two_dim_histo[hue_bin, sat_bin] // 3.56]

title = 'image'
dst = 'dst'

color_histo = cv2.cvtColor(color_histo, cv2.COLOR_HSV2BGR)

end = time.time()
result = (end-start) * 1000.0
print(f"실행속도:{result: .2f} msec")

cv2.imshow(title, image)
cv2.imshow(dst, color_histo)
cv2.waitKey(0)
cv2.destroyAllWindows()


