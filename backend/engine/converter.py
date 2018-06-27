from PIL import Image
BLACK_PERC = .9

def get_black_percentage(pixels):
	p = 0
	for pixel in pixels:
		if pixel == 1:
			p += 1
	if len(pixels) == 0:
		return 0.0
	else:
		return p / len(pixels)

def get_bar_coords(pixel_list):
	is_line = False
	curr_line = 0
	starting = -1
	curr_staff = 0
	staff_coords = {}
	for pixels in pixel_list:
		if get_black_percentage(pixels) > BLACK_PERC:
			if not is_line:
				is_line = True
				starting = curr_line
		else:
			if is_line:
				is_line = False
				staff_coords[curr_staff] = (starting, curr_line - 1)
				curr_staff += 1
				starting = -1
		curr_line += 1
	return staff_coords

def make_pixel_list(pixels):
	num_pixels = 0
	new_pixels = []
	pixel_list = []
	for pixel in pixels:
		if pixel[0] < 128:
			pixel_list.append(1)
			num_pixels += 1
		else:
			pixel_list.append(0)
			num_pixels += 1
		if num_pixels == LINE_LEN:
			pixel_list = []
			num_pixels = 0
			new_pixels.append(pixel_list)
	return new_pixels

def print_pixels(pixel_list):
	for pixels in pixel_list:
		for pixel in pixels:
			print(pixel, end='')
		print()

im = Image.open("../../sample/sample3.png")
LINE_LEN = im.width
pixel_list = make_pixel_list(list(im.getdata()))
bars = get_bar_coords(pixel_list)
# print(get_bar_coords(pixel_list))
# print_pixels(pixel_list)
