#!/usr/bin/env python3
""" Convert Minecraft Resource Packs. """

import os

PRINT_ERRORS = False

CORAL_TYPES = [
    "brain", "bubble", "fire", "horn", "tube",
    "dead_brain", "dead_bubble", "dead_fire", "dead_horn", "dead_tube"
]

TREE_MATERIALS = ["acacia", "big_oak", "birch", "jungle", "oak", "spruce"]

blockstates = [

]

textures_blocks = [
    "honeycomb_block",
    "lantern",
    "lily_of_the_valley",
]

search_blocks = [
    "bee_nest",
    "beehive",
    "blue_ice",
    "bamboo_",
    "barrel",
    "bell",
    "blast_furnace",
    "campfire",
    "cartography",
    "composter",
    "conduit",
    "cornflower",
    "fletching_table",
    "grindstone",
    "honey_block",
    "jigsaw",
    "kelp",
    "lectern",
    "loom",
    "scaffolding",
    "seagrass",
    "sea_pickle",
    "smithing_table",
    "smoker",
    "stonecutter",
    "turtle_egg",
    "sweet_berry_bush",
    "wither_rose",
]

textures_items = [
    "bamboo",
    "bell",
    "campfire",
    "cod_bucket",
    "pufferfish_bucket",
    "salmon_bucket",
    "tropical_fish_bucket",
    "black_dye",
    "blue_dye",
    "brown_dye",
    "white_dye",
    "heart_of_the_sea",
    "lantern",
    "leather_horse_armor",
    "nautilus_shell",
    "phantom_membrane",
    "scute",
    "sea_pickle",
    "seagrass",
    "suspicious_stew",
    "sweet_berries",
    "trident",
    "turtle_egg",
    "turtle_helmet",
]

search_items = [
    "banner_pattern",
    "crossbow",
    "honey",
    "kelp",
]


def gen_path(subdir, item):
    """ Generate path. """
    return "assets/minecraft/{}/{}".format(subdir, item)


def remove(subdir, file):
    """ Remove file. """
    path = gen_path(subdir, file)
    if os.path.isfile(path):
        os.remove(path)
        print("Successfully removed " + str(file))
    elif PRINT_ERRORS:
        print(str(file) + " does not exist!")


def remove_files():
    """ Remove unwanted files. """
    for coral_type in CORAL_TYPES:
        textures_blocks.append(coral_type + "_coral")
        textures_blocks.append(coral_type + "_coral_block")
        textures_blocks.append(coral_type + "_coral_fan")

    for material in TREE_MATERIALS:
        if material == "big_oak":
            material = "dark_oak"
        textures_blocks.append("stripped_" + material + "_log")
        textures_blocks.append("stripped_" + material + "_log_top")
        if material != "oak":
            blockstates.append(material + "_button")
            blockstates.append(material + "_pressure_plate")
            blockstates.append(material + "_sign")
            textures_blocks.append(material + "_trapdoor")
            textures_items.append(material + "_sign")

    print("[blockstates]")
    for file in blockstates:
        remove("blockstates", file + ".json")

    print("[textures]")
    print("[../block]")
    for file in textures_blocks:
        remove("textures/block", file + ".png")
        remove("textures/block", file + ".png.mcmeta")

    print("[../item]")
    for file in textures_items:
        remove("textures/item", file + ".png")
        remove("textures/item", file + ".png.mcmeta")

    remaining_blocks = []
    block_dir = "assets/minecraft/textures/block"
    for block in os.listdir(block_dir):
        block_path = os.path.join(block_dir, block)
        if os.path.isfile(block_path):
            remaining_blocks.append(block)

    remaining_items = []
    item_dir = "assets/minecraft/textures/item"
    for item in os.listdir(item_dir):
        item_path = os.path.join(item_dir, item)
        if os.path.isfile(item_path):
            remaining_items.append(item)

    for name in search_blocks:
        for block in remaining_blocks:
            if name in block:
                remove("textures/block", block)

    for name in search_items:
        for item in remaining_items:
            if name in item:
                remove("textures/item", item)

def main():
    """ Main function. """
    remove_files()

if __name__ == '__main__':
    main()
