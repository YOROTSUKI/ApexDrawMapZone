from draw_map import *
from settings import *


# English man? OR Chinese man?
is_en = True

if is_en:
    map_dice = {}
    for map_index, i in enumerate(tran.values()):
        print(f"{map_index+1}. {i}")
        map_dice[map_index] = i
    input_map_index = int(input('input the map index').strip()) - 1
    map_offset = offsets[map_dice[input_map_index]]
    print(map_offset)
else:
    map_dice = {}
    for map_index, i in enumerate(tran.keys(),start=1):
        print(f"{map_index}. {i}")
        map_dice[map_index] = i

    input_map_index = int(input('选择数据对应的地图(输入序号即可)').strip()) - 1
    map_offset = offsets[tran[map_dice[input_map_index]]]
    print(map_offset)