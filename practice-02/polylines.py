'''
img = cv.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]])
    img: イメージ
    pts: 多角形曲線の配列
    isClosed: ポリラインが閉じているかどうか
    color: 色または明るさ(グレースケールイメージ)
    thickness: ラインの太さ(マイナスは塗り潰し)
    lineType: ラインの種別
        cv.FILLED: 塗り潰し
        cv.LINE_4: 4-connected
        cv.LINE_8: 8-connected
    shift: 頂点の小数ビットの数
'''

import numpy as np
import cv2

# 白イメージの生成
img = np.full((256, 256, 3), 255, np.uint8)

# 多角形の描画
pts = np.array([[10, 5], [120, 30], [170, 120], [50, 110]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 0), 5)

# 多角形の画像を保存
cv2.imwrite('polylines.png', img)

# イメージの表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
