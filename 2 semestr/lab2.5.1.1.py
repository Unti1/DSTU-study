from PIL import Image,ImageDraw,ImageFont, ImageColor,ImageFilter

#1 
img = Image.open('imgur.jpg')
img.show()

crope = img.crop((0,0,320,190))
crope.save('test_png.jpg')

img2 = Image.open('test_png.jpg')
img2.show()

#2 
img3 = Image.open('KFC.png')
idraw = ImageDraw.Draw(img3)
text = 'Он любит KFC'
font = ImageFont.truetype('arial.ttf',size=20)
idraw.text((100,300),text,font = font)

idraw.rectangle((250,10,30,300),outline = ImageColor.getcolor("#F19033", "RGB"),width = 3)
img3.show()

#3

img4 = Image.open('google.png')
area = (0,100,1200,1000)
ic = img4.crop(area)
for i in range(10):
    ic = ic.filter(ImageFilter.BLUR)
img4.paste(ic,area)
img4.show()


#4
img4.save('search_pic.png')