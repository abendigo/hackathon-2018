import os
from PIL import Image
from collections import Counter


# im = Image.open('/Users/daniel.pang/dev/hackathon-2018/sample/sample1.png')
# pic = im.load()

# vals = list(im.getdata())
# print(len(vals))
# print(im.size)
# print(vals)

def find_note(start, end, bar_dict):
    '''
    Hard coded key placements
    '''
    if start < bar_dict[0][0] and end_row < bar_dict[0][1]:
        return 'G'
    elif start < bar_dict[0][0] and end_row > bar_dict[0][1]
        return 'F'
    elif start > bar_dict[0][0] and

    for i in range(4):
        if

def img_to_note(pixels, bar_dict):
    '''
    Accepts a list of list representing the pixel data and a dict with keys being
    the row column and values being the tuples indicating the pixel row range
    Returns a musical note (output format TBD)
    '''
    # Input handling
    if len(pixels) != 600 or len(pixels[0] != 900):
        print 'Incorrect image size'
        return

    min = 105
    max = 140
    start_row = 0
    end_row = 0

    # Count number of dark pixels in each row (black is 1, white is 0)
    # If number of pixels is within threshold of min and max then a note has been found
    pixel_range = {'G':0, 'E': 0, 'C':0, 'A':0 'F':0, 'D':0}
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

    top_2 = dict(sorted(pixel_range.iteritems(), key=operator.itemgetter(1), reverse=True)[:2])
    print(top_2)





    if !found_note:
        print 'Could not find note'
        return

    note = find_note(start_row, end_row, bar_dict)
