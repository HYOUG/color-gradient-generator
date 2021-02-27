#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by "HYOUG"

from PIL import Image
from sys import argv
from os import getcwd


def gen_gradient(xy_size: tuple = (1000, 1000), rgb_start: tuple = (0, 0, 0), rgb_end: tuple = (255, 255, 255), fp: str = f"{getcwd()}/gradient.png") -> None:
    """Generate a gradient from the given format and the two RGB given"""

    xy_size = [int(item) for item in xy_size]                                       # convert the function's arguments
    rgb_start = [int(item) for item in rgb_start]                                   # //
    rgb_end = [int(item) for item in rgb_end]                                       # //

    r_gap = (rgb_end[0] - rgb_start[0]) / xy_size[0]                                # calculate the gap of the "R" value for every column
    g_gap = (rgb_end[1] - rgb_start[1]) / xy_size[0]                                # calculate the gap of the "G" value for every column
    b_gap = (rgb_end[2] - rgb_start[2]) / xy_size[0]                                # calculate the gap of the "B" value for every column

    im = Image.new("RGB", xy_size)                                                  # create a new picture (RGB format, with the given XY size)

    for x in range(xy_size[0]):                                                     # iterate the x value of the picture
        column_color = (int(rgb_start[0] + r_gap * x),                              # calculate the RGB value of the column
                        int(rgb_start[1] + g_gap * x),
                        int(rgb_start[2] + b_gap * x))
        for y in range(xy_size[1]):                                                 # iterate the y value of the image
            im.putpixel((x, y), column_color)                                       # apply the RGB value on the whole column

    im.save(fp)                                                                     # save the generated picture
    im.close()                                                                      # close the picture's editing


if __name__ == "__main__":                                                          # check if the script is the main program
    xy_size = tuple(argv[1:3])                                                      # fatch command line arguments
    rgb_start = tuple(argv[3:6])                                                    # //
    rgb_end = tuple(argv[6:])                                                       # //

    gen_gradient(xy_size, rgb_start, rgb_end)                                       # call the gen_gradient function with the command line arguments