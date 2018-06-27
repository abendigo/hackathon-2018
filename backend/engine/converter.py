from PIL import Image
BLACK_PERC = .9

def get_black_percentage(pixels):
	p = 0
	for pixel in pixels:
		if pixel == 1:
			p += 1
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

def get_combined_bar_coords(pixel_list):
	all_coords = []
	coord_dict = get_bar_coords(pixel_list)
	for i in range(5):
		(s, e) = coord_dict[i]
		for j in range(s, e+1):
			all_coords.append(j)
	
	return all_coords

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
		if num_pixels == WIDTH:
			new_pixels.append(pixel_list)
			pixel_list = []
			num_pixels = 0
	return new_pixels

def make_vertical_pixel_list(pixel_list):
	vertical_pixel_list = [[None for _ in range(LINE_VER_LEN)] for _ in range(WIDTH)]
	for i in range(LINE_VER_LEN):
		for j in range(WIDTH):
			vertical_pixel_list[j][i] = pixel_list[i][j]
	return vertical_pixel_list

def print_pixels(pixel_list):
	for pixels in pixel_list:
		for pixel in pixels:
			print(pixel, end='')
		print()

def remove_staffs(pixel_list, staffs):
	curr_staff = 0
	for i in range(len(pixel_list)):
		empty_list = [0 for _ in range(WIDTH)]
		if i in staffs:
			pixel_list[i] = empty_list

im = Image.open("../../sample/sample3.png")
WIDTH = im.width
LINE_VER_LEN = im.height
pixel_list = make_pixel_list(list(im.getdata()))
# gets the bar lines in format {0: (starting, ending)}
bars = get_bar_coords(pixel_list)
# for removing bars; list of all the lines that are a bar
combined_bars = get_combined_bar_coords(pixel_list)
# same as pixel_list but now vertical
vertical_list = make_vertical_pixel_list(pixel_list)
# remove staff bars
remove_staffs(pixel_list, combined_bars)
print_pixels(pixel_list)



