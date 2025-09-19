import cv2

# イメージの読み込み
img = cv2.imread('sample.png')

# グレースケール変換
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# グレースケールの画像を保存
cv2.imwrite('sample_gray.png', img_gray)

# イメージの表示
cv2.imshow('Gray Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
