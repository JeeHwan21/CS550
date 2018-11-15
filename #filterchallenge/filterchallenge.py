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

		hsv = c.rgb_to_hsv(origrgb[0] * 1.29, origrgb[1] * 1.15, origrgb[2])

		if hsv[1] < 0.45:

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

img.save('REVISED16.JPG')