#!/usr/bin/env python3
""" Convert Minecraft Resource Packs. """

import os

minecraft_version = "1.14"
pack_format = 4

blockstates = {
    "wood_button": "oak_button",
    "wood_pressure_plate": "oak_pressure_plate",
    "sign": "oak_sign",
}

COLORS = [
    "black", "blue", "brown", "cyan", "gray", "green", "light_blue", "lime",
    "magenta", "orange", "pink", "purple", "red", "silver", "white", "yellow"
]

TREE_MATERIALS = ["acacia", "big_oak", "birch", "jungle", "oak", "spruce"]

block_dict = {
    "anvil_base": "anvil",
    "anvil_top_damaged_0": "anvil_top",
    "anvil_top_damaged_1": "chipped_anvil_top",
    "anvil_top_damaged_2": "damaged_anvil_top",
    "brick": "bricks",
    "cobblestone_mossy": "mossy_cobblestone",
    "comparator_off": "comparator",
    "deadbush": "dead_bush",
    "dirt_podzol_side": "podzol_side",
    "dirt_podzol_top": "podzol_top",
    "dispenser_front_horizontal": "dispenser_front",
    "door_iron_lower": "iron_door_bottom",
    "door_iron_upper": "iron_door_top",
    "itemframe_background": "item_frame",
    "double_plant_fern_bottom": "large_fern_bottom",
    "double_plant_fern_top": "large_fern_top",
    "double_plant_grass_bottom": "tall_grass_bottom",
    "double_plant_grass_top": "tall_grass_top",
    "double_plant_paeonia_bottom": "peony_bottom",
    "double_plant_paeonia_top": "peony_top",
    "double_plant_rose_bottom": "rose_bush_bottom",
    "double_plant_rose_top": "rose_bush_top",
    "double_plant_sunflower_back": "sunflower_back",
    "double_plant_sunflower_bottom": "sunflower_bottom",
    "double_plant_sunflower_front": "sunflower_front",
    "double_plant_sunflower_top": "sunflower_top",
    "double_plant_syringa_bottom": "lilac_bottom",
    "double_plant_syringa_top": "lilac_top",
    "dropper_front_horizontal": "dropper_front",
    "end_bricks": "end_stone_bricks",
    "endframe_eye": "end_portal_frame_eye",
    "endframe_side": "end_portal_frame_side",
    "endframe_top": "end_portal_frame_top",
    "farmland_dry": "farmland",
    "farmland_wet": "farmland_moist",
    "fire_layer_0": "fire_0",
    "fire_layer_1": "fire_1",
    "flower_allium": "allium",
    "flower_blue_orchid": "blue_orchid",
    "flower_dandelion": "dandelion",
    "flower_houstonia": "azure_bluet",
    "flower_oxeye_daisy": "oxeye_daisy",
    "flower_rose": "poppy",
    "flower_tulip_orange": "orange_tulip",
    "flower_tulip_pink": "pink_tulip",
    "flower_tulip_red": "red_tulip",
    "flower_tulip_white": "white_tulip",
    "furnace_front_off": "furnace_front",
    "grass_side": "grass_block_side",
    "grass_side_overlay": "grass_block_side_overlay",
    "grass_side_snowed": "grass_block_snow",
    "grass_top": "grass_block_top",
    "hardened_clay": "terracotta",
    "ice_packed": "packed_ice",
    "redstone_lamp_off": "redstone_lamp",
    "melon_stem_connected": "attached_melon_stem",
    "melon_stem_disconnected": "melon_stem",
    "mob_spawner": "spawner",
    "mushroom_block_skin_brown": "brown_mushroom_block",
    "mushroom_block_skin_red": "red_mushroom_block",
    "mushroom_block_skin_stem": "mushroom_stem",
    "mushroom_brown": "brown_mushroom",
    "mushroom_red": "red_mushroom",
    "nether_brick": "nether_bricks",
    "noteblock": "note_block",
    "observer_back_lit": "observer_back_on",
    "piston_top_normal": "piston_top",
    "portal": "nether_portal",
    "prismarine_dark": "dark_prismarine",
    "prismarine_rough": "prismarine",
    "pumpkin_face_off": "carved_pumpkin",
    "pumpkin_face_on": "jack_o_lantern",
    "pumpkin_stem_connected": "attached_pumpkin_stem",
    "pumpkin_stem_disconnected": "pumpkin_stem",
    "purple_stained_glass": "purple_stained_glass",
    "purpur_pillar": "purpur_pillar",
    "purpur_pillar_top": "purpur_pillar_top",
    "quartz_block_chiseled": "chiseled_quartz_block",
    "quartz_block_chiseled_top": "chiseled_quartz_block_top",
    "quartz_block_lines": "quartz_pillar",
    "quartz_block_lines_top": "quartz_pillar_top",
    "quartz_ore": "nether_quartz_ore",
    "rail_activator": "activator_rail",
    "rail_activator_powered": "activator_rail_on",
    "rail_detector": "detector_rail",
    "rail_detector_powered": "detector_rail_on",
    "rail_golden": "powered_rail",
    "rail_golden_powered": "powered_rail_on",
    "rail_normal": "rail",
    "rail_normal_turned": "rail_corner",
    "red_nether_brick": "red_nether_bricks",
    "red_sandstone_carved": "chiseled_red_sandstone",
    "red_sandstone_normal": "red_sandstone",
    "red_sandstone_smooth": "cut_red_sandstone",
    "redstone_torch_on": "redstone_torch",
    "reeds": "sugar_cane",
    "repeater_off": "repeater",
    "sandstone_carved": "chiseled_sandstone",
    "sandstone_normal": "sandstone",
    "sandstone_smooth": "cut_sandstone",
    "slime": "slime_block",
    "sponge_wet": "wet_sponge",
    "stone_andesite": "andesite",
    "stone_andesite_smooth": "polished_andesite",
    "stone_diorite": "diorite",
    "stone_diorite_smooth": "polished_diorite",
    "stone_granite": "granite",
    "stone_granite_smooth": "polished_granite",
    "stonebrick": "stone_bricks",
    "stonebrick_carved": "chiseled_stone_bricks",
    "stonebrick_cracked": "cracked_stone_bricks",
    "stonebrick_mossy": "mossy_stone_bricks",
    "stone_slab_top": "smooth_stone",
    "stone_slab_side": "smooth_stone_slab_side",
    "tallgrass": "grass",
    "torch_on": "torch",
    "trip_wire_source": "tripwire_hook",
    "waterlily": "lily_pad",
    "web": "cobweb",
    "trapdoor": "oak_trapdoor",
    "trip_wire": "tripwire",
}

item_dict = {
    "apple_golden": "golden_apple",
    "beef_cooked": "cooked_beef",
    "beef_raw": "beef",
    "book_enchanted": "enchanted_book",
    "book_normal": "book",
    "book_writable": "writable_book",
    "book_written": "written_book",
    "bow_standby": "bow",
    "bucket_empty": "bucket",
    "bucket_lava": "lava_bucket",
    "bucket_milk": "milk_bucket",
    "bucket_water": "water_bucket",
    "carrot_golden": "golden_carrot",
    "chicken_cooked": "cooked_chicken",
    "chicken_raw": "chicken",
    "chorus_fruit_popped": "popped_chorus_fruit",
    "door_iron": "iron_door",
    "dye_powder_black": "ink_sac",
    "dye_powder_blue": "lapis_lazuli",
    "dye_powder_brown": "cocoa_beans",
    "dye_powder_cyan": "cyan_dye",
    "dye_powder_gray": "gray_dye",
    "dye_powder_green": "cactus_green",
    "dye_powder_light_blue": "light_blue_dye",
    "dye_powder_lime": "lime_dye",
    "dye_powder_magenta": "magenta_dye",
    "dye_powder_orange": "orange_dye",
    "dye_powder_pink": "pink_dye",
    "dye_powder_purple": "purple_dye",
    "dye_powder_red": "rose_red",
    "dye_powder_silver": "light_gray_dye",
    "dye_powder_white": "bone_meal",
    "dye_powder_yellow": "dandelion_yellow",
    "fireball": "fire_charge",
    "fireworks": "firework_rocket",
    "fireworks_charge": "firework_star",
    "fireworks_charge_overlay": "firework_star_overlay",
    "fish_clownfish_raw": "tropical_fish",
    "fish_cod_cooked": "cooked_cod",
    "fish_cod_raw": "cod",
    "fish_pufferfish_raw": "pufferfish",
    "fish_salmon_cooked": "cooked_salmon",
    "fish_salmon_raw": "salmon",
    "fishing_rod_uncast": "fishing_rod",
    "gold_axe": "golden_axe",
    "gold_boots": "golden_boots",
    "gold_chestplate": "golden_chestplate",
    "gold_helmet": "golden_helmet",
    "gold_hoe": "golden_hoe",
    "gold_horse_armor": "golden_horse_armor",
    "gold_leggings": "golden_leggings",
    "gold_pickaxe": "golden_pickaxe",
    "gold_shovel": "golden_shovel",
    "gold_sword": "golden_sword",
    "map_empty": "map",
    "map_filled": "filled_map",
    "map_filled_markings": "filled_map_markings",
    "melon": "melon_slice",
    "melon_speckled": "glistering_melon_slice",
    "minecart_chest": "chest_minecart",
    "minecart_command_block": "command_block_minecart",
    "minecart_furnace": "furnace_minecart",
    "minecart_hopper": "hopper_minecart",
    "minecart_normal": "minecart",
    "minecart_tnt": "tnt_minecart",
    "mutton_cooked": "cooked_mutton",
    "mutton_raw": "mutton",
    "netherbrick": "nether_brick",
    "porkchop_cooked": "cooked_porkchop",
    "porkchop_raw": "porkchop",
    "potato_baked": "baked_potato",
    "potato_poisonous": "poisonous_potato",
    "potion_bottle_drinkable": "glass_bottle",
    "potion_bottle_empty": "potion",
    "potion_bottle_lingering": "lingering_potion",
    "potion_bottle_splash": "splash_potion",
    "rabbit_cooked": "cooked_rabbit",
    "rabbit_raw": "rabbit",
    "record_11": "music_disc_11",
    "record_13": "music_disc_13",
    "record_blocks": "music_disc_blocks",
    "record_cat": "music_disc_cat",
    "record_chirp": "music_disc_chirp",
    "record_far": "music_disc_far",
    "record_mall": "music_disc_mall",
    "record_mellohi": "music_disc_mellohi",
    "record_stal": "music_disc_stal",
    "record_strad": "music_disc_strad",
    "record_wait": "music_disc_wait",
    "record_ward": "music_disc_ward",
    "redstone_dust": "redstone",
    "seeds_melon": "melon_seeds",
    "seeds_pumpkin": "pumpkin_seeds",
    "seeds_wheat": "wheat_seeds",
    "sign": "oak_sign",
    "reeds": "sugar_cane",
    "slimeball": "slime_ball",
    "spider_eye_fermented": "fermented_spider_eye",
    "totem": "totem_of_undying",
    "wood_axe": "wooden_axe",
    "wood_hoe": "wooden_hoe",
    "wood_pickaxe": "wooden_pickaxe",
    "wood_shovel": "wooden_shovel",
    "wood_sword": "wooden_sword",
    "wooden_armorstand": "armor_stand",
}


def gen_path(subdir, item):
    """ Generate path. """
    return "assets/minecraft/{}/{}".format(subdir, item)


def convert(subdir, source, target, extension):
    """ Rename source to target. """
    source_path = gen_path(subdir, source + extension)
    target_path = gen_path(subdir, target + extension)
    source_path_mcmeta = source_path + ".mcmeta"
    target_path_mcmeta = target_path + ".mcmeta"
    if os.path.isfile(source_path):
        # try:
        os.rename(source_path, target_path)
        if os.path.isfile(source_path_mcmeta):
            os.rename(source_path_mcmeta, target_path_mcmeta)
            print("Successfully converted "
                  + str(source + ".mcmeta") + " to " + str(target + ".mcmeta"))
        print("Successfully converted " + str(source) + " to " + str(target))
        # except:
        #     print("An error occured converting " + str(source) + " to " + str(target))
    else:
        print(str(source_path) + " does not exist!")


def convert_resourcepack():
    """ Convert Resource Pack. """
    for i in range(3):
        block_dict["cocoa_stage_" + str(i)] = "cocoa_stage" + str(i)
        block_dict["nether_wart_stage_" + str(i)] = "nether_wart_stage" + str(i)

    for i in range(4):
        block_dict["beetroots_stage_" + str(i)] = "beetroots_stage" + str(i)
        block_dict["carrots_stage_" + str(i)] = "carrots_stage" + str(i)
        block_dict["potatoes_stage_" + str(i)] = "potatoes_stage" + str(i)

    for i in range(8):
        block_dict["wheat_stage_" + str(i)] = "wheat_stage" + str(i)

    for color in COLORS:
        new_color = color
        if new_color == "silver":
            new_color = "light_gray"
        block_dict["concrete_" + color] = new_color + "_concrete"
        block_dict["concrete_powder_" + color] = new_color + "_concrete_powder"
        block_dict["glass_" + color] = new_color + "_stained_glass"
        block_dict["glass_pane_top_" + color] = new_color + "_stained_glass_pane_top"
        block_dict["glazed_terracotta_" + color] = new_color + "_glazed_terracotta"
        block_dict["hardened_clay_stained_" + color] = new_color + "_terracotta"
        if color == "purple":
            block_dict["shulker_top_" + color] = "shulker_box"
        else:
            block_dict["shulker_top_" + color] = new_color + "_shulker_box"
        block_dict["wool_colored_" + color] = new_color + "_wool"

    if minecraft_version == "1.14":
        item_dict["dye_powder_green"] = "green_dye"
        item_dict["dye_powder_red"] = "red_dye"
        item_dict["dye_powder_yellow"] = "yellow_dye"

    print("[blockstates]")
    for key, value in blockstates.items():
        convert("blockstates", value, key, ".json")

    print("[textures]")
    print("[../block]")
    for key, value in block_dict.items():
        convert("textures/block", value, key,".png")

    print("[../item]")
    for key, value in item_dict.items():
        convert("textures/item", value, key, ".png")


def main():
    """ Main function. """

    for material in TREE_MATERIALS:
        new_material = material
        if material == "big_oak":
            new_material = "dark_oak"
        door_material = new_material
        if door_material == "oak":
            door_material = "wood"
        sapling_material = material
        if sapling_material == "big_oak":
            sapling_material = "roofed_oak"
        block_dict["door_" + door_material + "_lower"] = new_material + "_door_bottom"
        block_dict["door_" + door_material + "_upper"] = new_material + "_door_top"
        block_dict["leaves_" + material] = new_material + "_leaves"
        block_dict["log_" + material] = new_material + "_log"
        block_dict["log_" + material + "_top"] = new_material + "_log_top"
        block_dict["planks_" + material] = new_material + "_planks"
        block_dict["sapling_" + sapling_material] = new_material + "_sapling"
        item_dict["door_" + door_material] = new_material + "_door"
    convert_resourcepack()
    # TODO: Rename block and item folder


if __name__ == '__main__':
    main()
