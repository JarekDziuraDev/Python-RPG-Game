class Editor_Brush:
    def __init__(self):
        self.brush_menu = False
        self.brush_use = False    
        self.__actual_brush = 0
        self.actual_position_y = None
        self.actual_position_x = None
        self.size = Const_Editor.brush_small

    @property
    def actual_brush(self):
        self.brush_use = False
        return self.__actual_brush

    @actual_brush.setter
    def actual_brush(self, value):
        self.brush_menu = False
        self.__actual_brush = value

    # @property
    # def brush_use(self):
    #     return self.__brush_use

class Const_Editor:
    def __init__(self):
        pass
    width = 30
    height = 15

    water = 0
    grass1 = 1
    sand = 2
    port1 = 3
    rock = 4
    grass2 = 5
    #kraken = 4
    #shark = 5
    brush_small = "brush_small"
    brush_medium = "brush_medium"
    brush_big = "brush_big"

    