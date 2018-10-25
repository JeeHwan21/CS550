from PIL import Image
import math as m, colorsys as c
global color, imgx, imgy, xmin, xmax, ymin, ymax

imgx, imgy = 512, 512

# xmin, xmax = -0.5438500237651169, -0.5431959995767102
# ymin, ymax = 0.6137094649166102, 0.614363489105169

xmin, xmax = 0.13501, 0.13506
ymin, ymax = 0.63751, 0.63756

image = Image.new("RGB",(imgx, imgy))

for i in range(imgx):
	for j in range(imgy):

		x = i * (xmax - xmin) / (imgx - 1) + xmin
		y = j * (ymax - ymin) / (imgy - 1) + ymin

		sum = 1

		z = [x, y]

		while True:
			if sum == 256:
				# maximum iteration is 100
				a = c.hsv_to_rgb(1, 0.1, 1.0)
				image.putpixel((i, j), (int(a[0]), int(a[1]), int(a[2])))
				break
			elif m.pow(z[0], 2) + m.pow(z[1], 2) >= 4:
				b = c.hsv_to_rgb((1 / 64 * sum)/255, (sum / 10)/255, 1.0)
				image.putpixel((i, j), (int(b[0]*255), int(b[1]*255), int(b[2]*255)))
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

image.save("MANDELBROT4.png", "PNG")