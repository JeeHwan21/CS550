from PIL import Image
import math as m, colorsys as c
from decimal import Decimal

imgx, imgy = 512, 512

# def zop(z, x, y, sum):
# 	temp = z[0]
# 	z[0] = m.pow(z[0], 2) - m.pow(z[1], 2)
# 	z[1] = 2 * temp * z[1]
# 	# calculate z * z

# 	z[0] = z[0] + x
# 	z[1] = z[1] + y
# 	# calculate z + c

# 	sum = sum + 1

# MANDELBROT 1

image = Image.new("RGB",(imgx, imgy))

xmin, xmax = -0.8638, -0.8614
ymin, ymax = 0.2637, 0.2659

for i in range(imgx):
	for j in range(imgy):

		x = i * (xmax - xmin) / (imgx - 1) + xmin
		y = j * (ymax - ymin) / (imgy - 1) + ymin

		sum = 1

		z = [x, y]

		while True:
			if sum == 256:
				a = c.hsv_to_rgb(0.5, 0.2, 200)
				image.putpixel((i, j), (int(a[0]), int(a[1]), int(a[2])))
				break
				# max iteration: 256
			elif m.pow(z[0], 2) + m.pow(z[1], 2) >= 4:
				b = c.hsv_to_rgb(sum / 8 - int(sum / 8), sum / 8 - int(sum / 8), 200)
				# repeating rainbow colors with varying saturation
				image.putpixel((i, j), (int(b[0]), int(b[1]), int(b[2])))
				# check if z escaped
				break
			else:
				temp = z[0]
				z[0] = m.pow(z[0], 2) - m.pow(z[1], 2)
				z[1] = 2 * temp * z[1]
				# calculate z * z

				z[0] = z[0] + x
				z[1] = z[1] + y
				# calculate z + c

				sum = sum + 1

image.save("JeeHwan_M1.png", "PNG")

# MANDELBROT 2

xmin, xmax = -0.45676176, -0.45669549
ymin, ymax = 0.58401132, 0.58407759

for i in range(imgx):
	for j in range(imgy):

		x = i * (xmax - xmin) / (imgx - 1) + xmin
		y = j * (ymax - ymin) / (imgy - 1) + ymin

		sum = 1

		z = [x, y]

		while True:
			if sum == 256:
				a = c.hsv_to_rgb(0.5, 0.2, 200)
				image.putpixel((i, j), (int(a[0]), int(a[1]), int(a[2])))
				break
				# max iteration: 256
			elif m.pow(z[0], 2) + m.pow(z[1], 2) >= 4:
				b = c.hsv_to_rgb(0.925 + sum / 64 - int(sum / 64 / 0.047) * 0.047 , sum / 64 - int(sum / 64), 220 - sum * 100 / 255)
				# gradient color from pink to red with varying value
				image.putpixel((i, j), (int(b[0]), int(b[1]), int(b[2])))
				# check if z escaped
				break
			else:
				temp = z[0]
				z[0] = m.pow(z[0], 2) - m.pow(z[1], 2)
				z[1] = 2 * temp * z[1]
				# calculate z * z

				z[0] = z[0] + x
				z[1] = z[1] + y
				# calculate z + c

				sum = sum + 1

image.save("JeeHwan_M2.png", "PNG")

# JULIA SET

xmin, xmax = -2, 2
ymin, ymax = -2, 2

for i in range(imgx):
	for j in range(imgy):

		x = i * (xmax - xmin) / (imgx - 1) + xmin
		y = j * (ymax - ymin) / (imgy - 1) + ymin

		sum = 1

		z = [x, y]

		while True:
			if sum == 256:
				a = c.hsv_to_rgb(0.5, 1, 255)
				image.putpixel((i, j), (int(a[0]), int(a[1]), int(a[2])))
				break
				# max iteration: 256
			elif m.pow(z[0], 2) + m.pow(z[1], 2) >= 4:
				b = c.hsv_to_rgb(sum / 255, 1, 255)
				# gradient color from pink to red with varying value
				image.putpixel((i, j), (int(b[0]), int(b[1]), int(b[2])))
				# check if z escaped
				break
			else:
				temp = z[0]
				z[0] = m.pow(z[0], 2) - m.pow(z[1], 2)
				z[1] = 2 * temp * z[1]
				# calculate z * z

				z[0] = z[0] + 0.5
				z[1] = z[1] - 0.245
				# constant c is 0.5 - 0.245i
				# calculate z + c

				sum = sum + 1

image.save("JeeHwan_J1.png", "PNG")



