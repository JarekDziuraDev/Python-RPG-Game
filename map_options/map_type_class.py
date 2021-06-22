class Map_Type:
    def __init__(self, map_type = ""):
        self.__map_type = map_type

    @property
    def map_type(self):
        return self.__map_type
    @map_type.setter
    def map_type(self, map_type):
        self.__map_type = map_type
