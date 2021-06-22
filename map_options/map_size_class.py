class Map_Size:
    def __init__(self, size_map):
        self.__map_size = size_map

    @property
    def map_size(self):
        return self.__map_size
    @map_size.setter
    def map_size(self, map_size):
        self.__map_size = map_size