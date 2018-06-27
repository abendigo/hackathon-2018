from PIL import Image
LINE_LEN = 600

def print_pixels(pixels):
	line = 0
	for pixel in pixels:
		if pixel == (255, 255, 255):
			print(0, end='')
			line += 1
		else:
			print(1, end='')
			line += 1
		if line == LINE_LEN:
			print()
			line = 0


def remove_staff(pixels):
	new_pixels = []

	for pixel in pixels:
		if pixel[0] < 128:
			p = (0, 0, 0)
		else:
			p = (255, 255, 255)
		new_pixels.append(p)
	return new_pixels	


im = Image.open("../../sample/sample1.png")
pixels = remove_staff(list(im.getdata()))

print_pixels(pixels)




