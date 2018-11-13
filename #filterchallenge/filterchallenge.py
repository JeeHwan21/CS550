# https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
# https://docs.python.org/2/library/colorsys.html

from PIL import Image
import sys as s, colorsys as c

img = Image.open(s.argv[1])
[x, y] = img.size

pix = img.load()

for a in range(x):
	for b in range(y):

		rgb = pix[a, b]

		hsv = c.rgb_to_hsv(rgb[0], rgb[1], rgb[2])

		rgb = c.hsv_to_rgb(hsv[0], hsv[1] + 0.3, hsv[2] * 1.32)

		pix[a, b] = (int(rgb[0]), int(rgb[1]), int(rgb[2]))

img.save('REVISED.JPG')