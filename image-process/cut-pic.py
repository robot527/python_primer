#! /usr/bin/env python3
# coding: utf-8
'''
按指定坐标裁剪图片。
'''
import sys
from PIL import Image


def cut_picture(pic, lu_x, lu_y, rd_x, rd_y, new="new"):
    '''
    按指定坐标裁剪图片
    lu_x, lu_y: 左上角坐标
    rd_x, rd_y: 右下角坐标
    '''
    im = Image.open(pic)
    im = im.crop((lu_x, lu_y, rd_x, rd_y))
    width, height = im.size
    print("After cutting, width: %d, height: %d" % (width, height))

    #save new picture
    im.save('{}{}'.format(new, pic))
    print(new + pic)


def main():
    argc = len(sys.argv)
    if argc != 6:
        print("Usage: python3 %s picture.png x1 y1 x2 y2" % sys.argv[0])
        print(sys.argv)
    else:
        x1 = int(sys.argv[2])
        y1 = int(sys.argv[3])
        x2 = int(sys.argv[4])
        y2 = int(sys.argv[5])
        new = sys.argv[2] + '_' + sys.argv[3] + '-' + sys.argv[4] + '_' + sys.argv[5] + '@'
        cut_picture(sys.argv[1], x1, y1, x2, y2, new)

if __name__ == '__main__':
    main()

