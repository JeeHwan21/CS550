from PIL import Image
import math as m
global color

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))

def check(a, b):
	x = 2 / 256 * (a - 255)
	y = 2 / 256 * (b - 255)
	# set center as (0,0) - not exact because the grid is 512 x 512, which are even numbers

	sum = 1
	z = [x, y]
	while True:
		if sum == 255:
			# maximum iteration is 255
			image.putpixel((a, b), ((109 * sum) % 110, (109 * sum) % 43, 0))
			break
		elif m.pow(z[0], 2) + m.pow(z[1], 2) >= 4:
			image.putpixel((a, b), ((109 * sum) % 110, (109 * sum) % 43, 0))
			# checking if z escaped
			break
		else:
			temp = z[0]
			z[0] = m.pow(z[0], 2) - m.pow(z[1], 2)
			z[1] = 2 * temp * z[1]
			# calculated z squared

			z[0] = z[0] + x
			z[1] = z[1] + y
			# calculated z + c

			sum = sum + 1

for i in range(512):
	for j in range(512):
		check(i, j)

image.save("m2.png", "PNG")