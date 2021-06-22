from game_options.game_const import Game_Const
from error_options.error_class import Error_Message

from menu_class import simple_item_menu
from menu_class import choose_item_menu
from menu_class import Menu

from item_options.item_class import Item_Material
from item_options.item_class import Item_Equipment

from game_options.player_statistic_class import Player_Statistic
from game_options.player_armor_class import Player_Armor

import time
import os
import sys
import keyboard
from sty import fg, bg, ef, rs

class Map:
    def __init__(self, mmap, size):
        self.map = mmap
        self.size = size
        self.width = 30
        self.height = 15
        self.__const_y = 7
        self.__const_x = 14
        self.__relative_x = 0
        self.__relative_y = 0
        self.__mod_x = self.relative_x + self.__const_x
        self.__mod_y = self.relative_y + self.__const_y
        self.blocked_up = False
        self.blocked_down = False
        self.blocked_right = False
        self.blocked_left = False
    
    def refresh_block(self):
        self.blocked_up = False
        self.blocked_down = False
        self.blocked_right = False
        self.blocked_left = False        

    @property
    def position_x(self):
        return (self.__relative_x + self.__mod_x)
    @property
    def position_y(self):
        return (self.__relative_y + self.__mod_y)
    @property
    def mod_y(self):
        return self.__mod_y
    @property
    def mod_x(self):
        return self.__mod_x
    @property
    def relative_x(self):
        return self.__relative_x

    @relative_x.setter
    def relative_x(self, value):
        if value < 0:
            if self.__relative_x > 0:
                if self.__mod_x > 15:
                    self.__mod_x -= 1
                else:
                    self.__relative_x -= 1
            elif self.__relative_x == 0 and self.__mod_x > 0:
                self.__mod_x -= 1
        else:
            if self.__mod_x < self.__const_x:
                self.__mod_x += 1
            elif self.__relative_x < self.size - self.width:
                self.__relative_x += 1
            elif self.__mod_x < self.width-1:
                self.__mod_x += 1

    @property
    def relative_y(self):
        return self.__relative_y
    @relative_y.setter
    def relative_y(self, value):
        if value < 0:
            if self.__relative_y > 0:
                if self.__mod_y > 7:
                    self.__mod_y -= 1
                else:
                    self.__relative_y -= 1
            elif self.__relative_y == 0 and self.__mod_y > 0:
                self.__mod_y -= 1
        else:
            if self.__mod_y < self.__const_y:
                self.__mod_y += 1
            elif self.__relative_y < self.size - self.height:
                self.__relative_y += 1
            elif self.__mod_y < self.height -1:
                self.__mod_y += 1

class Equipment_Material_Item:
    def __init__(self, item, count):
        self.item = item
        self.count = count

class Equipment_Equipment_Item:
    def __init__(self, item, count):
        self.item = item
        self.count = count


class Player:
    def __init__(self):
        self.__health = 50
        self.__defense = 1
        self.__agility = 1
        self.__attack = 10

        
        
        self.__item_material_list = self.__initialize_materials_base()
        self.__item_armor_list = self.__initialize_armor_base()
        self.__item_weapon_list = self.__initialiez_weapon_base()
        
        self.__equipment_material_list = []
        self.__equipment_armor_list = []
        self.__equipment_weapon_list = []
        
        self.__outfit_armor = Player_Armor()
        self.__outfit_weapon = None

    def __armor_statistic(self):
        for item in self.__item_armor_list:            
            if item.name == self.__outfit_armor.name:
                return item
            
        return None

    def health(self):        
        all_health = self.__health

        item = self.__armor_statistic()
        
        if not item == None:
            all_health += item.health
        
        return all_health

    def attack(self):        
        all_attack = self.__attack

        item = self.__armor_statistic()
        
        if not item == None:
            all_attack += item.attack
        
        return all_attack
    
    def defense(self):
        all_defense = self.__defense

        item = self.__armor_statistic()
        
        if not item == None:
            all_defense += item.defense
        
        return all_defense
    
    def agility(self):
        all_agility = self.__agility

        item = self.__armor_statistic()
        
        if not item == None:
            all_agility += item.agility
        
        return all_agility
        
    def __equipment_material_add(self, item):
        item_add = False
        if len(self.__equipment_material_list) > 0:
            for element in self.__equipment_material_list:
                if element.item.id == item.id:
                    element.count += 1                    
                    item_add = True
            if not item_add:
                self.__equipment_material_list.append(Equipment_Material_Item(item, item.count))    
        else:
            self.__equipment_material_list.append(Equipment_Material_Item(item, item.count))
    
    def __equipment_armor_add(self, item):
        item_add = False
        if len(self.__equipment_armor_list) > 0:
            for element in self.__equipment_armor_list:
                if element.item.id == item.id:
                    element.count += 1
                    item_add = True
            if not item_add:
                self.__equipment_armor_list.append(Equipment_Equipment_Item(item, 1))
        else:
            self.__equipment_armor_list.append(Equipment_Equipment_Item(item, 1))

    def __equipment_weapon_add(self, item):
        item_add = False
        if len(self.__equipment_weapon_list) > 0:
            for element in self.__equipment_weapon_list:
                if element.item.id == item.id:
                    element.count += 1
                    item_add = True
            if not item_add:
                self.__equipment_weapon_list.append(Equipment_Equipment_Item(item, 1))
        else:
            self.__equipment_weapon_list.append(Equipment_Equipment_Item(item, 1))

    def __initialiez_weapon_base(self):
        filepath_weapon_item = "item/equipment/weapon_item.txt"
        item_list = []
        try:
            f_weapon = open(filepath_weapon_item, "r")
            file_list = []
            file_list.append(f_weapon)
            index = 0
            end_of_file = False
            line = []

            while not end_of_file:
                row = file_list[index].readline()
                if row == "":
                    index += 1
                else:
                    row = row.split(" ")
                    line.append(row)
                if index == len(file_list):
                    end_of_file = True

            for item in line:
                item_list.append(Item_Equipment(int(item[0]), item[1], item[2], int(item[3]), int(item[4]), int(item[5]), int(item[6]), int(item[7]) ))
            
            f_weapon.close()            
        
        except(FileNotFoundError):
            Error_Message.Msg("Brak plików, {}".format(filepath_weapon_item), 2)  

        return item_list

    def __initialize_armor_base(self):
        filepath_armor_item = "item/equipment/armor_item.txt"
        item_list = []        
        try:            
            f_armor = open(filepath_armor_item)
            
            file_list = []
            file_list.append(f_armor)

            end_of_file = False
            line = []
            index = 0

            while not end_of_file:
                row = file_list[index].readline()
                if row == "":
                    index += 1
                else:
                    row = row.split(" ")
                    line.append(row)
                if index == len(file_list):
                    end_of_file = True

            for item in line:
                item_list.append(Item_Equipment(int(item[0]), item[1], item[2], int(item[3]), int(item[4]), int(item[5]), int(item[6]), int(item[7]) ))
            
            
            f_armor.close()
        
        except(FileNotFoundError):
            Error_Message.Msg("Brak plików, {}".format(filepath_armor_item), 2)  

        return item_list

    def __initialize_materials_base(self):        
        filepath_wood_item = "item/materials/wood_item.txt"        
        filepath_flax_item = "item/materials/flax_item.txt"
        filepath_liane_item = "item/materials/liane_item.txt"
        item_lsit = []
        try:
            f_wood = open(filepath_wood_item, 'r')
            f_flax = open(filepath_flax_item, 'r')
            f_liane = open(filepath_liane_item, 'r')

            file_list = []
            file_list.append(f_wood)
            file_list.append(f_flax)
            file_list.append(f_liane)

            end_of_file = False
            line = []
            index = 0
            while not end_of_file:
                row = file_list[index].readline()
                if row == "":
                    index += 1
                else:
                    row = row.split(" ")
                    line.append(row)
                if index == len(file_list):
                    end_of_file = True
            
            for item in line:
                item_lsit.append(Item_Material(int(item[0]), item[1], item[2], int(item[3]), int(item[4])))
            
            f_wood.close()
            f_flax.close()
            f_liane.close()

        except(FileNotFoundError):
            Error_Message.Msg("Brak plików, {} {} {}".format(filepath_wood_item,filepath_flax_item,filepath_liane_item), 2)                
        return item_lsit

    def pick_up(self, item):
        if item >= 400 and item < 500:
            for item_on_list in self.__item_weapon_list:
                if item_on_list.id == item:
                    self.__equipment_weapon_add(item_on_list)
        elif item >= 500 and item < 600:
            for item_on_list in self.__item_armor_list:
                if item_on_list.id == item:
                    self.__equipment_armor_add(item_on_list)
        elif item >= 100 and item < 400:
            for item_on_list in self.__item_material_list:            
                if item_on_list.id == item:
                    self.__equipment_material_add(item_on_list)

    
    
    def show_equipment(self):
        equipment_simple_im = simple_item_menu("Ekwipunek", Game_Const.equipment)
        material_simple_im = simple_item_menu("Materiały", Game_Const.materials)
        outfit_simple_im = simple_item_menu("Wyposażenie", Game_Const.outfit)
        quit_game_simple_im = simple_item_menu("Koniec", Game_Const.quit_game)

        equipment_menu = Menu([equipment_simple_im, material_simple_im, outfit_simple_im, quit_game_simple_im], "all equipment")
        list_equipment_material_simple_im = []
        list_equipment_equipment_simple_im = []

        for item in self.__equipment_material_list:
            equipment_simple_im = simple_item_menu("{} {}".format(item.item.name, item.count), 0)
            list_equipment_material_simple_im.append(equipment_simple_im)
        list_equipment_material_simple_im.append(quit_game_simple_im)

        for item in self.__equipment_armor_list:
            equipment_simple_im = simple_item_menu("{} {}".format(item.item.name, item.count), 0)
            list_equipment_equipment_simple_im.append(equipment_simple_im)
        for item in self.__equipment_weapon_list:
            equipment_simple_im = simple_item_menu("{} {}".format(item.item.name, item.count), 0)
            list_equipment_equipment_simple_im.append(equipment_simple_im)
        list_equipment_equipment_simple_im.append(quit_game_simple_im)

        equipment_equipment_menu = Menu(list_equipment_equipment_simple_im, "equipment")
        equipment_material_menu = Menu(list_equipment_material_simple_im, "materials")


        player_statistic = Player_Statistic(self.health(), self.attack(), self.defense(), self.agility())

        equipment_outfit_armor_choose = []
        equipment_outfit_menu = None

        

        if len(self.__equipment_armor_list) > 0:         
            for item in self.__equipment_armor_list:
                equipment_outfit_armor_choose.append(item.item.name)
            equipment_armor_choose_im = choose_item_menu("Pancerz",equipment_outfit_armor_choose,  self.__outfit_armor)
            equipment_outfit_menu = Menu([equipment_armor_choose_im, quit_game_simple_im], "outfit")
        else:
            equipment_outfit_menu = Menu([quit_game_simple_im], "outfit")

        run_condition = True
        while run_condition:
            options = equipment_menu.use_menu()

            if options == Game_Const.quit_game:
                run_condition = False
            elif options == Game_Const.materials:
                equipment_material_menu.use_menu()
            elif options == Game_Const.equipment:
                equipment_equipment_menu.use_menu()
            elif options == Game_Const.outfit:
                equipment_outfit_menu.use_menu(player_statistic)

class Game:
    def __init__(self):
        pass

    def __interaction(self, mmap, player):
        x = mmap.position_x
        y = mmap.position_y

        mmap.refresh_block()

        if mmap.map[y-1][x] == Game_Const.water or mmap.map[y-1][x] == Game_Const.rock:
            mmap.blocked_up = True
        if mmap.map[y+1][x] == Game_Const.water or mmap.map[y+1][x] == Game_Const.rock:
            mmap.blocked_down = True
        if mmap.map[y][x+1] == Game_Const.water or mmap.map[y][x+1] == Game_Const.rock:
            mmap.blocked_right = True
        if mmap.map[y][x-1] == Game_Const.water or mmap.map[y][x-1] == Game_Const.rock:
            mmap.blocked_left = True

        if mmap.map[y][x] >= 100 and mmap.map[y][x] < 600:
            player.pick_up(mmap.map[y][x])
            mmap.map[y][x] = mmap.map[y][x+1]

    def __control(self, control_list):
        input_key = True
        while input_key:
            for item in control_list:
                if isinstance(item, Map):
                    if keyboard.is_pressed('w') and not item.blocked_up:
                        input_key = False
                        item.relative_y = -1
                    if keyboard.is_pressed('s') and not item.blocked_down:
                        input_key = False
                        item.relative_y= 1
                    if keyboard.is_pressed('d') and not item.blocked_right:
                        input_key = False
                        item.relative_x = 1
                    if keyboard.is_pressed('a') and not item.blocked_left:
                        input_key = False
                        item.relative_x = -1
                if isinstance(item, Player):                    
                    if keyboard.is_pressed('e'):
                        input_key = False
                        item.show_equipment()


    def __draw_map(self, mmap):
        for y in range(mmap.relative_y, mmap.relative_y + mmap.height):
            for x in range(mmap.relative_x, mmap.relative_x + mmap.width):                
                if y == mmap.mod_y + mmap.relative_y and x == mmap.mod_x + mmap.relative_x:
                    print(fg(150,150,200) + "{:1}".format("■") + fg.rs , end = " ")
                else:
                    if mmap.map[y][x] == Game_Const.water:                        
                        print('\x1b[1;34;40m' + "{:1}".format("▒"), end =" ")
                    elif mmap.map[y][x] == Game_Const.sand:                        
                        print('\x1b[1;33;40m' + "{:1}".format("▒"), end = " ")
                    elif mmap.map[y][x] == Game_Const.grass1:                        
                        print(fg(20,150,20) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif mmap.map[y][x] == Game_Const.grass2:                        
                        print(fg(15,120,15) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif mmap.map[y][x] == Game_Const.port1:                        
                        print(fg(130,20,20) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif mmap.map[y][x] == Game_Const.rock:                        
                        print(fg(60,60,60) + "{:1}".format("▓") + fg.rs , end = " ")
                    elif mmap.map[y][x] == 100 and mmap.map[y][x] < 200:
                        print(fg(160,100,60) + "{:1}".format("╬") + fg.rs , end = " ")
                    elif mmap.map[y][x] >= 200 and mmap.map[y][x] < 300:
                        print(fg(210,210,0) + "{:1}".format("♣") + fg.rs , end = " ")
                    elif mmap.map[y][x] >= 300 and mmap.map[y][x] < 399:
                        print(fg(20,130,20) + "{:1}".format("§") + fg.rs , end = " ")
                    elif mmap.map[y][x] >= 400 and mmap.map[y][x] < 600:
                        print(fg(20,20,20) + "{:1}".format("☼") + fg.rs , end = " ")
                    elif mmap.map[y][x] == 600:
                        print(fg(128,64,64) + "{:1}".format("■") + fg.rs , end = " ")
            print()
        print('\x1b[6;30;42m' + '' + '\x1b[0m')
                
    def __load_map(self):
        file_path = "maps/map1.txt"
        try:
            f = open(file_path, "r")
            end_of_file = False
            lines = []
            while not end_of_file:
                row = f.readline()
                if row == "":
                    end_of_file = True
                else:
                    row = row.split(" ")
                    lines.append(row)
            
            line = []
            mmap = []
            for row in lines:
                for item in row:
                    if not item == " " and not item == '\n' and not item == "":
                        line.append(int(item))
                mmap.append(line)
                line = []
        except(FileNotFoundError):
            Error_Message.Msg("Nie znaleziono pliku: {}".format(file_path), 2)


        return Map(mmap, len(mmap))
    
    def __load_or_initialize_player(self):
        return Player()

    def start_game(self):
        
        Map = self.__load_map()
        Player = self.__load_or_initialize_player()
        
        run_game_condition = True

        while run_game_condition:
            os.system("cls")
            
            self.__draw_map(Map)

            # print(Map.blocked_up)
            # print(Map.blocked_down)
           

            self.__control([Map, Player])
            self.__interaction(Map, Player)

            time.sleep(.11)
