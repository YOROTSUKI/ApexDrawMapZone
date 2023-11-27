import os

from draw_map import *
from settings import *

# English man? OR Chinese man?
is_en = True

if is_en:
    map_dice = {}
    for map_index, i in enumerate(tran.values()):
        print(f"{map_index + 1}. {i}")
        map_dice[map_index] = i
    input_map_index = int(input('input the map index').strip()) -1
    map_offset = offsets[map_dice[input_map_index]]
else:
    map_dice = {}
    for map_index, i in enumerate(tran.keys(), start=1):
        print(f"{map_index}. {i}")
        map_dice[map_index] = i

    input_map_index = int(input('选择数据对应的地图(输入序号即可)').strip())
    map_offset = offsets[tran[map_dice[input_map_index]]]


map_img_filename = './map_image/mp_rr_tropic_island_mu2.png'
# os.system('python new_re.py')
for data_file,data_color in color_ring.items():
    draw(map_img_filename, data_file, map_offset[0], map_offset[1], map_offset[2], map_offset[3],data_color)
