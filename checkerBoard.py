from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))

for i in range(512):
	for j in range(512):
		image.putpixel((i, j), (0, 0, 0))

def cb(x):
	for i in range(x):
		for j in range(x):
			for k in range(int(512/x) * i, int(512/x) * (i + 1)):
				for l in range(int(512/x) * j, int(512/x) * (j + 1)):
					if (i + j) % 2 == 0:
						image.putpixel((k, l), (0, 0, 0))
					else:
						image.putpixel((k, l), (255, 0, 0))

cb(16)

image.save("checkBoard.png", "PNG")