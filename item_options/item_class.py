#from main.const_enum_class import Const
import os
import sys

sys.path.append(os.getcwd())
sys.path.append("..")

#from const_enum.item_type_const import Item_Type_Const

class Item_Material:
    def __init__(self, id, mtype, name, value, count):
        self.id = id
        self.name = name
        self.type = mtype        
        self.value = value
        self.count = count

class Item_Equipment:
    def __init__(self, id, mtype, name, value, health, attack, defense, agility):
        self.id = id
        self.name = name
        self.type = mtype
        self.value = value
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility

class Item_Enemy:
    def __init__(self, id, mtype, name, level, health, attack, defense, agility):
        self.id = id
        self.type = mtype
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility

class Item_Id:
    def __init__(self):
        self.id = None

class Item_Type:
    def __init__(self):
        self.type = None

class Item_Name:
    def __init__(self):
        self.name = ""

class Item_Value:
    def __init__(self):
        self.value = None

class Item_Count:
    def __init__(self):
        self.count = None

class Item_Attack:
    def __init__(self):
        self.attack = None

class Item_Defense:
    def __init__(self):
        self.defense = None
    
class Item_Health:
    def __init__(self):
        self.health = None

class Item_Agility:
    def __init__(self):
        self.agility = None

class Item_Level:
    def __init__(self):
        self.level = None