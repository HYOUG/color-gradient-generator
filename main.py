#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by "HYOUG"

from PIL import Image
from sys import argv
from os import getcwd


def gen_gradient(xy_size: tuple = (1000, 1000), rgb_start: tuple = (0, 0, 0), rgb_end: tuple = (255, 255, 255), fp: str = f"{getcwd()}/gradient.png") -> None:
    """Generate a gradient from the given format and the two RGB given"""

    xy_size = (int(xy_size[0]), int(xy_size[1]))
    rgb_start = (int(rgb_start[0]), int(rgb_start[1]), int(rgb_start[2]))
    rgb_end = (int(rgb_end[0]), int(rgb_end[1]), int(rgb_end[2]))

    r_gap = (rgb_end[0] - rgb_start[0]) / xy_size[0]
    g_gap = (rgb_end[1] - rgb_start[1]) / xy_size[0]
    b_gap = (rgb_end[2] - rgb_start[2]) / xy_size[0]

    im = Image.new("RGB", xy_size)

    for x in range(xy_size[0]):
        column_color = (int(rgb_start[0] + r_gap * x),
                        int(rgb_start[1] + g_gap * x),
                        int(rgb_start[2] + b_gap * x))
        for y in range(xy_size[1]):
            im.putpixel((x, y), column_color)

    im.save(fp)
    im.close()


if __name__ == "__main__":
    xy_size = tuple(argv[1:3])
    rgb_start = tuple(argv[3:6])
    rgb_end = tuple(argv[6:])

    gen_gradient(xy_size, rgb_start, rgb_end)