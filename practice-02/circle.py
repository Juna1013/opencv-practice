'''
img = cv.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
    img: イメージ
    center: 中心点
    radius: 半径
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

# 円の描画
cv2.circle(img, (40, 40), 30, (255, 0, 0), -1)

# 円の画像を保存
cv2.imwrite('circle.png', img)

# イメージの表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
