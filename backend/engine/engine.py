import os
from PIL import Image
from collections import Counter
import converter as c

# im = Image.open('/Users/daniel.pang/dev/hackathon-2018/sample/sample1.png')
# pic = im.load()

# vals = list(im.getdata())
# print(len(vals))
# print(im.size)
# print(vals)

def img_to_note(pixels, bar_dict):
    '''
    Accepts a list of list representing the pixel data and a dict with keys being
    the row column and values being the tuples indicating the pixel row range
    Returns a musical note (output format TBD)
    '''
    # Input handling
    if len(pixels) != 600 or len(pixels[0]) != 900:
        print('Incorrect image size')
        return

    min = 105
    max = 140
    start_row = 0
    end_row = 0

    # Count number of dark pixels in each row (black is 1, white is 0)
    # If number of pixels is within threshold of min and max then a note has been found
    pixel_range = {'G':0, 'E': 0, 'C':0, 'A':0, 'F':0, 'D':0}
    for row_index in range(len(pixels)):
        row = pixels[row_index]
        pixel_counts = Counter(row[230:])
        # Count number of black pixels in the row
        num_black_pixels = pixel_counts[1]

        # Map pixel row to a note
        if row_index < bar_dict[0][0]:
            pixel_range['G'] += num_black_pixels
        elif row_index < bar_dict[1][0]:
            pixel_range['E'] += num_black_pixels
        elif row_index < bar_dict[2][0]:
            pixel_range['C'] += num_black_pixels
        elif row_index < bar_dict[3][0]:
            pixel_range['A'] += num_black_pixels
        elif row_index < bar_dict[4][0]:
            pixel_range['F'] += num_black_pixels
        else:
            pixel_range['D'] += num_black_pixels

    # find note from pixel range
    total = sum(pixel_range.values())
    for key in pixel_range:
        pixel_range[key] = pixel_range[key]/total

    sorted_pixel_list = list(reversed(sorted(pixel_range.items(), key=lambda x: x[1])))

    key1 = ''
    key2 = ''
    note = ''
    if sorted_pixel_list[0][1] >= 0.55:
        note = sorted_pixel_list[0][0]
        if note == 'G' or note == 'E' or note == 'C':
            note += '5'
        else:
            note += '4'
    else:
        key1 = sorted_pixel_list[0][0]
        key2 = sorted_pixel_list[1][0]
        top_keys = (key1, key2)

        if sorted(top_keys) == ['E','G']:
            note = 'F5'
        elif sorted(top_keys) == ['C','E']:
            note = 'D5'
        elif sorted(top_keys) == ['A','C']:
            note = 'B4'
        elif sorted(top_keys) == ['A','F']:
            note = 'G4'
        else:
            note = 'E4'

    return note



def main():
    im = Image.open("../../test/image3.png")
    WIDTH = im.width
    LINE_VER_LEN = im.height
    pixel_list = c.make_pixel_list(list(im.getdata()))
    # gets the bar lines in format {0: (starting, ending)}
    bars = c.get_bar_coords(pixel_list)
    # for removing bars; list of all the lines that are a bar
    combined_bars = c.get_combined_bar_coords(pixel_list)
    # same as pixel_list but now vertical
    vertical_list = c.make_vertical_pixel_list(pixel_list)
    # remove staff bars
    c.remove_staffs(pixel_list, combined_bars)

    print(img_to_note(pixel_list, bars))

if __name__ == '__main__':
    main()
