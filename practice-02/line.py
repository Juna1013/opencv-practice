'''
img = cv.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
    img: イメージ
    pt1: ラインの始点
    pt2: ラインの終点
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

# ラインの描画
cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# ラインの画像を保存
cv2.imwrite('line.png', img)

# イメージの表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
