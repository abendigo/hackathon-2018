import os
from PIL import Image
from collections import Counter

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
