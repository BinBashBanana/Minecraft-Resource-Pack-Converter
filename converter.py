import os, sys, shutil, json, datetime

# Format: Key: 1.12, Value: 1.13

dirDict = {
	"textures/blocks/": "textures/block/",
	"textures/items/": "textures/item/",
	"textures/entity/endercrystal/": "textures/entity/end_crystal/"
}

blockDict = {
	"anvil_base": "anvil",
	"anvil_slightly_damaged": "chipped_anvil",
	"anvil_top_damaged_0": "anvil_top",
	"anvil_top_damaged_1": "chipped_anvil_top",
	"anvil_top_damaged_2": "damaged_anvil_top",
	"anvil_very_damaged": "damaged_anvil",
	"beetroots_stage_0": "beetroots_stage0",
	"beetroots_stage_1": "beetroots_stage1",
	"beetroots_stage_2": "beetroots_stage2",
	"beetroots_stage_3": "beetroots_stage3",
	"brick": "bricks",
	"carrots_stage_0": "carrots_stage0",
	"carrots_stage_1": "carrots_stage1",
	"carrots_stage_2": "carrots_stage2",
	"carrots_stage_3": "carrots_stage3",
	"cobblestone_mossy": "mossy_cobblestone",
	"cocoa_stage_0": "cocoa_stage0",
	"cocoa_stage_1": "cocoa_stage1",
	"cocoa_stage_2": "cocoa_stage2",
	"comparator_off": "comparator",
	"concrete_light_blue": "light_blue_concrete",
	"concrete_black": "black_concrete",
	"concrete_blue": "blue_concrete",
	"concrete_brown": "brown_concrete",
	"concrete_cyan": "cyan_concrete",
	"concrete_gray": "gray_concrete",
	"concrete_green": "green_concrete",
	"concrete_lime": "lime_concrete",
	"concrete_magenta": "magenta_concrete",
	"concrete_orange": "orange_concrete",
	"concrete_pink": "pink_concrete",
	"concrete_powder_black": "black_concrete_powder",
	"concrete_powder_blue": "blue_concrete_powder",
	"concrete_powder_brown": "brown_concrete_powder",
	"concrete_powder_cyan": "cyan_concrete_powder",
	"concrete_powder_gray": "gray_concrete_powder",
	"concrete_powder_green": "green_concrete_powder",
	"concrete_powder_light_blue": "light_blue_concrete_powder",
	"concrete_powder_lime": "lime_concrete_powder",
	"concrete_powder_magenta": "magenta_concrete_powder",
	"concrete_powder_orange": "orange_concrete_powder",
	"concrete_powder_pink": "pink_concrete_powder",
	"concrete_powder_purple": "purple_concrete_powder",
	"concrete_powder_red": "red_concrete_powder",
	"concrete_powder_silver": "light_gray_concrete_powder",
	"concrete_powder_white": "white_concrete_powder",
	"concrete_powder_yellow": "yellow_concrete_powder",
	"concrete_purple": "purple_concrete",
	"concrete_red": "red_concrete",
	"concrete_silver": "light_gray_concrete",
	"concrete_white": "white_concrete",
	"concrete_yellow": "yellow_concrete",
	"deadbush": "dead_bush",
	"dirt_podzol_side": "podzol_side",
	"dirt_podzol_top": "podzol_top",
	"dispenser_front_horizontal": "dispenser_front",
	"door_acacia_lower": "acacia_door_bottom",
	"acacia_door_lower": "acacia_door_bottom",
	"door_acacia_upper": "acacia_door_top",
	"acacia_door_upper": "acacia_door_top",
	"door_birch_lower": "birch_door_bottom",
	"birch_door_lower": "birch_door_bottom",
	"door_birch_upper": "birch_door_top",
	"birch_door_upper": "birch_door_top",
	"door_dark_oak_lower": "dark_oak_door_bottom",
	"dark_oak_door_lower": "dark_oak_door_bottom",
	"door_dark_oak_upper": "dark_oak_door_top",
	"dark_oak_door_upper": "dark_oak_door_top",
	"door_iron_lower": "iron_door_bottom",
	"iron_door_lower": "iron_door_bottom",
	"door_iron_upper": "iron_door_top",
	"iron_door_upper": "iron_door_top",
	"door_jungle_lower": "jungle_door_bottom",
	"jungle_door_lower": "jungle_door_bottom",
	"door_jungle_upper": "jungle_door_top",
	"jungle_door_upper": "jungle_door_top",
	"door_spruce_lower": "spruce_door_bottom",
	"spruce_door_lower": "spruce_door_bottom",
	"door_spruce_upper": "spruce_door_top",
	"spruce_door_upper": "spruce_door_top",
	"door_wood_lower": "oak_door_bottom",
	"oak_door_lower": "oak_door_bottom",
	"door_wood_upper": "oak_door_top",
	"oak_door_upper": "oak_door_top",
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
	"enchanting_table_base": "enchanting_table",
	"end_bricks": "end_stone_bricks",
	"end_portal_frame_empty": "end_portal_frame",
	"endframe_eye": "end_portal_frame_eye",
	"endframe_side": "end_portal_frame_side",
	"endframe_top": "end_portal_frame_top",
	"farmland_dry": "farmland",
	"farmland_wet": "farmland_moist",
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
	"glass_black": "black_stained_glass",
	"glass_blue": "blue_stained_glass",
	"glass_brown": "brown_stained_glass",
	"glass_cyan": "cyan_stained_glass",
	"glass_gray": "gray_stained_glass",
	"glass_green": "green_stained_glass",
	"glass_light_blue": "light_blue_stained_glass",
	"glass_lime": "lime_stained_glass",
	"glass_magenta": "magenta_stained_glass",
	"glass_orange": "orange_stained_glass",
	"glass_pink": "pink_stained_glass",
	"glass_purple": "purple_stained_glass",
	"glass_red": "red_stained_glass",
	"glass_silver": "light_gray_stained_glass",
	"glass_white": "white_stained_glass",
	"glass_yellow": "yellow_stained_glass",
	"glass_pane_top_black": "black_stained_glass_pane_top",
	"glass_pane_top_blue": "blue_stained_glass_pane_top",
	"glass_pane_top_brown": "brown_stained_glass_pane_top",
	"glass_pane_top_cyan": "cyan_stained_glass_pane_top",
	"glass_pane_top_gray": "gray_stained_glass_pane_top",
	"glass_pane_top_green": "green_stained_glass_pane_top",
	"glass_pane_top_light_blue": "light_blue_stained_glass_pane_top",
	"glass_pane_top_lime": "lime_stained_glass_pane_top",
	"glass_pane_top_magenta": "magenta_stained_glass_pane_top",
	"glass_pane_top_orange": "orange_stained_glass_pane_top",
	"glass_pane_top_pink": "pink_stained_glass_pane_top",
	"glass_pane_top_purple": "purple_stained_glass_pane_top",
	"glass_pane_top_red": "red_stained_glass_pane_top",
	"glass_pane_top_silver": "light_gray_stained_glass_pane_top",
	"glass_pane_top_white": "white_stained_glass_pane_top",
	"glass_pane_top_yellow": "yellow_stained_glass_pane_top",
	"glazed_terracotta_black": "black_glazed_terracotta",
	"glazed_terracotta_blue": "blue_glazed_terracotta",
	"glazed_terracotta_brown": "brown_glazed_terracotta",
	"glazed_terracotta_cyan": "cyan_glazed_terracotta",
	"glazed_terracotta_gray": "gray_glazed_terracotta",
	"glazed_terracotta_green": "green_glazed_terracotta",
	"glazed_terracotta_light_blue": "light_blue_glazed_terracotta",
	"glazed_terracotta_lime": "lime_glazed_terracotta",
	"glazed_terracotta_magenta": "magenta_glazed_terracotta",
	"glazed_terracotta_orange": "orange_glazed_terracotta",
	"glazed_terracotta_pink": "pink_glazed_terracotta",
	"glazed_terracotta_purple": "purple_glazed_terracotta",
	"glazed_terracotta_red": "red_glazed_terracotta",
	"glazed_terracotta_silver": "light_gray_glazed_terracotta",
	"glazed_terracotta_white": "white_glazed_terracotta",
	"glazed_terracotta_yellow": "yellow_glazed_terracotta",
	"grass_side": "grass_block_side",
	"grass_side_overlay": "grass_block_side_overlay",
	"grass_side_snowed": "grass_block_snow",
	"grass_top": "grass_block_top",
	"hardened_clay": "terracotta",
	"hardened_clay_stained_black": "black_terracotta",
	"hardened_clay_stained_blue": "blue_terracotta",
	"hardened_clay_stained_brown": "brown_terracotta",
	"hardened_clay_stained_cyan": "cyan_terracotta",
	"hardened_clay_stained_gray": "gray_terracotta",
	"hardened_clay_stained_green": "green_terracotta",
	"hardened_clay_stained_light_blue": "light_blue_terracotta",
	"hardened_clay_stained_lime": "lime_terracotta",
	"hardened_clay_stained_magenta": "magenta_terracotta",
	"hardened_clay_stained_orange": "orange_terracotta",
	"hardened_clay_stained_pink": "pink_terracotta",
	"hardened_clay_stained_red": "red_terracotta",
	"hardened_clay_stained_silver": "light_gray_terracotta",
	"hardened_clay_stained_white": "white_terracotta",
	"hardened_clay_stained_yellow": "yellow_terracotta",
	"ice_packed": "packed_ice",
	"leaves_acacia": "acacia_leaves",
	"leaves_big_oak": "dark_oak_leaves",
	"leaves_birch": "birch_leaves",
	"leaves_jungle": "jungle_leaves",
	"leaves_oak": "oak_leaves",
	"leaves_spruce": "spruce_leaves",
	"log_acacia": "acacia_log",
	"log_acacia_top": "acacia_log_top",
	"log_big_oak": "dark_oak_log",
	"log_big_oak_top": "dark_oak_log_top",
	"log_birch": "birch_log",
	"log_birch_top": "birch_log_top",
	"log_jungle": "jungle_log",
	"log_jungle_top": "jungle_log_top",
	"log_oak": "oak_log",
	"log_oak_top": "oak_log_top",
	"log_spruce": "spruce_log",
	"log_spruce_top": "spruce_log_top",
	"melon_stem_connected": "attached_melon_stem",
	"melon_stem_disconnected": "melon_stem",
	"mushroom_block_skin_brown": "brown_mushroom_block",
	"mushroom_block_skin_red": "red_mushroom_block",
	"mushroom_block_skin_stem": "mushroom_stem",
	"mushroom_brown": "brown_mushroom",
	"mushroom_red": "red_mushroom",
	"nether_brick": "nether_bricks",
	"nether_wart_stage_0": "nether_wart_stage0",
	"nether_wart_stage_1": "nether_wart_stage1",
	"nether_wart_stage_2": "nether_wart_stage2",
	"noteblock": "note_block",
	"observer_back_lit": "observer_back_on",
	"piston_inventory_normal": "piston_inventory",
	"piston_inventory_sticky": "sticky_piston_inventory",
	"piston_normal": "piston",
	"piston_top_normal": "piston_top",
	"planks_acacia": "acacia_planks",
	"planks_big_oak": "dark_oak_planks",
	"planks_birch": "birch_planks",
	"planks_jungle": "jungle_planks",
	"planks_oak": "oak_planks",
	"planks_spruce": "spruce_planks",
	"potatoes_stage_0": "potatoes_stage0",
	"potatoes_stage_1": "potatoes_stage1",
	"potatoes_stage_2": "potatoes_stage2",
	"potatoes_stage_3": "potatoes_stage3",
	"prismarine_dark": "dark_prismarine",
	"prismarine_rough": "prismarine",
	"prismarine_rough.mcmeta": "prismarine.mcmeta",
	"pumpkin_face_off": "pumpkin_face",
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
	"red_sandstone_carved": "chiseled_red_sandstone",
	"red_sandstone_normal": "red_sandstone",
	"red_sandstone_smooth": "cut_red_sandstone",
	"redstone_torch_on": "redstone_torch",
	"reeds": "sugar_cane",
	"repeater_off": "repeater",
	"sandstone_carved": "chiseled_sandstone",
	"sandstone_normal": "sandstone",
	"sandstone_smooth": "cut_sandstone",
	"sapling_acacia": "acacia_sapling",
	"sapling_birch": "birch_sapling",
	"sapling_jungle": "jungle_sapling",
	"sapling_oak": "oak_sapling",
	"sapling_roofed_oak": "dark_oak_sapling",
	"sapling_spruce": "spruce_sapling",
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
	"tallgrass": "grass",
	"terracotta_purple": "purple_terracotta",
	"torch_on": "torch",
	"trip_wire_source": "trip_wire_hook",
	"waterlily": "lily_pad",
	"web": "cobweb",
	"wheat_stage_0": "wheat_stage0",
	"wheat_stage_1": "wheat_stage1",
	"wheat_stage_2": "wheat_stage2",
	"wheat_stage_3": "wheat_stage3",
	"wheat_stage_4": "wheat_stage4",
	"wheat_stage_5": "wheat_stage5",
	"wheat_stage_6": "wheat_stage6",
	"wheat_stage_7": "wheat_stage7",
	"wool_colored_black": "black_wool",
	"wool_colored_blue": "blue_wool",
	"wool_colored_brown": "brown_wool",
	"wool_colored_cyan": "cyan_wool",
	"wool_colored_gray": "gray_wool",
	"wool_colored_green": "green_wool",
	"wool_colored_light_blue": "light_blue_wool",
	"wool_colored_lime": "lime_wool",
	"wool_colored_magenta": "magenta_wool",
	"wool_colored_orange": "orange_wool",
	"wool_colored_pink": "pink_wool",
	"wool_colored_purple": "purple_wool",
	"wool_colored_red": "red_wool",
	"wool_colored_silver": "light_gray_wool",
	"wool_colored_white": "white_wool",
	"wool_colored_yellow": "yellow_wool",
	"carpet_black": "black_carpet",
	"carpet_blue": "blue_carpet",
	"carpet_brown": "brown_carpet",
	"carpet_cyan": "cyan_carpet",
	"carpet_green": "green_carpet",
	"carpet_light_blue": "light_blue_carpet",
	"carpet_lime": "lime_carpet",
	"carpet_magenta": "magenta_carpet",
	"carpet_orange": "orange_carpet",
	"carpet_pink": "pink_carpet",
	"carpet_purple": "purple_carpet",
	"carpet_red": "red_carpet",
	"carpet_silver": "light_gray_carpet",
	"silver_carpet": "light_gray_carpet",
	"carpet_white": "white_carpet",
	"carpet_yellow": "yellow_carpet",
	"carpet_gray": "gray_carpet",
	"wooden_pressure_plate": "oak_pressure_plate",
	"wood_pressure_plate": "oak_pressure_plate",
	"trapdoor": "oak_trapdoor",
	"hopper_down": "hopper"
}

itemDict = {
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
	"door_acacia": "acacia_door",
	"door_birch": "birch_door",
	"door_dark_oak": "dark_oak_door",
	"door_iron": "iron_door",
	"door_jungle": "jungle_door",
	"door_spruce": "spruce_door",
	"door_wood": "oak_door",
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
	"fish_clownfish_raw": "clownfish",
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
	"houstonia": "azure_bluet",
	"map_empty": "map",
	"melon_speckled": "glistering_melon_slice",
	"speckled_melon": "glistering_melon_slice",
	"minecart_chest": "chest_minecart",
	"minecart_command_block": "command_block_minecart",
	"minecart_furnace": "furnace_minecart",
	"minecart_hopper": "hopper_minecart",
	"minecart_normal": "minecart",
	"minecart_tnt": "tnt_minecart",
	"mutton_cooked": "cooked_mutton",
	"mutton_raw": "mutton",
	"paeonia": "peony",
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
	"slimeball": "slime_ball",
	"spider_eye_fermented": "fermented_spider_eye",
	"totem": "totem_of_undying",
	"wood_axe": "wooden_axe",
	"wood_hoe": "wooden_hoe",
	"wood_pickaxe": "wooden_pickaxe",
	"wood_shovel": "wooden_shovel",
	"wood_sword": "wooden_sword",
	"wooden_armorstand": "armor_stand",
	"wooden_pressure_plate": "oak_pressure_plate",
	"wood_pressure_plate": "oak_pressure_plate",
	"trip_wire": "tripwire"
}

entityDict = {
	"boat/boat_acacia": "boat/acacia",
	"boat/boat_birch": "boat/birch",
	"boat/boat_darkoak": "boat/dark_oak",
	"boat/boat_jungle": "boat/jungle",
	"boat/boat_oak": "boat/oak",
	"boat/boat_spruce": "boat/spruce",
	"end_crystal/endercrystal": "end_crystal/end_crystal",
	"end_crystal/endercrystal_beam": "end_crystal/end_crystal_beam",
	"llama/llama_brown": "llama/brown",
	"llama/llama_creamy": "llama/creamy",
	"llama/llama_gray": "llama/gray",
	"llama/llama_white": "llama/white",
	"llama/decor/decor_black": "llama/decor/black",
	"llama/decor/decor_blue": "llama/decor/blue",
	"llama/decor/decor_brown": "llama/decor/brown",
	"llama/decor/decor_cyan": "llama/decor/cyan",
	"llama/decor/decor_gray": "llama/decor/gray",
	"llama/decor/decor_green": "llama/decor/green",
	"llama/decor/decor_light_blue": "llama/decor/light_blue",
	"llama/decor/decor_lime": "llama/decor/lime",
	"llama/decor/decor_magenta": "llama/decor/magenta",
	"llama/decor/decor_orange": "llama/decor/orange",
	"llama/decor/decor_pink": "llama/decor/pink",
	"llama/decor/decor_purple": "llama/decor/purple",
	"llama/decor/decor_red": "llama/decor/red",
	"llama/decor/decor_silver": "llama/decor/light_gray",
	"llama/decor/decor_white": "llama/decor/white",
	"llama/decor/decor_yellow": "llama/decor/yellow",
	"snowman": "snow_golem"
}

# Get command line arguments
usage = "\nUsage: converter.py <up|down> texturepack.zip"

if len(sys.argv) != 3:
	print(usage)
	sys.exit(0)

opr = sys.argv[1]
infile = sys.argv[2]

if not os.path.isfile(infile):
	print ("\nCould not find %s!" % infile)
	sys.exit(0)

if not opr in ["up", "down"]:
	print(usage)
	sys.exit(0)

tempDir = "CONVERTERTEMP-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Conversion functions
def renameDir(before, after):
	if os.path.isdir("%s/assets/minecraft/%s" % (tempDir, before)):
		os.rename("%s/assets/minecraft/%s" % (tempDir, before), "%s/assets/minecraft/%s" % (tempDir, after))
		print("Directory %s --> %s" % (before, after))

def renameFile(before, after):
	if os.path.isfile("%s/assets/minecraft/%s.png" % (tempDir, before)):
		os.rename("%s/assets/minecraft/%s.png" % (tempDir, before), "%s/assets/minecraft/%s.png" % (tempDir, after))

def convertDir(dict, dir):
	for key, value in dict.items():
		if opr == "up":
			renameFile(dir + key, dir + value)
		elif opr == "down":
			renameFile(dir + value, dir + key)
	print("Converted %s" % dir)

# Unpack the resource pack
print("Unpacking\n")
shutil.unpack_archive(infile, tempDir, "zip")

# Dirs to 1.13?
if opr == "up":
	for key, value in dirDict.items():
		renameDir(key, value)
	print("")

# Convert the dirs
convertDir(blockDict, "textures/block/")
convertDir(itemDict, "textures/item/")
convertDir(entityDict, "textures/entity/")

# Dirs to 1.12?
if opr == "down":
	print("")
	for key, value in dirDict.items():
		renameDir(value, key)

# Edit pack.mcmeta
mcmeta_1 = open("%s/pack.mcmeta" % tempDir, mode="r", encoding="utf-8").read()
mcmeta_2 = json.loads(mcmeta_1, strict=False)
mcmeta_3 = mcmeta_2.get("pack")
mcmeta_3.update({"pack_format": (3, 4)[opr == "up"]})
mcmeta_2.update({"pack": mcmeta_3})
open("%s/pack.mcmeta" % tempDir, mode="w", encoding="utf-8").write(json.dumps(mcmeta_2, ensure_ascii=False))

# Repack the resource pack
print("\nRepacking")
outfile = os.path.splitext(infile)[0] + "---" + ("1.12", "1.13")[opr == "up"]
shutil.make_archive(outfile, "zip", tempDir)
shutil.rmtree(tempDir)

print("\nDone! Output file: %s.zip" % outfile)
