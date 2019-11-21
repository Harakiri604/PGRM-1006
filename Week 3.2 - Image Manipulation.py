from PIL import Image as image

inString = "cool_image.png"
outString = "cooler_image.png"

img = image.open(inString)

#print(img.size)
#print(img.size[0], img.size[1])

#size = (int(img.size[0]/4), int(img.size[1]/4))
#img = img.resize(size)
#img.save(outString)

#cropsize = (0,0,400,262)
#img = img.crop(cropsize)
#img.save(outString)

img = img.convert('LA')
img.save(outString)