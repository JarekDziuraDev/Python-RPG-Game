class Map_Name:
    def __init__(self, map_name = ""):
        self.__map_name = map_name

    @property
    def map_name(self):
        return self.__map_name
    @map_name.setter
    def map_name(self, map_name):
        self.__map_name = map_name