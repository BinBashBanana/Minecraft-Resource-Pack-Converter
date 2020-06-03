#!/usr/bin/env python3
""" Convert Minecraft Resource Packs. """

import os
import shutil

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

entity_cat = [
    'all_black',
    'british_shorthair',
    'calico',
    'cat_collar',
    'persian',
    'ragdoll',
    'tabby',
    'white',
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
        shutil.rmtree(path)
        print("Successfully removed " + str(directory))
    elif PRINT_ERRORS:
        print(str(directory) + " does not exist!")


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
            items.append(material + '_sign')
            items.append(material + '_wall_sign')

    for file in blocks:
        remove('block', file + '.png')
        remove('block', file + '.png.mcmeta')

    remove('entity/banner', 'globe.png')
    remove('entity/cow', 'brown_mooshroom.png')
    remove('entity/horse/armor', 'horse_armor_leather.png')
    remove('entity/illager', 'pillager.png')
    remove('entity/illager', 'ravager.png')
    remove('entity/llama/decor', 'trader_llama.png')
    remove('entity/shield', 'globe.png')

    for file in entity_cat:
        remove('entity/cat', file + '.png')

    remove_dir('entity/bee/')
    remove_dir('entity/bell/')
    remove_dir('entity/conduit/')
    remove_dir('entity/fish/')
    remove_dir('entity/fox/')
    remove_dir('entity/panda/')
    remove_dir('entity/turtle/')

    for file in items:
        remove('item', file + '.png')
        remove('item', file + '.png.mcmeta')

    remaining_blocks = []
    block_dir = 'assets/minecraft/textures/block'
    for block in os.listdir(block_dir):
        block_path = os.path.join(block_dir, block)
        if os.path.isfile(block_path):
            remaining_blocks.append(block)

    remaining_items = []
    item_dir = 'assets/minecraft/textures/item'
    for item in os.listdir(item_dir):
        item_path = os.path.join(item_dir, item)
        if os.path.isfile(item_path):
            remaining_items.append(item)

    for name in search_blocks:
        for block in remaining_blocks:
            if name in block:
                remove('block', block)

    for name in search_items:
        for item in remaining_items:
            if name in item:
                remove('item', item)

def main():
    """ Main function. """
    remove_files()

if __name__ == '__main__':
    main()
