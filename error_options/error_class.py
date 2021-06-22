import os
import time

class Error_Message:
    def __init__(self):
        pass
    
    @classmethod
    def Msg(cls, msg, tim):
        os.system("cls || clear")
        print(f"{msg}")
        time.sleep(tim)