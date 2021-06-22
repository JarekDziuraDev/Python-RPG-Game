import os
import sys
import time
import keyboard
import termcolor #import colored, cprint
from sty import fg, bg, ef, rs

from menu_class import choose_item_menu
from menu_class import simple_item_menu
from menu_class import string_item_menu
from menu_class import min_max_item_menu
from menu_class import Menu

from map_options.map_class import Map
from map_options.map_class import Map_Size
from map_options.map_class import Map_Name
from map_options.map_class import Map_Type
from map_options.map_class import Map_Id

from item_options.item_class import Item_Material
from item_options.item_class import Item_Id
from item_options.item_class import Item_Type
from item_options.item_class import Item_Name
from item_options.item_class import Item_Value
from item_options.item_class import Item_Count
from item_options.item_class import Item_Attack
from item_options.item_class import Item_Defense
from item_options.item_class import Item_Health
from item_options.item_class import Item_Agility
from item_options.item_class import Item_Level

from item_options.item_class import Item_Equipment
from item_options.item_class import Item_Enemy

from const_enum_class import Const
from editor_options.editor_brush_class import Const_Editor
from editor_options.editor_brush_class import Editor_Brush

from error_options.error_class import Error_Message
class Editor_Map:
    def __init__(self):
        self.map = []
        self.name = None
        self.size = None
class Point_Y:
    def __init__(self, mod_start = 0, mod_end = 0, r = 0, size = 50):
        self.start = mod_start
        self.end = mod_end        
        self.relative = r
        self.__size = size

    def start_mod(self, value):
        if value == -1:
            if self.start == 0 and self.relative > 0:
                self.relative += value
            else:
                if self.relative > 7:
                    self.relative += value
                else:
                    self.start += value
        
        elif value == 1:
            if self.relative < 7:
                self.relative += value
            else:
                self.start += value
            if self.start >= self.__size - 15 and self.relative < 14:
                self.relative += value
        
class Point_X:
    def __init__(self, start = 0, end = 0, r = 0, size = 50):
        self.start = start
        self.end = end
        self.relative = r
        self.__size = size

    def start_mod(self, value):
        if value == -1:
            if self.start == 0 and self.relative > 0:
                self.relative += value
            else:
                if self.relative > 14:
                    self.relative += value
                else:
                    self.start += value
        elif value == 1:
            if self.relative < 14:
                self.relative += value
            else:
                self.start += value
            if self.start >= self.__size - 30 and self.relative < 29:
                self.relative += value

class Edytor:
    def __init__(self):
        pass

    def __validation_item_before_save(self, item):
        validation = True
        if isinstance(item, Item_Material):
            if item.type == None and not (item.type == Const.wood or item.type == Const.liane or item.type == Const.flax):
                validation = False
            elif item.name == "" or len(item.name) > 20:
                validation = False
            elif item.value == None:
                validation = False
            elif item.count == None:
                validation = False
        elif isinstance(item, Item_Equipment):
            if item.type == None and not (item.type == Const.armor or item.type == Const.weapon):
                validation = False
            elif item.name == "" or len(item.name) > 20:
                validation = False
            elif item.value == None:
                validation = False
            elif item.health == None:
                validation = False
            elif item.attack == None:
                validation = False
            elif item.defense == None:
                validation = False
            elif item.agility == None:
                validation = False
        elif isinstance(item, Item_Enemy):
            if item.type == None and not (item.type == Const.no_agressive or item.type == Const.agressive or item.type == Const.very_agressive):
                validation = False
            elif item.name == "" or len(item.name) > 20:
                validation = False
            elif item.level == None:
                validation = False
            elif item.health == None:
                validation = False
            elif item.attack == None:
                validation = False
            elif item.defense == None:
                validation = False
            elif item.agility == None:
                validation = False
        elif isinstance(item, Map):
            if item.type == None or not (item.type == Const.local_map or item.type == Const.wolrd_map):
                validation = False
            elif item.size == None:
                validation = False
            elif item.name == "" or len(item.name)>20:
                validation = False

        return validation
    
    def __read_id_file(self, filepath):
        return_id = 0
        no_file = False
        try:
            f = open(filepath, "r")
            index = f.read()
            return_id = int(index)
        
        except(FileNotFoundError):
            no_file = True
        
        if no_file:
            f = open(filepath, "w+")
            f.write(str(return_id))            
            f.close()
        return return_id

    def __write_id_file(self, filepath, id):
        try:
            f = open(filepath, "w")
            f.write(str(id))
            f.close()
        except(FileNotFoundError):
            pass
    
    def write_item_file(self, filepath, item):
        if isinstance(item, Item_Material):
            try:
                f = open(filepath, "a+")
                f.writelines(str(item.id)+ " " + str(item.type) + " " + str(item.name) + " " + str(item.value) + " " + str(item.count) + "\n")
            except(FileNotFoundError):
                Error_Message.Msg("FileNotFound {}".format(filepath),2)
        elif isinstance(item, Item_Equipment):
            try:
                f = open(filepath, "a+")
                f.writelines(str(item.id)+ " " + str(item.type) + " " + str(item.name) + " " + str(item.value) + " " + str(item.health)+ " " + str(item.attack)+ " " + str(item.defense)+ " " + str(item.agility) + "\n")
            except(FileNotFoundError):
                Error_Message.Msg("FileNotFound {}".format(filepath),2)
        elif isinstance(item, Item_Enemy):
            try:
                f = open(filepath, "a+")
                f.writelines(str(item.id) + " " + str(item.type) + " " + str(item.name)+ " " + str(item.level) + " " + str(item.health) + " " + str(item.attack) + " " + str(item.defense)+ " " + str(item.agility) + "\n")
            except(FileNotFoundError):
                Error_Message.Msg("FileNotFound {}".format(filepath),2)

    def __save_item(self, item):
        filepath_wood_index = "item/materials/wood_index.txt"
        filepath_wood_item = "item/materials/wood_item.txt"
        
        filepath_flax_index = "item/materials/flax_index.txt"
        filepath_flax_item = "item/materials/flax_item.txt"

        filepath_liane_index = "item/materials/liane_index.txt"
        filepath_liane_item = "item/materials/liane_item.txt"

        filepath_armor_index = "item/equipment/armor_index.txt"
        filepath_armor_item = "item/equipment/armor_item.txt"

        filepath_weapon_index = "item/equipment/weapon_index.txt"
        filepath_weapon_item = "item/equipment/weapon_item.txt"
        
        filepath_enemy_index = "item/enemy/enemy_index.txt"
        filepath_enemy_item = "item/enemy/enemy_item.txt"

        filepath_item = ""
        filepath_index = ""
        
        if isinstance(item, Item_Material):
            if item.type  == Const.wood:
                index = self.__read_id_file(filepath_wood_index)
                item.id = index + 100
                filepath_index = filepath_wood_index
                filepath_item = filepath_wood_item
            elif item.type == Const.flax:
                index = self.__read_id_file(filepath_flax_index)
                item.id = index + 200
                filepath_index = filepath_flax_index
                filepath_item = filepath_flax_item
            elif item.type == Const.liane:
                index = self.__read_id_file(filepath_liane_index)
                item.id = index + 300
                filepath_index = filepath_liane_index
                filepath_item = filepath_liane_item
            self.__write_id_file(filepath_index, index + 1)
            self.write_item_file(filepath_item, item)
            
        elif isinstance(item, Item_Equipment):
            if item.type == Const.weapon:
                index = self.__read_id_file(filepath_weapon_index)
                item.id = index + 400
                filepath_index = filepath_weapon_index
                filepath_item = filepath_weapon_item
            if item.type == Const.armor:
                index = self.__read_id_file(filepath_armor_index)
                item.id = index + 500
                filepath_index = filepath_armor_index
                filepath_item = filepath_armor_item
            self.__write_id_file(filepath_index, index + 1)
            self.write_item_file(filepath_item, item)

        elif isinstance(item, Item_Enemy):
            if item.type == Const.no_agressive or item.type == Const.agressive or item.type == Const.very_agressive:
                index = self.__read_id_file(filepath_enemy_index)
                item.id = index + 600
                filepath_index = filepath_enemy_index
                filepath_item = filepath_enemy_item
            self.__write_id_file(filepath_index, index + 1)
            self.write_item_file(filepath_item, item)
    
    def __clear_item(self, *args):
        for item in args:
            if isinstance(item, Item_Name):
                item = ""
            else:
                item = None

    def create_item(self):
        #region deklaracje (item, item_menu)
        item_type = Item_Type()
        item_name = Item_Name()
        item_value = Item_Value()
        item_count = Item_Count()
        item_attack = Item_Attack()
        item_defense = Item_Defense()
        item_health = Item_Health()
        item_agility = Item_Agility()

        type_item_choose_im = choose_item_menu("Item type", 
        [Const.weapon,
        Const.armor,
        Const.wood,
        Const.flax,
        Const.liane], item_type)
        name_item_string_im = string_item_menu("Item name", item_name)
        value_item_min_max_im = min_max_item_menu("Item value",0,100, item_value)
        count_item_min_max_im = min_max_item_menu("Item count",0,100, item_count)
        attack_item_min_max_im = min_max_item_menu("Item attack",0,100, item_attack)
        defense_item_min_max_im = min_max_item_menu("Item defense",0,100, item_defense)
        health_item_min_max_im = min_max_item_menu("Item health",0,100, item_health)
        agility_item_min_max_im = min_max_item_menu("Item agility",0,100, item_agility)
        

        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)
        save_item_simple_im = simple_item_menu("Zapisz", Const.edytor_save)

        tmp_menu_list = [type_item_choose_im, quit_game_simple_im]
        new_item_menu = Menu(tmp_menu_list , "new item")
        #endregion
        
        choose_materials = False
        choose_equipment = False
        editor_options = None
        editor_run = True
        
        while editor_run:
            
            editor_options = new_item_menu.use_menu(None,True)
            #wyjście z edytora
            if editor_options == Const.quit_game:
                editor_run = False
            #lista opcji dla wood, liane, flax
            if item_type.type == Const.wood or item_type.type == Const.liane or item_type.type == Const.flax:
                tmp_menu_list = [type_item_choose_im,name_item_string_im, value_item_min_max_im, count_item_min_max_im, save_item_simple_im, quit_game_simple_im]                
                choose_materials = True
            
            #lista opcji dla equipment
            if item_type.type == Const.armor or item_type.type == Const.weapon:
                tmp_menu_list = [type_item_choose_im, 
                                    name_item_string_im, 
                                    value_item_min_max_im,
                                    health_item_min_max_im, 
                                    attack_item_min_max_im,
                                    defense_item_min_max_im,
                                    agility_item_min_max_im,
                                    save_item_simple_im,
                                    quit_game_simple_im]
                choose_equipment = True
            
            if editor_options == Const.edytor_save:
                if choose_materials:
                    item = Item_Material(None, item_type.type,item_name.name,item_value.value,item_count.count)
                    
                    validation_condition = self.__validation_item_before_save(item)

                    if validation_condition:                    
                        self.__save_item(item)
                        self.__clear_item(item_type, item_name, item_value, item_count, item_attack, item_defense, item_health, item_agility)
                        tmp_menu_list = [type_item_choose_im, quit_game_simple_im]
                    else:
                        Error_Message.Msg("Brak wszystkich wymaganych ustawień!", 2)
                elif choose_equipment:
                    item = Item_Equipment(None, item_type.type,
                                            item_name.name,
                                            item_value.value, 
                                            item_health.health,
                                            item_attack.attack, 
                                            item_defense.defense,
                                            item_agility.agility)
                
                    validation_condition = self.__validation_item_before_save(item)

                    if validation_condition:
                        self.__save_item(item)
                        self.__clear_item(item_type, item_name, item_value, item_count, item_attack, item_defense, item_health, item_agility)
                        tmp_menu_list = [type_item_choose_im, quit_game_simple_im]
                    else:
                        Error_Message.Msg("Brak wszystkich wymaganych ustawień!", 2)
                choose_equipment = False
                choose_materials = False
            new_item_menu = Menu(tmp_menu_list, "new item")
        
        #powrót do menu edytora
        return Const.edytor

    def create_enemy(self):
        #region deklaracje zmiennych item, menu
        item_type = Item_Type()
        item_name = Item_Name()
        item_level = Item_Level()
        item_attack = Item_Attack()
        item_defense = Item_Defense()
        item_health = Item_Health()
        item_agility = Item_Agility()

        name_item_string_im = string_item_menu("Enemy name", item_name)
        level_item_min_max_im = min_max_item_menu("Enemy level",1, 100, item_level)
        attack_item_min_max_im = min_max_item_menu("Enemy attack",0,100, item_attack)
        defense_item_min_max_im = min_max_item_menu("Enemy defense",0,100, item_defense)
        health_item_min_max_im = min_max_item_menu("Enemy health",0,100, item_health)
        agility_item_min_max_im = min_max_item_menu("Enemy agility",0,100, item_agility)

        type_enemy_choose_im = choose_item_menu("Ennemy agression",
        [Const.no_agressive,
        Const.agressive,
        Const.very_agressive], item_type)

        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)
        save_item_simple_im = simple_item_menu("Zapisz", Const.edytor_save)

        #lista opcji dla enemy
        new_enemy_menu = Menu([type_enemy_choose_im,
                                name_item_string_im,
                                level_item_min_max_im,
                                attack_item_min_max_im,
                                defense_item_min_max_im,
                                health_item_min_max_im,
                                agility_item_min_max_im,
                                save_item_simple_im, 
                                quit_game_simple_im], "new enemy")
        #endregion
        editor_run = True
        while editor_run:
            editor_options = new_enemy_menu.use_menu()

            if editor_options == Const.edytor_save:
                enemy = Item_Enemy(None, item_type.type, item_name.name, item_level.level, item_health.health, item_attack.attack, item_defense.defense, item_agility.agility)

                validation_condition = self.__validation_item_before_save(enemy)

                if validation_condition:
                    self.__save_item(enemy)
                    self.__clear_item(enemy)
                else:
                    Error_Message.Msg("Brak wszystkich wymaganych ustawień!", 2)
            
            elif editor_options == Const.quit_game:
                editor_run = False
        return Const.edytor
    
    def create_map(self):
        map_type = Map_Type()
        map_name = Map_Name()
        map_size = Map_Size()

        type_map_choose_im = choose_item_menu("Map type", [Const.local_map,
                                                            Const.wolrd_map],
                                                            map_type)
        name_map_string_im = string_item_menu("Map name", map_name)
        size_map_min_max_im = min_max_item_menu("Map size", 100,300, map_size, 10)
        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)        
        create_map_simple_im = simple_item_menu("Create Map", Const.edytor_create_map)

        new_map_menu = Menu([type_map_choose_im, 
                            name_map_string_im,
                            size_map_min_max_im,
                            create_map_simple_im,                            
                            quit_game_simple_im],
                            "new map")

        editor_run = True
        while editor_run:
            editor_options = new_map_menu.use_menu()
            
            if editor_options == Const.quit_game:
                editor_run = False
            elif editor_options == Const.edytor_create_map:
                mmap = Map(None, map_name.name, map_size.size, map_type.type)
                validation_condition = self.__validation_item_before_save(mmap)

                if validation_condition:
                    self.set_map(mmap)
                else:
                    Error_Message.Msg("Brak wszystkich wymaganych ustawień!", 2)
            #elif editor_options == Const.edytor_save:
            #    pass
        return Const.edytor
    
    def editor_map_control(self, editor_control_list):
        input_key = True
        while input_key:
            for item in editor_control_list:
                if isinstance(item, Point_Y):
                    if keyboard.is_pressed('w'):                
                        input_key = False
                        item.start_mod(-1)
                    if keyboard.is_pressed('s'):
                        input_key = False
                        item.start_mod(1)
                        
                elif isinstance(item, Point_X):            
                    if keyboard.is_pressed('a'):                
                        input_key = False
                        item.start_mod(-1)
                    if keyboard.is_pressed('d'):
                        input_key = False
                        item.start_mod(1)

                elif isinstance(item, Editor_Brush):
                    if keyboard.is_pressed('m'):
                        input_key = False
                        item.brush_menu = True
                    
                    if keyboard.is_pressed('space'):
                        input_key = False
                        item.brush_use = True

    def editor_map_validation_control(self, pA_list, size):
        for pA in pA_list:            
            if isinstance(pA, Point_Y):
                if pA.start < 0:
                    pA.start = 0                    
                elif pA.start > size - Const_Editor.height:
                    pA.start = size - Const_Editor.height
            
            if isinstance(pA, Point_X):
                if pA.start < 0:
                    pA.start = 0
                elif pA.start > size - Const_Editor.width:
                    pA.start = size - Const_Editor.width

    #menu do wyboru typu terenu
    def editor_terrain_menu(self, p_brush):
        grass1_simple_im = simple_item_menu("grass1", Const_Editor.grass1)
        grass2_simple_im = simple_item_menu("grass2", Const_Editor.grass2)
        sand_simple_im = simple_item_menu("sand", Const_Editor.sand)
        water_simple_im = simple_item_menu("water", Const_Editor.water)
        rock_simple_im = simple_item_menu("rock", Const_Editor.rock)

        editor_terrain_menu = Menu([grass1_simple_im,grass2_simple_im, sand_simple_im, water_simple_im,rock_simple_im], "terrain options")

        p_brush.actual_brush = editor_terrain_menu.use_menu()

    #menu do wyboru specjalnych pozycji na mapie
    def editor_special_mark_menu(self, p_brush):
        port_simple_im = simple_item_menu("port1", Const_Editor.port1)
        editor_special_mark_menu = Menu([port_simple_im], "special marks")

        p_brush.actual_brush = editor_special_mark_menu.use_menu()
    ###############################################################################################
    def __editor_load_enemy_items(self, file_path):
        #enemy_list = None
        try:
            f = open("{}".format(file_path), "r")
            end_of_file = False
            lines = []
            while not end_of_file:
                row = f.readline()
                if row == "":
                    end_of_file = True
                else:
                    row = row.split(" ")
                    lines.append(row)
            #OK
            enemy_list = []
            for item in lines:
                enemy_list.append(Item_Enemy(int(item[0]), item[1], item[2], int(item[3]), int(item[4]), int(item[5]), int(item[6]), int(item[7])))
                    
        except(FileNotFoundError):
            Error_Message.Msg("Nie znaleziono pliu {}".format(file_path),2)
        return enemy_list
                    
    def __editor_enemy_menu(self, p_brush):
        filepath_map_index = "item/enemy/enemy_item.txt"
        enemy_list = self.__editor_load_enemy_items(filepath_map_index)
        list_enemy_simple_im = []
        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)

        if enemy_list == None:
            list_enemy_simple_im.append(quit_game_simple_im)
        else:
            for item in enemy_list:
                enemy_simple_im = simple_item_menu("{} {}".format(item.name, item.id), item.id)
                list_enemy_simple_im.append(enemy_simple_im)
            list_enemy_simple_im.append(quit_game_simple_im)
        list_enemy_menu = Menu(list_enemy_simple_im, "choose enemy")
        p_brush.actual_brush = list_enemy_menu.use_menu()
    ###############################################################################################
    def __editor_load_materials_items(self, file_path_flax, file_path_liane, file_path_wood):
        material_list = None
        file_list = [] 
        try:
            f_flax = open("{}".format(file_path_flax), "r")
            f_liane = open("{}".format(file_path_liane), "r")
            f_wood = open("{}".format(file_path_wood), "r")
            file_list.append(f_flax)
            file_list.append(f_liane)
            file_list.append(f_wood)
            

            end_of_file = False
            material_list = []
            lines = []
            i = 0
            while not end_of_file:

                row = file_list[i].readline()
                if row == "":
                    i += 1
                else:
                    row = row.split(" ")
                    lines.append(row)
                if i == 3:
                    end_of_file = True

            for item in lines:
                material_list.append(Item_Material(int(item[0]), item[1], item[2], int(item[3]), int(item[4])))

        except(FileNotFoundError):
            Error_Message.Msg("Nie znaleziono pliu {}".format(file_path_flax),2)
            Error_Message.Msg("Nie znaleziono pliu {}".format(file_path_liane),2)
            Error_Message.Msg("Nie znaleziono pliu {}".format(file_path_wood),2)

        return material_list
        
    def __editor_material_menu(self, p_brush):
        file_path_flax = "item/materials/flax_item.txt"
        file_path_liane = "item/materials/liane_item.txt"
        file_path_wood = "item/materials/wood_item.txt"

        material_list = self.__editor_load_materials_items(file_path_flax,file_path_liane,file_path_wood)
        list_material_simple_im = []
        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)

        if material_list == None or len(material_list) == 0:
            list_material_simple_im.append(quit_game_simple_im)
        else:
            for item in material_list:
                material_simple_im = simple_item_menu("{} {}".format(item.name, item.id), item.id)
                list_material_simple_im.append(material_simple_im)
        list_material_simple_im.append(quit_game_simple_im)

        list_material_menu = Menu(list_material_simple_im, "choose material")
        p_brush.actual_brush = list_material_menu.use_menu()

    def __editor_load_equipment_items(self, file_path_armor,file_path_weapon):
        equipment_list = None
        file_list = []
        try:
            f_armor = open("{}".format(file_path_armor), "r")
            f_weapon = open("{}".format(file_path_weapon), "r")            
            file_list.append(f_armor)
            file_list.append(f_weapon)     
            end_of_file = False
            equipment_list = []
            lines = []
            i = 0
            while not end_of_file:
                row = file_list[i].readline()
                if row == "":
                    i += 1
                else:
                    row = row.split(" ")
                    lines.append(row)
                if i == len(file_list):
                    end_of_file = True
            for item in lines:
                equipment_list.append(Item_Equipment(int(item[0]), item[1], item[2], int(item[3]), int(item[4]), int(item[5]), int(item[6]), int(item[7]) ))     
        except(FileNotFoundError):
            Error_Message.Msg("Nie znaleziono pliu {}".format(file_path_armor),2)
            Error_Message.Msg("Nie znaleziono pliu {}".format(file_path_weapon),2)
        return equipment_list

    def __editor_equipment_menu(self, p_brush):
        file_path_armor = "item/equipment/armor_item.txt"
        file_path_weapon = "item/equipment/weapon_item.txt"
        

        equipment_list = self.__editor_load_equipment_items(file_path_armor,file_path_weapon)
        list_equipment_simple_im = []
        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)

        if equipment_list == None or len(equipment_list) == 0:
            list_equipment_simple_im.append(quit_game_simple_im)
        else:
            for item in equipment_list:
                equipment_simple_im = simple_item_menu("{} {}".format(item.name, item.id), item.id)
                list_equipment_simple_im.append(equipment_simple_im)
        list_equipment_simple_im.append(quit_game_simple_im)

        list_equipment_menu = Menu(list_equipment_simple_im, "choose equipment")
        p_brush.actual_brush = list_equipment_menu.use_menu()

    ###############################################################################################

    ###############################################################################################
    #rysowanie mapy
    def editor_draw_map(self, editor_map, pX, pY, p_brush):
        game_x = 0
        game_y = 0
                
        for y in range(pY.start, pY.start + pY.end):
            for x in range(pX.start, pX.start + pX.end):                        
                if game_x == pX.relative and game_y == pY.relative:                    
                    termcolor.cprint("•", 'red',end =" ")
                else:
                    if editor_map.map[y][x] == Const_Editor.water:                        
                        print('\x1b[1;34;40m' + "{:1}".format("▒"), end =" ")
                    elif editor_map.map[y][x] == Const_Editor.grass1:                                            
                        print(fg(20,150,20) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == Const_Editor.grass2:                                            
                        print(fg(15,120,15) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == Const_Editor.sand:
                        print('\x1b[1;33;40m' + "{:1}".format("▒"), end = " ")
                    elif editor_map.map[y][x] == Const_Editor.port1:                        
                        print(fg(130,20,20) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == Const_Editor.rock:
                        print(fg(60,60,60) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == 600:
                        print(fg(128,64,64) + "{:1}".format("■") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == 601:
                        print(fg(90,50,0) + "{:1}".format("■") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == 602:
                        print(fg(210,105,0) + "{:1}".format("■") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == 100: #or editor_map.map[y][x] < 200
                        print(fg(160,100,60) + "{:1}".format("╬") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == 200:
                        print(fg(210,210,0) + "{:1}".format("♣") + fg.rs , end = " ")
                    elif editor_map.map[y][x] == 300:
                        print(fg(20,130,20) + "{:1}".format("§") + fg.rs , end = " ")
                    elif editor_map.map[y][x] >= 400 and editor_map.map[y][x] < 600:
                        print(fg(20,20,20) + "{:1}".format("☼") + fg.rs , end = " ")
                game_x += 1
                p_brush.actual_position_y = pY.start + pY.relative
                p_brush.actual_position_x = pX.start + pX.relative

            print()                            
            game_y += 1
            game_x = 0               
            
        print('\x1b[6;30;42m' + '' + '\x1b[0m')
    
    def editor_map_menu(self, p_brush,editor_map):
        #region deklaracje (menu)
        type_of_terrain_simple_im = simple_item_menu("Teren", Const.edytor_type_of_terrain)
        type_of_enemy_simple_im = simple_item_menu("Wrogowie", Const.edytor_type_of_enemy)
        type_of_raw_material_simple_im = simple_item_menu("Surowce", Const.edytor_type_of_material)
        type_of_special_position_simple_im = simple_item_menu("Special mark", Const.edytor_type_of_special_mark)
        type_of_equipment_simple_im = simple_item_menu("Ekwipunek", Const.edytor_type_of_equipment)
        size_of_brush_choose_im = choose_item_menu("Brush size", [Const_Editor.brush_small,
                                                                    Const_Editor.brush_medium,
                                                                    Const_Editor.brush_big], p_brush)
        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)
        save_item_simple_im = simple_item_menu("Zapisz", Const.edytor_save)

        editor_main_menu = Menu([size_of_brush_choose_im,type_of_terrain_simple_im, type_of_enemy_simple_im, type_of_raw_material_simple_im,type_of_equipment_simple_im, type_of_special_position_simple_im, save_item_simple_im, quit_game_simple_im],"map menu")
        #endregion

        run_editor_condition = True

        if p_brush.brush_menu:
            editor_options = editor_main_menu.use_menu()

            if editor_options == Const.edytor_type_of_terrain:
                self.editor_terrain_menu(p_brush)
            elif editor_options == Const.edytor_type_of_special_mark:
                self.editor_special_mark_menu(p_brush)
            elif editor_options == Const.edytor_type_of_enemy:
                self.__editor_enemy_menu(p_brush)
            elif editor_options == Const.edytor_type_of_material:
                self.__editor_material_menu(p_brush)
            elif editor_options == Const.edytor_type_of_equipment:
                self.__editor_equipment_menu(p_brush)
            elif editor_options == Const.edytor_save:
                self.editor_save_map(editor_map)
            elif editor_options == Const.quit_game:
                run_editor_condition = False
        return run_editor_condition
    
    def __editor_map_paint(self, p_brush, editor_map):
        if p_brush.size == Const_Editor.brush_small:
            size = 1
        elif p_brush.size == Const_Editor.brush_medium:
            size = 2
        elif p_brush.size == Const_Editor.brush_big:
            size = 3
        else:
            Error_Message.Msg("Undifined brush size",2)
        
        if p_brush.brush_use:
            for j in range(size):
                for i in range(size):
                    editor_map.map[p_brush.actual_position_y+j][p_brush.actual_position_x+i] = p_brush.actual_brush

    def editor_save_map_index(self, file_path, map_name):
        map_name_list = None
        try:
            f = open("{}".format(file_path), 'r')
            row = f.read()
            map_name_list = row.split(' ')
            for item in map_name_list:
                if item == "":
                    map_name_list.remove(item)
        except:
            pass

        #Error_Message.Msg("{}".format(len(map_name_list)), 2)

        if map_name_list == None:            
            try:
                f = open(file_path, "w")
                f.write(str(map_name))
                f.close()
            except:
                Error_Message.Msg("Zapis się nie powiódł", 2)
        else:
            if not map_name in map_name_list:
                Error_Message.Msg(map_name_list,1)
                map_name_list.append(map_name)
                try:
                    f = open(file_path, "w+")
                    for cel in map_name_list:
                        f.write(str(cel)+" ")                        
                    f.close()
                except:
                    Error_Message.Msg("Zapis się nie powiódł", 2)

    def editor_save_map(self, editor_map):
        filepath_map = "maps/{}.txt".format(editor_map.name)
        filepath_map_index = "maps/maps_index.txt"

        try:
            f = open(filepath_map, "w+")
            i = 0
            for row in editor_map.map:
                for cel in row:
                    if i == len(row):
                        f.write("\n")
                        i = 0
                    f.write(str(cel) + " ")
                    i += 1
        except(FileNotFoundError):
            Error_Message.Msg("FileNotFound",2)

        self.editor_save_map_index(filepath_map_index, editor_map.name)

    def __load_map_menu_load_index(self, file_path):
        map_name_list = None
        try:
            f = open("{}".format(file_path), 'r')
            row = f.read()
            map_name_list = row.split(' ')
            for item in map_name_list:
                if item == "":
                    map_name_list.remove(item)
        except:
            return None
        return map_name_list

    def load_map_menu(self):        
        filepath_map_index = "maps/maps_index.txt"

        map_name_list = self.__load_map_menu_load_index(filepath_map_index)
        
        list_map_simple_im = []
        
        quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)
        if map_name_list == None:
            list_map_simple_im.append(quit_game_simple_im)
        else:
            for item in map_name_list:
                map_name = str(item)
                map_simple_im = simple_item_menu("{}".format(map_name), map_name)
                list_map_simple_im.append(map_simple_im)                    
            list_map_simple_im.append(quit_game_simple_im)
        
        list_map_menu = Menu(list_map_simple_im, "load map")

        map_name = list_map_menu.use_menu()

        return map_name
        
    def set_map(self, options_map):        

        editor_map = Editor_Map()
        map_row = []
        i = 0
        
        if isinstance(options_map, Map):
            editor_map.name = options_map.name
            editor_map.size = options_map.size
            for y in range(options_map.size):
                for x in range(options_map.size):
                    map_row.append(0)
                    i += 1
                editor_map.map.append(map_row)
                map_row = []
        else:
            editor_map.name = options_map
            file_path = "maps/{}.txt".format(editor_map.name)
            try:
                f = open(file_path, "r")
                end_of_file = False
                
                maps = []
                while not end_of_file:
                    row = f.readline()
                    if row == "":
                        end_of_file = True
                    else:
                        row = row.split(" ")
                        maps.append(row)

                #Error_Message.Msg("{}".format(maps),2)
                
                i = 0
                line = [] 
                for row in maps:                    
                    for cel in row:
                        if not cel == " " and not cel == '\n' and not cel == "":                            
                            line.append(int(cel))  
                    editor_map.map.append(line)
                    line = []
                    i += 1
                
                editor_map.size = i
                
            except(FileNotFoundError):
                Error_Message.Msg("Nie znaleziono mapy",2)
        
        pY = Point_Y(10,15,7, editor_map.size)
        pX = Point_X(10,30,14, editor_map.size)
        p_brush = Editor_Brush()
        run_editor_condition = True

        while run_editor_condition:
            os.system("cls")

            self.editor_draw_map(editor_map, pX, pY, p_brush)
            
            print("Actual brush {}".format(p_brush.actual_brush))
            print("Actual brush position Y {}".format(p_brush.actual_position_y))
            print("Actual brush position X {}".format(p_brush.actual_position_x))


            self.editor_map_control([pY,pX,p_brush])           
            self.editor_map_validation_control([pY,pX], editor_map.size)
            run_editor_condition = self.editor_map_menu(p_brush, editor_map)
            self.__editor_map_paint(p_brush, editor_map)
            
            time.sleep(.11)


#edytor = Edytor()

#edytor.set_map(Map(None, "map1", 50, Const.wolrd_map))

