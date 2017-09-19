#!/usr/bin/env python
#coding: utf-8

myPath = "./media/"
fontPath = "./media/"
inputFile = "xwp.jpg"
outputFile = "output.jpg"

import Image, ImageFont, ImageDraw
#打开图片
im = Image.open(myPath + inputFile)
draw = ImageDraw.Draw(im)
#根据图片大小确定字体大小
fontsize = min(im.size)/4
#加文字
font = ImageFont.truetype(fontPath + 'KhmerOS.ttf', fontsize)
draw.text((im.size[0]-fontsize, 20), '9', font = font, fill = (0,255,0))
im.save(myPath + outputFile,"jpeg")
