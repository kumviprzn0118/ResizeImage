from PIL import Image

img = Image.open("img/Python.jpg")
width = 320
height = 180
# 各フィルターでリサイズ
resized_nearest = img.resize((width, height), resample=Image.NEAREST)
resized_box = img.resize((width, height), resample=Image.BOX)
resized_bilinear = img.resize((width, height), resample=Image.BILINEAR)
resized_hamming = img.resize((width, height), resample=Image.HAMMING)
resized_bicubic = img.resize((width, height), resample=Image.BICUBIC)
resized_lanczos = img.resize((width, height), resample=Image.LANCZOS)
resized_antialias = img.resize((width, height), resample=Image.ANTIALIAS)

# 各リサイズ結果の保存
resized_nearest.save("pillow/resized_nearest.jpg")
resized_box.save("pillow/resized_box.jpg")
resized_bilinear.save("pillow/resized_bilinear.jpg")
resized_hamming.save("pillow/resized_hamming.jpg")
resized_bicubic.save("pillow/resized_bicubic.jpg")
resized_lanczos.save("pillow/resized_lanczos.jpg")
resized_antialias.save("pillow/resized_antialias.jpg")
