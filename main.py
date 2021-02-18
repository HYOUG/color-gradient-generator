from PIL import Image
from sys import argv

xy_size = tuple(argv[1:3])
rgb_start = tuple(argv[3:6])
rgb_end = tuple(argv[6:])

xy_size = (int(xy_size[0]), int(xy_size[1]))
rgb_start = (int(rgb_start[0]), int(rgb_start[1]), int(rgb_start[2]))
rgb_end = (int(rgb_end[0]), int(rgb_end[1]), int(rgb_end[2]))

R_GAP = (rgb_end[0] - rgb_start[0]) / xy_size[0]
G_GAP = (rgb_end[1] - rgb_start[1]) / xy_size[0]
B_GAP = (rgb_end[2] - rgb_start[2]) / xy_size[0]

im = Image.new("RGB", xy_size)

for x in range(xy_size[0]):
    column_color = (int(rgb_start[0] + R_GAP * x),
                    int(rgb_start[1] + G_GAP * x),
                    int(rgb_start[2] + B_GAP * x))
    for y in range(xy_size[1]):
        im.putpixel((x, y), column_color)

im.save("gradient.png")
im.close()

print("The gradient have been saved under gradient.png in the working directory")

if __name__ == "__main__":
    pass