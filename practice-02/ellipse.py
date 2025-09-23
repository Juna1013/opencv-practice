'''
img = cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])
img = cv.ellipse(img, box, color[, thickness[, lineType]])
    img: イメージ
    center: 楕円の中心点
    axes: 主軸のサイズの半分
    angle: 回転角度(度)
    startAngle: 弧の開始角度(度)
    endAngle: 弧の終了角度(度)
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

# 楕円の描画
cv2.ellipse(img, (40, 40), (30, 30), 0, 0, 180, (0, 0, 255), -1)

# 円の画像を保存
cv2.imwrite('ellipse.png', img)

# イメージの表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
