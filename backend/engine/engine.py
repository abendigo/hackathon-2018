import os
from PIL import Image
from collections import Counter


# im = Image.open('/Users/daniel.pang/dev/hackathon-2018/sample/sample1.png')
# pic = im.load()

vals = list(im.getdata())
print(len(vals))
# print(im.size)
# print(vals)


def avg_space_between_bars(pixels, bar_dict):
    '''
    Accepts a list of list representing the pixel data and a dict with keys being
    the row column and values being the tuples indicating the pixel row range
    Returns the average number of pixel rows between two bars
    '''
    space = 0
    for key in bar_dict:
        if key == 1:
            pass
        else:
            space += (bar_dict[key][0] - bar_dict[key - 1][1])

    return space/4

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

    # Count number of dark pixels in each row (black is 1, white is 0)
    for row in pixels:
        pixel_counts = Counter(row[230:])
        # Check number of black pixels
