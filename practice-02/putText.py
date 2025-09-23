'''
img = cv.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    img: イメージ
    text: テキスト
    org: テキストの左下隅の座標
    fontFace: フォント種別
        cv.FONT_HERSHEY_SIMPLEX: 通常サイズのSans-Serif
        cv.FONT_HERSHEY_PLAIN: 小サイズのSans-Serif
        cv.FONT_HERSHEY_DUPLEX: 通常サイズのSans-Serif(FONT_HERSHEY_SIMPLEXより複雑)
        cv.FONT_HERSHEY_COMPLEX: 通常サイズのSerif
        cv.FONT_HERSHEY_TRIPLEX: 通常サイズのSerif(FONT_HERSHEY_COMPLEXより複雑)
        cv.FONT_HERSHEY_COMPLEX_SMALL:  小サイズのSerif
        cv.FONT_HERSHEY_SCRIPT_SIMPLEX: 手書き文字
        cv.FONT_HERSHEY_SCRIPT_COMPLEX: 手書き文字(FONT_HERSHEY_SCRIPT_SIMPLEXより複雑)
        cv.FONT_ITALIC: イタリック
    fontScale: フォントスケール(基本サイズを乗算)
    color: 色
    thickness: ライン太さ
    lineType: ラインの種別
        cv.FILLED: 塗り潰し
        cv.LINE_4: 4-connected
        cv.LINE_8: 8-connected
        cv.LINE_AA: アンチエイリアス
    bottomLeftOrigin: true時はイメージの原点は左下隅、False時は左上隅
'''

import numpy as np
import cv2

# 白イメージの生成
img = np.full((256, 256, 3), 255, np.uint8)

# テキストの描画
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 50), font, 1, (255, 0, 0), 1, cv2.LINE_AA)

# テキストの画像を保存
cv2.imwrite('putText.png', img)

# イメージの表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
