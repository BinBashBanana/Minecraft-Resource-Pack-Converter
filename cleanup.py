#!/usr/bin/env python3
""" Remove files that doesn't exist in 1.12. """

import os
import shutil

PRINT_ERRORS = False

CORAL_TYPES = [
    'brain', 'bubble', 'fire', 'horn', 'tube',
    'dead_brain', 'dead_bubble', 'dead_fire', 'dead_horn', 'dead_tube'
]

TREE_MATERIALS = ['acacia', 'big_oak', 'birch', 'jungle', 'oak', 'spruce']

blocks = [
    'chain',
    'chiseled_nether_bricks',
    'cracked_nether_bricks',
    'crying_obsidian',
    'honeycomb_block',
    'lantern',
    'lily_of_the_valley',
    'nether_gold_ore',
    'nether_sprouts',
    'purple_shulker_box',
    'quartz_bricks',
    'shroomlight',
    'soul_soil',
    'soul_torch',
]

search_blocks = [
    'ancient_debris',
    'basalt',
    'blackstone',
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
    'crimson',
    'fletching_table',
    'grindstone',
    'honey_block',
    'jigsaw',
    'kelp',
    'lectern',
    'lodestone',
    'loom',
    'netherite',
    'respawn_anchor',
    'scaffolding',
    'seagrass',
    'sea_pickle',
    'smithing_table',
    'smoker',
    'soul_fire',
    'soul_lantern',
    'stonecutter',
    'stripped_',
    'target',
    'turtle_egg',
    'twisting_vines',
    'sweet_berry_bush',
    'warped_',
    'weeping_vines',
    'wither_rose',
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

gui_container = [
    'blast_furnace',
    'cartography_table',
    'gamemode_switcher',
    'grindstone',
    'loom',
    'smithing',
    'smoker',
    'stonecutter',
]

items = [
    'bamboo',
    'bell',
    'campfire',
    'chain',
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
    'music_disc_pigstep',
    'nautilus_shell',
    'nether_sprouts',
    'phantom_membrane',
    'scute',
    'sea_pickle',
    'seagrass',
    'soul_campfire',
    'soul_lantern',
    'suspicious_stew',
    'sweet_berries',
    'trident',
    'turtle_egg',
    'turtle_helmet',
]

search_items = [
    'banner_pattern',
    'crimson_',
    'crossbow',
    'honey',
    'kelp',
    'netherite',
    'warped_',
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


def remove_dir(directory, force=False):
    """ Remove directory. """
    path = gen_path(None, directory)
    if os.path.isdir(path):
        if force:
            shutil.rmtree(path)
        else:
            os.rmdir(path)
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
        if material != 'oak':
            blocks.append(material + '_trapdoor')
            items.append(material + '_sign')
            items.append(material + '_wall_sign')

    for file in blocks:
        remove('blocks', file + '.png')
        remove('blocks', file + '.png.mcmeta')

    remove('entity', 'dolphin.png')
    remove('entity', 'phantom.png')
    remove('entity', 'phantom_eyes.png')
    remove('entity', 'trident.png')
    remove('entity', 'trident_riptide.png')
    remove('entity', 'wandering_trader.png')

    for file in ['globe', 'piglin']:
        remove('entity/banner', file + '.png')
        remove('entity/shield', file + '.png')

    for file in entity_cat:
        remove('entity/cat', file + '.png')

    remove('entity/cow', 'brown_mooshroom.png')
    remove('entity/horse/armor', 'horse_armor_leather.png')
    remove('entity/illager', 'pillager.png')
    remove('entity/illager', 'ravager.png')

    for value in ['low', 'medium', 'high']:
        remove('entity/iron_golem', 'iron_golem_crackiness_' + value + '.png')

    remove('entity/llama/decor', 'trader_llama.png')
    remove('entity/zombie', 'drowned.png')
    remove('entity/zombie', 'drowned_outer_layer.png')

    remove('models/armor', 'turtle_layer_1.png')

    remove_dir('entity/bee/', force=True)
    remove_dir('entity/bell/', force=True)
    remove_dir('entity/conduit/', force=True)
    remove_dir('entity/fish/', force=True)
    remove_dir('entity/fox/', force=True)
    remove_dir('entity/hoglin/', force=True)
    remove_dir('entity/panda/', force=True)
    remove_dir('entity/piglin/', force=True)
    remove_dir('entity/signs/', force=True)
    remove_dir('entity/strider/', force=True)
    remove_dir('entity/turtle/', force=True)

    for file in ['accessibility', 'social_interactions']:
        remove('gui', file + '.png')

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
