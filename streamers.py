import random as r
from PIL import Image
global k, g, b, j

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))

def p():
	m = r.randint(1, 5)
	if m == 1:
		image.putpixel((x + 1, j), (k, g, b))
	elif m == 2:
		image.putpixel((x + 1, j + 1), (k, g, b))
		j = j + 1
	elif m == 3:
		image.putpixel((x, j + 1), (k, g, b))
		j = j + 1
	elif m == 4:
		image.putpixel((x - 1, j + 1), (k, g, b))
		j = j + 1
	else:
		image.putpixel((x - 1, j), (k, g, b))

for i in range(100):
	k = r.randint(0, 255)
	g = r.randint(0, 255)
	b = r.randint(0, 255)
	x = r.randint(0, 511)
	j = 0
	image.putpixel((x, j), (k, g, b))
	while True:
		if j == 511:
			break
		else:
			p()


image.save("streamers.png", "PNG")

# for i in range(100):
# 	x = r.randint(10, 501)
# 	a = x + 6
# 	b = x - 6
# 	global k, g, b
# 	k = r.randint(0, 255)
# 	g = r.randint(0, 255)
# 	b = r.randint(0, 255)
# 	for j in range(512):
# 		y = r.randint(-1, 1)
# 		x = x + y
# 		if x > a:
# 			x = x - 1
# 		elif x < b:
# 			x = x + 1
# 		image.putpixel((x + y, j), (k, g, b))

# image.save("streamers.png", "PNG")