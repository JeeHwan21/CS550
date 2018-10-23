from PIL import Image
import math as m
global color, imgx, imgy, xmin, xmax, ymin, ymax

imgx, imgy = 512, 512

dif = 4

xmin, xmax = -2, -2 + dif
ymin, ymax = -2, -2 + dif

image = Image.new("RGB",(imgx, imgy))

# def check(a, b):
# 	x = a * (xmax - xmin) / (imgx - 1) + xmin
# 	y = b * (ymax - ymin) / (imgy - 1) + ymin

# 	sum = 1
# 	z = [x, y]
# 	while True:
# 		if sum == 255:
# 			# maximum iteration is 255
# 			image.putpixel((a, b), ((109 * sum) % 110, (109 * sum) % 43, 0))
# 			break
# 		elif m.pow(z[0], 2) + m.pow(z[1], 2) >= 4:
# 			image.putpixel((a, b), ((109 * sum) % 110, (109 * sum) % 43, 0))
# 			# checking if z escaped
# 			break
# 		else:
# 			temp = z[0]
# 			z[0] = m.pow(z[0], 2) - m.pow(z[1], 2)
# 			z[1] = 2 * temp * z[1]
# 			# calculated z squared

# 			z[0] = z[0] + x
# 			z[1] = z[1] + y
# 			# calculated z + c

# 			sum = sum + 1

for i in range(imgx):
	for j in range(imgy):

		x = i * (xmax - xmin) / (imgx - 1) + xmin
		y = j * (ymax - ymin) / (imgy - 1) + ymin

		sum = 1
		z = [x, y]
		while True:
			if sum == 256:
				# maximum iteration is 255
				image.putpixel((i, j), ((109 * sum) % 110, (109 * sum) % 43, 0))
				break
			elif m.pow(z[0], 2) + m.pow(z[1], 2) >= 4:
				image.putpixel((i, j), ((109 * sum) % 110, (109 * sum) % 43, 0))
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

image.save("m3.png", "PNG")