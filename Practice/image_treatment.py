# -*- coding:utf8 -*-
from PIL import Image

Yunaimg=Image.open("C:\\Users\\Basanwei\\Pictures\\1454533979.jpg")
print(Yunaimg.format)
print(Yunaimg.mode)
print(Yunaimg.size)
Yunaimg.save('yuna.pdf')
width, height = Yunaimg.size
sYuna=Yunaimg.resize((int(width/2), int(height/2)))
sYuna.save('shrinked_yuna.JPEG')
tile=Yunaimg.crop((50,30,250,230))
tile.save('yuna_face.JPEG')
tile.transpose(Image.FLIP_LEFT_RIGHT).save('yunaface_mirrror.PNG')
yunafaces=Image.new('RGBA',(600,600),'grey')
yunafaces.save('background.PNG')

backgroundwidth, backgroundheight=yunafaces.size
facewidth, faceheight=tile.size
yuna=yunafaces.copy()
print(yunafaces.size, tile.size)
for i in range(0,backgroundwidth,facewidth):
    for j in range(0,backgroundheight,faceheight):
        print(i,j)
        yuna.paste(tile,(i,j))
yuna.save('yuna.PNG')




# ermei=Image.open("C:\\Users\\Basanwei\\Pictures\\mmexport1556446967531.jpg")
# print(ermei.format)
# print(ermei.mode)
# print(ermei.size)
# width, height = ermei.size
# s_ermei=ermei.resize((int(width/2), int(height/2)))
# s_ermei.save('s_ermei.JPEG')