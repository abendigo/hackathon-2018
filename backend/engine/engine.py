import os
from PIL import Image
from collections import Counter
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


# im = Image.open("../../sample/sample1.png")
# pixels = remove_staff(list(im.getdata()))
# 
# print_pixels(pixels)


im = Image.open('/Users/daniel.pang/dev/hackathon-2018/sample/sample1.png')
pic = im.load()

vals = list(im.getdata())
print(len(vals))
# print(im.size)
# print(vals)


def img_to_note(img):
    '''
    Accepts a PIL image object and returns a musical note (output format TBD)
    '''
    if img.size != (600,350):
        return 'Incorrect image size'

    # Convert to greyscale values and store it in a list
    grey_img = img.convert('L')
    grey_vals = list(grey_img.getdata())

    # Count number of dark pixels in each row (black is 0, white is 255)
    for row in range(350):
        if count(grey_vals[row*600], )
