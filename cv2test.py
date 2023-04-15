import cv2
img = cv2.imread('img/Python.jpg')
width = 320
height = 180
# トリミングするサイズ
crop_width = 640
crop_height = 360

# 画像の中心座標
center_x = img.shape[1] / 2
center_y = img.shape[0] / 2

# 中心を中心としてトリミングする範囲
x_start = int(center_x - crop_width / 2)
y_start = int(center_y - crop_height / 2)
x_end = int(center_x + crop_width / 2)
y_end = int(center_y + crop_height / 2)

# トリミング
cropped_img = cv2.getRectSubPix(img, (crop_width, crop_height), (center_x, center_y))

# 各フラグでリサイズ
resized_nearest = cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)
resized_linear = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
resized_cubic = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(img, (width, height), interpolation=cv2.INTER_LANCZOS4)

# 各リサイズ結果の保存
cv2.imwrite("cv/resized_nearest.jpg", resized_nearest)
cv2.imwrite("cv/resized_linear.jpg", resized_linear)
cv2.imwrite("cv/resized_cubic.jpg", resized_cubic)
cv2.imwrite("cv/resized_lanczos.jpg", resized_lanczos)

