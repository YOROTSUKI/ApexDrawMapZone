import cv2
import re
import os

def draw(data_file, input_img, output_img, x_offset, y_offset, x_adj_factor, y_adj_factor):
    coordinates = []

    max_x = 45056
    max_y = 45055
    min_x = -45056
    min_y = -45055

    map_x = 4096
    map_y = 4096

    scale_x = ((abs(min_x) + max_x + x_offset) / map_x)
    scale_y = ((abs(min_y) + max_y + y_offset) / map_y)

    class InvalidEndZone:
        x = None
        y = None
        z = None
        radius = None

    with open(data_file) as f:
        thisline = InvalidEndZone()
        for line in f.readlines():
            if "origin" in line:
                result = re.search('origin" "(.*)"', line)
                xyz = result.group(1).split()
                thisline.x = int(float(xyz[0]))
                thisline.y = int(float(xyz[1]) * -1)
                thisline.z = int(float(xyz[2]))

            if "script_radius" in line:
                result = re.search('script_radius" "(.*)"', line)
                thisline.radius = int(result.group(1))
                coordinates.append(thisline)
                thisline = InvalidEndZone()

    img = cv2.imread(input_img)

    for restriction in coordinates:
        x_coord = int(((restriction.x + abs(max_x)) / scale_x) / x_adj_factor)
        y_coord = int(((restriction.y + abs(max_y)) / scale_y) / y_adj_factor)
        img = cv2.circle(img, (x_coord + x_offset, y_coord + y_offset), int(restriction.radius / 24), (0, 250, 0), 7)

    cv2.imwrite(output_img, img)

data_file_list = os.listdir('./map_data')
for i in data_file_list:
    print(i)