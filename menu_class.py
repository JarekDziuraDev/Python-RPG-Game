import os 
import time
import keyboard

from map_options.map_class import Map_Size
from map_options.map_class import Map_Name
from map_options.map_class import Map_Type

from const_enum_class import Const

from item_options.item_class import Item_Type
from item_options.item_class import Item_Name
from item_options.item_class import Item_Value
from item_options.item_class import Item_Count
from item_options.item_class import Item_Attack
from item_options.item_class import Item_Defense
from item_options.item_class import Item_Health
from item_options.item_class import Item_Agility
from item_options.item_class import Item_Level

from editor_options.editor_brush_class import Editor_Brush

from game_options.player_statistic_class import Player_Statistic
from game_options.player_armor_class import Player_Armor

class Menu:
    def __init__(self, list_menu, logo):
        self.__menu_list = list_menu
        self.__menu_logo = logo

    def __draw_arrow(self, arrow_counter_in_menu, arrow_indication,menu_option_edit):
        if menu_option_edit:
            print()            
        else:
            if arrow_counter_in_menu == arrow_indication:
                print("<-")
            else:
                print()

    def __draw_logo(self):
        path = r'ascii_alphabet.txt'
        ascii_logo_to_draw = []
        alpha_ascii_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','v','x','y','z',' ','!','q']
        try:
            with open(path, 'r', encoding="UTF-8") as file:
                content = file.readlines()    
        except FileExistsError:
            print("Plik nie istnieje")
        for i in range(len(content)):
            content[i] = content[i].strip()
        for char_in_logo in self.__menu_logo:
            tmp = 0
            for char in alpha_ascii_list:
                if char == char_in_logo:
                    break            
                tmp += 1        
            i = 0
            if ascii_logo_to_draw == []:
                for i in range(7):
                    ascii_logo_to_draw.append(content[i + (tmp * 7)])
                    i += 1
            else:
                for i in range(7):
                    ascii_logo_to_draw[i] += content[i + (tmp * 7)]
                    i += 1
        for item in ascii_logo_to_draw:
            print(item)            
    
    def __draw_statistic(self, player_statistic):
        print(player_statistic.health)
        print(player_statistic.attack)
        print(player_statistic.defense)
        print(player_statistic.agility)

    def __validation_indication_in_menu(self, arrow_indication, size_max, size_min = 0 ):
        if arrow_indication < size_min:
            return size_max 
        elif arrow_indication > size_max:
            return size_min
        else:
            return arrow_indication

    def __menu_user_control(self, arrow_indication, size_max, size_min = 0):
        input_key = True
        while input_key:
            if keyboard.is_pressed('down'):
                arrow_indication += 1
                input_key = False                
                return self.__validation_indication_in_menu(arrow_indication, size_max, size_min)
            if keyboard.is_pressed('up'):
                arrow_indication -= 1
                input_key = False    
                return self.__validation_indication_in_menu(arrow_indication, size_max, size_min)
            if keyboard.is_pressed('left'):
                arrow_indication = 100
                input_key = False    
                return arrow_indication
            if keyboard.is_pressed('right'):
                arrow_indication = -100
                input_key = False    
                return arrow_indication

    def __draw_simple_menu(self, item):
        print("{}".format(item.item_name), end =" ")
    def __draw_min_max_menu(self, item, menu_min_max_edit):
        if menu_min_max_edit:
            print("{} : < {} >".format(item.item_name, item.actual_value), end =" ")
        else:
            print("{} : {}".format(item.item_name, item.actual_value), end =" ")
    def __draw_string_menu(self, item, menu_string_edit):
        if menu_string_edit:
            print("{} : {}_".format(item.item_name, item.actual_value), end = " ")
        else:
            print("{} : {}".format(item.item_name, item.actual_value), end =" ")
    def __draw_choose_menu(self, item, menu_choose_edit):
        if menu_choose_edit:
            print("{} : < {} >".format(item.item_name, item.actual_value), end = " ")
        else:
            print("{} : {}".format(item.item_name, item.actual_value), end = " ")
    
    def __menu_min_max_user_control(self, actual_value, size_max, size_min, step):
        input_key = True
        while input_key:
            if keyboard.is_pressed('up'):
                if actual_value < size_max:
                    return step
                else:
                    return 0
                input_key = False
            
            if keyboard.is_pressed('down'):
                if actual_value > size_min:
                    return -step
                else:
                    return 0
                input_key = False
               
            if keyboard.is_pressed('right'):
                actual_value = -100
                input_key = False    
                return actual_value    

    def __menu_string_user_control(self):
        input_key = True
        while input_key:
            if keyboard.is_pressed('right'):
                actual_value = -100
                input_key = False    
            if keyboard.is_pressed('backspace'):
                actual_value = -200
                input_key = False
            if keyboard.is_pressed('a'):
                actual_value = "a" 
                input_key = False    
            if keyboard.is_pressed('b'):
                actual_value = "b" 
                input_key = False
            if keyboard.is_pressed('c'):
                actual_value = "c" 
                input_key = False
            if keyboard.is_pressed('d'):
                actual_value = "d" 
                input_key = False
            if keyboard.is_pressed('e'):
                actual_value = "e" 
                input_key = False
            if keyboard.is_pressed('f'):
                actual_value = "f" 
                input_key = False
            if keyboard.is_pressed('g'):
                actual_value = "g" 
                input_key = False
            if keyboard.is_pressed('h'):
                actual_value = "h" 
                input_key = False
            if keyboard.is_pressed('i'):
                actual_value = "i" 
                input_key = False
            if keyboard.is_pressed('j'):
                actual_value = "j" 
                input_key = False
            if keyboard.is_pressed('k'):
                actual_value = "k" 
                input_key = False
            if keyboard.is_pressed('l'):
                actual_value = "l" 
                input_key = False
            if keyboard.is_pressed('m'):
                actual_value = "m" 
                input_key = False
            if keyboard.is_pressed('n'):
                actual_value = "n" 
                input_key = False
            if keyboard.is_pressed('s'):
                actual_value = "s" 
                input_key = False
            if keyboard.is_pressed('r'):
                actual_value = "r" 
                input_key = False
            if keyboard.is_pressed('o'):
                actual_value = "o" 
                input_key = False
            if keyboard.is_pressed('p'):
                actual_value = "p" 
                input_key = False
            if keyboard.is_pressed('t'):
                actual_value = "t" 
                input_key = False
            if keyboard.is_pressed('u'):
                actual_value = "u" 
                input_key = False
            if keyboard.is_pressed('v'):
                actual_value = "v" 
                input_key = False
            if keyboard.is_pressed('w'):
                actual_value = "w" 
                input_key = False
            if keyboard.is_pressed('y'):
                actual_value = "y" 
                input_key = False
            if keyboard.is_pressed('x'):
                actual_value = "x" 
                input_key = False
            if keyboard.is_pressed('z'):
                actual_value = "z" 
                input_key = False
            if keyboard.is_pressed('1'):
                actual_value = "1" 
                input_key = False
            if keyboard.is_pressed('2'):
                actual_value = "2" 
                input_key = False
            if keyboard.is_pressed('3'):
                actual_value = "3" 
                input_key = False
        return actual_value   

    def __menu_choose_user_control(self):
        input_key = True
        while input_key:
            if keyboard.is_pressed('down'):
                actual_value = -1
                input_key = False
            if keyboard.is_pressed('up'):
                actual_value = 1
                input_key = False
            if keyboard.is_pressed('right'):
                actual_value = -100
                input_key = False    
        return actual_value
    
    def use_menu(self, player_statistic = None, editor_mode= False, draw_logo = True ):
        arrow_indication = 0 #domyślna pozycja kursora
        tmp_arrow_indication = 0
        tmp_arrow_indication_str = ""
        size_menu = len(self.__menu_list) - 1
        run_menu = True
        menu_return_value = None
        menu_min_max_edit = False
        menu_min_max_object = None
        menu_string_edit = False
        menu_string_object = None
        menu_choose_edit = False
        menu_choose_object = None

        while run_menu:
            
            if draw_logo:
                os.system("cls")
                self.__draw_logo()

            if not player_statistic == None:
                self.__draw_statistic(player_statistic)

            arrow_counter_in_menu = 0
            for item in self.__menu_list: 
                if isinstance(item, simple_item_menu):
                    self.__draw_simple_menu(item)
                    self.__draw_arrow(arrow_counter_in_menu, arrow_indication, menu_min_max_edit)
                elif isinstance(item, min_max_item_menu):
                    if arrow_counter_in_menu == arrow_indication and menu_min_max_edit:
                        self.__draw_min_max_menu(item, True)
                    else:
                        self.__draw_min_max_menu(item, False)
                    # self.__draw_min_max_menu(item, menu_min_max_edit)
                    self.__draw_arrow(arrow_counter_in_menu, arrow_indication, menu_min_max_edit)
                elif isinstance(item, string_item_menu):
                    self.__draw_string_menu(item, menu_string_edit)
                    self.__draw_arrow(arrow_counter_in_menu, arrow_indication, menu_string_edit)
                elif isinstance(item, choose_item_menu):
                    self.__draw_choose_menu(item, menu_choose_edit)
                    self.__draw_arrow(arrow_counter_in_menu, arrow_indication, menu_choose_edit)
                arrow_counter_in_menu += 1

            if menu_min_max_edit:
                tmp_arrow_indication = self.__menu_min_max_user_control(menu_min_max_object.actual_value, menu_min_max_object.max_value, menu_min_max_object.min_value, menu_min_max_object.step)
            elif menu_string_edit:
                tmp = self.__menu_string_user_control()
                if isinstance(tmp, str):
                    tmp_arrow_indication_str = tmp                    
                else:
                    tmp_arrow_indication = tmp
            elif menu_choose_edit:
                tmp_arrow_indication = self.__menu_choose_user_control()
            else:                                
                tmp_arrow_indication = self.__menu_user_control(arrow_indication,size_menu)    
            
            if not menu_string_edit and not menu_min_max_edit and tmp_arrow_indication >= 100  :
                item = self.__menu_list[arrow_indication]

                if isinstance(item, simple_item_menu):                    
                    menu_return_value = item.item_value
                    run_menu = False
                elif isinstance(item, min_max_item_menu):                    
                    menu_min_max_edit = True
                    menu_min_max_object = item
                    tmp_arrow_indication = 0
                elif isinstance(item, string_item_menu):
                    menu_string_edit = True
                    menu_string_object = item
                    tmp_arrow_indication = 0
                elif isinstance(item, choose_item_menu):
                    menu_choose_edit = True
                    menu_choose_object = item
                    tmp_arrow_indication = 0

            #powrót do wyboru opcji
            if tmp_arrow_indication <= -100 and tmp_arrow_indication > -200:
                menu_min_max_edit = False
                menu_string_edit = False
                menu_choose_edit = False
                if editor_mode:
                    run_menu = False
            
            if menu_min_max_edit:
                if menu_min_max_object.actual_value == None:
                    menu_min_max_object.actual_value = 0
                    menu_min_max_object.actual_value += tmp_arrow_indication                
                else:
                    menu_min_max_object.actual_value += tmp_arrow_indication                
                
            elif menu_string_edit:
                if tmp_arrow_indication <= -200:
                    if len(menu_string_object.actual_value) > 0:
                        menu_string_object.actual_value = menu_string_object.actual_value[0:len(menu_string_object.actual_value)-1]
                        tmp_arrow_indication = 0
                else:
                    menu_string_object.actual_value += tmp_arrow_indication_str                      
            elif menu_choose_edit:
                menu_choose_object.actual_value = tmp_arrow_indication
            else:
                arrow_indication = self.__validation_indication_in_menu(tmp_arrow_indication, size_menu)
                
            time.sleep(0.21)    
            
        return menu_return_value

class simple_item_menu:
    def __init__(self, item_menu_name, menu_return_value):
        self.__item_menu_name = item_menu_name
        self.__item_menu_value = menu_return_value
    @property
    def item_name(self):
        return self.__item_menu_name
    @property
    def item_value(self):
        return self.__item_menu_value

class string_item_menu:
    def __init__(self, item_menu_name, option_object):
        self.__item_menu_name = item_menu_name
        self.__option_object = option_object

    @property
    def item_name(self):
        return self.__item_menu_name

    @property
    def actual_value(self):
        if isinstance(self.__option_object, Map_Name):
            return self.__option_object.name
        if isinstance(self.__option_object, Item_Name):
            return self.__option_object.name
    @actual_value.setter
    def actual_value(self, value):
        if isinstance(self.__option_object, Map_Name):
            self.__option_object.name = value
        if isinstance(self.__option_object, Item_Name):
            self.__option_object.name = value
    
class min_max_item_menu:
    #menu_return_value
    def __init__(self, item_menu_name, min_value, max_value, option_object, step=1):
        self.__item_menu_name = item_menu_name        
        self.__min_value = min_value
        self.__max_value = max_value
        self.__option_object = option_object
        self.__step = step        

    @property
    def step(self):
        return self.__step
    @property
    def min_value(self):
        return self.__min_value
    @property
    def max_value(self):
        return self.__max_value
    @property
    def item_name(self):
        return self.__item_menu_name
    
    @property
    def actual_value(self):
        if isinstance(self.__option_object, Map_Size):
            return self.__option_object.size   
        if isinstance(self.__option_object, Item_Value):
            return self.__option_object.value
        if isinstance(self.__option_object, Item_Count):
            return self.__option_object.count
        if isinstance(self.__option_object, Item_Attack):
            return self.__option_object.attack
        if isinstance(self.__option_object, Item_Defense):
            return self.__option_object.defense
        if isinstance(self.__option_object, Item_Health):
            return self.__option_object.health
        if isinstance(self.__option_object, Item_Agility):
            return self.__option_object.agility
        if isinstance(self.__option_object, Item_Level):
            return self.__option_object.level
        
    
    @actual_value.setter
    def actual_value(self, value):
        if isinstance(self.__option_object, Map_Size):
            self.__option_object.size = value
        if isinstance(self.__option_object, Item_Value):
            self.__option_object.value = value
        if isinstance(self.__option_object, Item_Count):
            self.__option_object.count = value
        if isinstance(self.__option_object, Item_Attack):
            self.__option_object.attack = value
        if isinstance(self.__option_object, Item_Defense):
            self.__option_object.defense = value
        if isinstance(self.__option_object, Item_Health):
            self.__option_object.health = value
        if isinstance(self.__option_object, Item_Agility):
            self.__option_object.agility = value
        if isinstance(self.__option_object, Item_Level):
            self.__option_object.level = value
        

class choose_item_menu:
    def __init__(self, item_menu_name, choose_list, option_object):
        self.__item_menu_name = item_menu_name
        self.__choose_list = choose_list
        self.__option_object = option_object
        self.__last_index = len(choose_list)-1
    @property
    def item_name(self):
        return self.__item_menu_name

    @property
    def actual_value(self):
        if isinstance(self.__option_object, Map_Type):
            return self.__option_object.type
        if isinstance(self.__option_object, Item_Type):
            return self.__option_object.type
        if isinstance(self.__option_object, Editor_Brush):
            return self.__option_object.size
        if isinstance(self.__option_object, Player_Armor):
            return self.__option_object.name
    
    @actual_value.setter
    def actual_value(self, value):
        
            if value == 1:
                self.__last_index += 1
                if self.__last_index == len(self.__choose_list):
                    self.__last_index = 0                
            elif value == -1:
                self.__last_index -= 1
                if self.__last_index < 0:
                    self.__last_index = len(self.__choose_list)-1
            if isinstance(self.__option_object, Map_Type):
                self.__option_object.type = self.__choose_list[self.__last_index]
            if isinstance(self.__option_object, Item_Type):
                self.__option_object.type = self.__choose_list[self.__last_index]
            if isinstance(self.__option_object, Editor_Brush):
                self.__option_object.size = self.__choose_list[self.__last_index]
            if isinstance(self.__option_object, Player_Armor):
                self.__option_object.name = self.__choose_list[self.__last_index]

