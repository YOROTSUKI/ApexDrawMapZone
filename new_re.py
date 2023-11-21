import re
import json

with open(r'script.ent', 'r', encoding='UTF-8') as F:
    f = F.read()
    text = str("[" + f.replace("}", "},").replace('" "', '":"')\
                   .replace('"\n', '",').replace(",}", '}').replace("},\n]", '}]')+"]")
    pattern  = 'ENTITIES\d+ num_models=\d+'
    json_str = re.sub(pattern, '', text)
    with open('map_data.json', 'w', encoding='utf-8') as w_f:
        w_f.write(json_str)

with open('map_data.json', 'r', encoding='utf-8') as rf:
    read_json = eval(rf.read())

for js in read_json:
    if 'info_survival_invalid_end_zone' == js.get("editorclass"):
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_invalid_end_zone', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_circle_end_location' == js.get("editorclass"):
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_circle_end_location', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'script_survival_next_zone_survey_beacon' == js.get("editorclass"):
        origin = js.get('origin')
        with open('./map_data/script_survival_next_zone_survey_beacon', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{2}"' + "\n")

    if 'script_survival_survey_beacon' == js.get("editorclass"):
        origin = js.get('origin')
        with open('./map_data/script_survival_survey_beacon', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{2}"' + "\n")

    if 'info_survival_loot_zone' == js.get("editorclass") and js.get("zone_class") == 'zone_medium':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_zone_mid', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_loot_zone' == js.get("editorclass") and js.get("zone_class") == 'zone_low':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_zone_low', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_loot_zone' == js.get("editorclass") and js.get("zone_class") == 'zone_high':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_zone_high', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_loot_zone' == js.get("editorclass") and js.get("zone_class") == 'POI_Ultra':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_zone_ultra', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_loot_zone' == js.get("editorclass") and js.get("zone_class") == 'data_knife_vault':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_zone_data_knife_vault', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_loot_zone' == js.get("editorclass") and js.get("zone_class") == 'POI_sniper':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_zone_snpier', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_loot_zone' == js.get("editorclass") and js.get("zone_class") == 'POI_High':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_POI_High', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'info_survival_loot_hotzone' == js.get("editorclass") and js.get("zone_class") == 'zone_hotzone':
        origin = js.get('origin')
        script_radius = js.get("script_radius")
        with open('./map_data/info_survival_loot_zone_hotzone', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{script_radius}"' + "\n")

    if 'script_ref' == js.get("classname") and js.get("editorclass") == 'info_survival_weapon_location':
        origin = js.get('origin')
        # script_radius = js.get("script_radius")
        with open('./map_data/info_survival_weapon_location', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{5}"' + "\n")

    if js.get("script_name") == 'survival_lootbin':
        origin = js.get('origin')
        # script_radius = js.get("script_radius")
        with open('./map_data/survival_lootbin', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{5}"' + "\n")

    if js.get("editorclass") == 'script_survival_crafting_workbench_cluster':
        origin = js.get('origin')
        # script_radius = js.get("script_radius")
        with open('./map_data/script_survival_crafting_workbench_cluster', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{5}"' + "\n")

    if js.get("editorclass") == 'script_survival_crafting_harvester':
        origin = js.get('origin')
        # script_radius = js.get("script_radius")
        with open('./map_data/script_survival_crafting_harvester', 'a+', encoding='utf-8') as File:
            File.write(f'"origin" "{origin}"' + "\n")
            File.write(f'"script_radius" "{5}"' + "\n")

