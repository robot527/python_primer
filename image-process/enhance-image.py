#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author  : luoyz
# @desc    : enhance image


def enhance_img(img, b=1.0, c=1.0, s=1.0, new='new'):
    '''
    图片强化处理
    '''
    from PIL import Image
    from PIL import ImageEnhance

    image = Image.open(img)
    enh_con = ImageEnhance.Contrast(image)
    #亮度 Brightness
    enh_image = enh_con.enhance(b)
    #对比度 Contrast
    enh_image = enh_con.enhance(c)
    #锐度 Sharpness
    enh_image = enh_con.enhance(s)

    enh_image.show()
    print(new + img)
    enh_image.save('{}{}'.format(new, img))


if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    if argc < 3:
        print("Usage: python3 %s picture.jpg b c s" % sys.argv[0])
        print("b: factor of Brightness, default is 1.0")
        print("c: factor of Contrast, default is 1.0")
        print("s: factor of Sharpness, default is 1.0")
    else:
        b = float(sys.argv[2])
        new = 'b' + sys.argv[2]
        c = 1.0
        if argc >= 4:
            c = float(sys.argv[3])
            new += '-c' + sys.argv[3]
        s = 1.0
        if argc == 5:
            s = float(sys.argv[4])
            new += '-s' + sys.argv[4]
        new += '-@'
        enhance_img(sys.argv[1], b, c, s, new)

