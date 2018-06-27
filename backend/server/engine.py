import os
from PIL import Image
from collections import Counter
import converter as c

def img_to_note(pixels, bar_dict):
    '''
    Accepts a list of lists representing the pixel data and a dict with keys being
    the bar number and values being the tuples indicating the pixel row range of the bars
    Returns a musical note in string format ex: 'D5'
    '''
    # Input handling
    if len(pixels) != 600 or len(pixels[0]) != 900:
        print('Incorrect image size')
        return ''

    # Count number of dark pixels in each row (black is 1, white is 0)
    # If number of pixels is within threshold of min and max then a note has been found
    pixel_range = {'G':0, 'E': 0, 'C':0, 'A':0, 'F':0, 'D':0}
    for row_index in range(len(pixels)):
        # Grab row of pixels, after the treble symbol
        row = pixels[row_index]
        pixel_counts = Counter(row[230:])
        # Count number of black pixels in the row
        num_black_pixels = pixel_counts[1]

        # Count the number of black pixels in each space between the bars
        # Store the number of pixels in a dict, indexed by the corresponding note
        # to that whitespace.
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

    # Sum the pixels between all the bars and divide each value in the dict
    # by the total
    total = sum(pixel_range.values())
    for key in pixel_range:
        pixel_range[key] = pixel_range[key]/total

    # Convert the dict into list, sorted by values from largest to smallest
    sorted_pixel_list = list(reversed(sorted(pixel_range.items(), key=lambda x: x[1])))

    key1 = ''
    key2 = ''
    note = ''
    # Finds the note
    # If the majortiy of the black pixels are between 2 bars, that is the note
    if sorted_pixel_list[0][1] >= 0.55:
        note = sorted_pixel_list[0][0]
        if note == 'G' or note == 'E' or note == 'C':
            note += '5'
        else:
            note += '4'
    # Otherwise, the note is on a bar (split on both sides of a bar)
    else:
        key1 = sorted_pixel_list[0][0]
        key2 = sorted_pixel_list[1][0]
        top_keys = (key1, key2)
        # Determine which line the note is on
        # Here we check which two whitespaces the note is in between
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

def engine(im):
    '''
    Accepts the im object to the image
    Returns the musical note as a list of tuples
    '''
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

    return [img_to_note(pixel_list, bars), 'Q']
