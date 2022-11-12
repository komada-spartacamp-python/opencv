import cv2

# print(cv2.__version__)
# img = cv2.imread("image/cat.jpeg",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("image/cat.jpeg")
cv2.imshow("Image", img)

cv2.putText(
    img,
    text="CAT !!!",
    org=(100, 250),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=5,
    color=(255, 255, 0),
    thickness=3,
)
resize_img = cv2.resize(
    img,
    dsize=(
        768 // 2,
        432 // 2,
    ),
)
cv2.imwrite("image/resize_cat.jpeg", resize_img)

# cv2.waitKey(5000)

# cv2.imwrite("image/new_cat.jpeg", img)
print(img.shape)


# import os
# import sys
# import cv2

# cur_dir = os.path.dirname(sys.argv[0])  # 現在のディレクトリを取得
# file_path = os.path.join(cur_dir, 'image/cat.jpg')

# img = cv2.imread(file_path)  # 画像の読み込み(path) 階層が違うと読み込めないので注意

# cv2.imshow("Image", img)  # 読み込んだ画像を表示

# cv2.waitKey(1000) # 1秒待つ
