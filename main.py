import keyboard

import os

from edytor_class import Edytor

from menu_class import simple_item_menu
from menu_class import min_max_item_menu
from menu_class import string_item_menu
from menu_class import choose_item_menu
from menu_class import Menu
from game_class import Game


from const_enum_class import Const


if __name__ == "__main__":

    new_game_simple_im = simple_item_menu("New game", Const.new_game)
    edytor_simple_im = simple_item_menu("Edytor", Const.edytor)
    quit_game_simple_im = simple_item_menu("Koniec", Const.quit_game)

    new_map_simple_im = simple_item_menu("New map", Const.edytor_new_map)
    new_item_simle_im = simple_item_menu("New item", Const.edytor_new_item)
    new_enemy_simle_im = simple_item_menu("New enemy", Const.edytor_new_enemy)

    list_item_simple_im = simple_item_menu("Item list", Const.edytor_item_list)
    load_map_simple_im = simple_item_menu("Load map", Const.edytor_load_map)


    main_menu = Menu([
        new_game_simple_im,
        edytor_simple_im,
        quit_game_simple_im],
         "rougelike game !")

    edytor_menu = Menu([
        new_map_simple_im,
        new_item_simle_im,
        new_enemy_simle_im,
        load_map_simple_im,
        quit_game_simple_im],
        "editor menu")

    run_game = True
    run_editor = True

    edytor = Edytor()
    game = Game()
    
    while run_game:

        options = main_menu.use_menu()

        if options == Const.new_game:
            game.start_game()        
        elif options == Const.edytor:
            while options == Const.edytor:

                options = edytor_menu.use_menu()
                    
                if options == Const.edytor_new_item:
                    options = edytor.create_item()                
                elif options == Const.edytor_new_enemy:
                    options = edytor.create_enemy()
                elif options == Const.edytor_new_map:
                    options = edytor.create_map()
                elif options == Const.edytor_load_map:
                    options = edytor.load_map_menu()
                    if options == Const.quit_game:
                        options = Const.edytor
                    else:
                        edytor.set_map(options)            

        elif options == Const.quit_game:
            run_game = False

        

input("Exit")