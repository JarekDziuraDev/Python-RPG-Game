class Map:
    def __init__(self, map_id = None, map_name = "", map_size = None, map_type = None):
        self.id = map_id
        self.type = map_type
        self.name = map_name
        self.size = map_size
        self.map = None
    

class Map_Size:
    def __init__(self):
        self.size = None

class Map_Name:
    def __init__(self):
        self.name = ""

class Map_Type:
    def __init__(self):
        self.type = None

class Map_Id:
    def __init__(self):
        self.id = None
