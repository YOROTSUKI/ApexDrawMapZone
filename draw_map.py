import cv2
import re


from settings import *


def draw(img_file,file_name, x_offset, y_offset, x_adj_factor, y_adj_factor,color):
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

    with open('./map_data/'+file_name) as f:
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

                # this pair is done, push into a map
                coordinates.append(thisline)
                thisline = InvalidEndZone()
    output_file = img_file.replace(".png",'').replace("map_image",'image_result')+'_'+output_file_name[file_name]+".png"
    if file_name not in is_need_special:
        img = cv2.imread(f'{img_file}')
    else:
        img = cv2.imread(output_file)
    if file_name not in is_use_special_size:
        for restriction in coordinates:
            x_coord = int(((restriction.x + abs(max_x)) / scale_x) / x_adj_factor)
            y_coord = int(((restriction.y + abs(max_y)) / scale_y) / y_adj_factor)
            img = cv2.circle(img, (x_coord + x_offset, y_coord + y_offset), int(restriction.radius / 24), color, 7)
    else:
        for restriction in coordinates:
            x_coord = int(((restriction.x + abs(max_x)) / scale_x) / x_adj_factor)
            y_coord = int(((restriction.y + abs(max_y)) / scale_y) / y_adj_factor)
            img = cv2.circle(img, (x_coord + x_offset, y_coord + y_offset), int(restriction.radius / 24), color, 20)

    cv2.imwrite(output_file, img)
