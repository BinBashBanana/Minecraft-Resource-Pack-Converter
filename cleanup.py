#!/usr/bin/env python3
""" Convert Minecraft Resource Packs. """

import os
#import shutil

PRINT_ERRORS = False

CORAL_TYPES = [
    'brain', 'bubble', 'fire', 'horn', 'tube',
    'dead_brain', 'dead_bubble', 'dead_fire', 'dead_horn', 'dead_tube'
]

TREE_MATERIALS = ['acacia', 'big_oak', 'birch', 'jungle', 'oak', 'spruce']

blocks = [
    'honeycomb_block',
    'lantern',
    'lily_of_the_valley',
    'purple_shulker_box',
]

search_blocks = [
    'bee_nest',
    'beehive',
    'blue_ice',
    'bamboo_',
    'barrel',
    'bell',
    'blast_furnace',
    'campfire',
    'cartography',
    'composter',
    'conduit',
    'cornflower',
    'fletching_table',
    'grindstone',
    'honey_block',
    'jigsaw',
    'kelp',
    'lectern',
    'loom',
    'scaffolding',
    'seagrass',
    'sea_pickle',
    'smithing_table',
    'smoker',
    'stonecutter',
    'turtle_egg',
    'sweet_berry_bush',
    'wither_rose',
]

entity_bee = [
    'bee_angry_nectar',
    'bee_angry',
    'bee_nectar',
    'bee',
    'bee_stinger',
]

entity_cat = [
    'all_black',
    'british_shorthair',
    'calico',
    'cat_collar',
    'jellie',
    'persian',
    'ragdoll',
    'tabby',
    'white',
]

entity_conduit = [
    'base',
    'break_particle',
    'cage',
    'closed_eye',
    'open_eye',
    'wind',
    'wind_vertical',
]

entity_fish = [
    'cod',
    'pufferfish',
    'salmon',
    'tropical_a',
    'tropical_b',
]

entity_fox = [
    'fox',
    'fox_sleep',
    'snow_fox',
    'snow_fox_sleep',
]

entity_panda = [
    'aggressive_panda',
    'brown_panda',
    'lazy_panda',
    'panda',
    'playful_panda',
    'weak_panda',
    'worried_panda',
]

entity_signs = []

gui_container = [
    'blast_furnace',
    'cartography_table',
    'grindstone',
    'loom',
    'smoker',
    'stonecutter',
]

items = [
    'bamboo',
    'bell',
    'campfire',
    'cod_bucket',
    'pufferfish_bucket',
    'salmon_bucket',
    'tropical_fish_bucket',
    'black_dye',
    'blue_dye',
    'brown_dye',
    'white_dye',
    'heart_of_the_sea',
    'lantern',
    'leather_horse_armor',
    'nautilus_shell',
    'phantom_membrane',
    'scute',
    'sea_pickle',
    'seagrass',
    'suspicious_stew',
    'sweet_berries',
    'trident',
    'turtle_egg',
    'turtle_helmet',
]

search_items = [
    'banner_pattern',
    'crossbow',
    'honey',
    'kelp',
]


def gen_path(subdir, item):
    """ Generate path. """
    if subdir is None:
        return 'assets/minecraft/textures/{}'.format(item)
    return 'assets/minecraft/textures/{}/{}'.format(subdir, item)


def remove(subdir, file):
    """ Remove file. """
    path = gen_path(subdir, file)
    if os.path.isfile(path):
        os.remove(path)
        print("Successfully removed " + str(file))
    elif PRINT_ERRORS:
        print(str(file) + " does not exist!")


def remove_dir(directory):
    """ Remove directory. """
    path = gen_path(None, directory)
    if os.path.isdir(path):
        os.rmdir(path)
        #shutil.rmtree(path)
        print("Successfully removed directory " + str(directory))
    elif PRINT_ERRORS:
        print("The directory " + str(directory) + " does not exist!")


def remove_files():
    """ Remove unwanted files. """
    for coral_type in CORAL_TYPES:
        blocks.append(coral_type + '_coral')
        blocks.append(coral_type + '_coral_block')
        blocks.append(coral_type + '_coral_fan')

    for material in TREE_MATERIALS:
        if material == 'big_oak':
            material = 'dark_oak'
        blocks.append('stripped_' + material + '_log')
        blocks.append('stripped_' + material + '_log_top')
        if material != 'oak':
            blocks.append(material + '_trapdoor')
            entity_signs.append(material)
            items.append(material + '_sign')
            items.append(material + '_wall_sign')

    for file in blocks:
        remove('blocks', file + '.png')
        remove('blocks', file + '.png.mcmeta')

    for i in range(6):
        entity_fish.append('tropical_a_pattern_' + str(i + 1))
        entity_fish.append('tropical_b_pattern_' + str(i + 1))

    remove('entity/banner', 'globe.png')
    remove('entity/cow', 'brown_mooshroom.png')
    remove('entity/horse/armor', 'horse_armor_leather.png')
    remove('entity/illager', 'pillager.png')
    remove('entity/illager', 'ravager.png')
    for value in ['low', 'medium', 'high']:
        remove('entity/iron_golem', 'iron_golem_crackiness_' + value + '.png')
    remove('entity/llama/decor', 'trader_llama.png')
    remove('entity/shield', 'globe.png')
    remove('entity/zombie', 'drowned.png')
    remove('entity/zombie', 'drowned_outer_layer.png')
    remove('entity', 'dolphin.png')
    remove('entity', 'phantom.png')
    remove('entity', 'phantom_eyes.png')
    remove('entity', 'trident.png')
    remove('entity', 'trident_riptide.png')
    remove('entity', 'wandering_trader.png')
    remove('models/armor', 'turtle_layer_1.png')

    for file in entity_bee:
        remove('entity/bee', file + '.png')
    remove_dir('entity/bee/')

    remove('entity/bell', 'bell_body.png')
    remove_dir('entity/bell/')

    for file in entity_cat:
        remove('entity/cat', file + '.png')

    for file in entity_conduit:
        remove('entity/conduit', file + '.png')
        remove('entity/conduit', file + '.png.mcmeta')
    remove_dir('entity/conduit/')

    for file in entity_fish:
        remove('entity/fish', file + '.png')
    remove_dir('entity/fish/')

    for file in entity_fox:
        remove('entity/fox', file + '.png')
    remove_dir('entity/fox/')

    for file in entity_panda:
        remove('entity/panda', file + '.png')
    remove_dir('entity/panda/')

    for file in entity_signs:
        remove('entity/signs', file + '.png')
    remove_dir('entity/signs/')

    remove('entity/turtle', 'big_sea_turtle.png')
    remove_dir('entity/turtle/')

    for file in gui_container:
        remove('gui/container', file + '.png')

    for file in items:
        remove('items', file + '.png')
        remove('items', file + '.png.mcmeta')

    remove('map', 'map_background_checkerboard.png')

    remaining_blocks = []
    block_dir = 'assets/minecraft/textures/blocks'
    for block in os.listdir(block_dir):
        block_path = os.path.join(block_dir, block)
        if os.path.isfile(block_path):
            remaining_blocks.append(block)

    remaining_items = []
    item_dir = 'assets/minecraft/textures/items'
    for item in os.listdir(item_dir):
        item_path = os.path.join(item_dir, item)
        if os.path.isfile(item_path):
            remaining_items.append(item)

    for name in search_blocks:
        for block in remaining_blocks:
            if name in block:
                remove('blocks', block)

    for name in search_items:
        for item in remaining_items:
            if name in item:
                remove('items', item)

def main():
    """ Main function. """
    remove_files()

if __name__ == '__main__':
    main()
