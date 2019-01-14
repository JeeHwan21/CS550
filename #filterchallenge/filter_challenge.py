# https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
# https://docs.python.org/2/library/colorsys.html

from PIL import Image
import sys as s, colorsys as c

img = Image.open(s.argv[1])
[x, y] = img.size

pix = img.load()

for a in range(x):
	for b in range(y):

		origrgb = pix[a, b]

		if origrgb[0] > 1.5 * origrgb[1] and origrgb[0] > 1.5 * origrgb[2]:

			p = 240
			q = origrgb[1] * 0.2
			r = origrgb[2] * 0.2

		elif origrgb[0] < 100 and origrgb[1] < 100 and origrgb[2] < 100:

			p = origrgb[0] * 0.29
			q = origrgb[1] * 0.29
			r = origrgb[2] * 0.29

		else:

			p = origrgb[0] * 1.29
			q = origrgb[1] * 1.29
			r = origrgb[2] * 1.29

		hsv = c.rgb_to_hsv(p * 1.19, q * 1.05, r + 10)

		if hsv[1] < 0.40:

			m = hsv[1] * 0.7

		else:
			
			m = hsv[1]

		if hsv[2] < 0.5:

			n = hsv[2] * 0.4

		else:

			n = hsv[2]

		newrgb = c.hsv_to_rgb(hsv[0], m, n)

		if newrgb[0] % 2 == 0:

			i = 200

		elif newrgb[0] % 3 == 0:

			i = 150

		else:

			i = newrgb[0]

		pix[a, b] = (int(i), int(newrgb[1]), int(newrgb[2]))

img.save('REVISED.JPG')