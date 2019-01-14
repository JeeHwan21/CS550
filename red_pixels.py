from PIL import Image
import math as m

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))

def up(i, j):
	image.putpixel((i, j), (int(300 / 512 * j), 0, 0))
def down(i, j):
	image.putpixel((i, j), (300 - int(300 / 512 * j), 0, 0))
def sq(x):
	return m.pow(x, 2)

for i in range(512):
	for j in range(512):

		if sq(i) + sq(j) < sq(64):
			down(i, j)
		elif sq(i) + sq(j) < sq(64 * 2):
			up(i, j)
		elif sq(i) + sq(j) < sq(64 * 3):
			down(i, j)
		elif sq(i) + sq(j) < sq(64 * 4):
			up(i, j)
		elif sq(i) + sq(j) < sq(64 * 5):
			down(i, j)
		elif sq(i) + sq(j) < sq(64 * 6):
			up(i, j)
		elif sq(i) + sq(j) < sq(64 * 7):
			down(i, j)
		elif sq(i) + sq(j) < sq(64 * 8):
			up(i, j)
		else:
			down(i, j)


image.save("JeeHwan_redPixels.png", "PNG")