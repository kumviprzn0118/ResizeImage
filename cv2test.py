import cv2
img = cv2.imread('img/Python.jpg')
width = 320
height = 180
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

