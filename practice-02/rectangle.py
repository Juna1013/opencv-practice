'''
img = cv.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
img = cv.rectangle(img, rec, color[, thickness[, lineType[, shift]]])
    img: イメージ
    pt1: 長方形の頂点
    pt2: pt1の反対側の長方形の頂点
    color: 色または明るさ(グレースケールイメージ)
    thickness: ラインの太さ(マイナスは塗り潰し)
    lineType: ラインの種別
        cv.FILLED: 塗り潰し
        cv.LINE_4: 4-connected
        cv.LINE_8: 8-connected
        cv.LINE_AA: アンチエイリアス
    shift: 頂点の小数ビットの数
'''

import numpy as np
import cv2

# 白イメージの生成
img = np.full((256, 256, 3), 255, np.uint8)

# 長方形の描画
cv2.rectangle(img, (10, 10), (100, 100), (0, 255, 0), 5)

# 長方形の画像を保存
cv2.imwrite('rectangle.png', img)

# イメージの表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
