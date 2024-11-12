from tkinter import *
from typing import Any

class Validator:
    @classmethod
    def window_size_for_geometry(
            
            cls, 
            window_size: tuple, 
            geometry = True) -> str:

        if type(window_size) == tuple or type(window_size) == list:
            return f"{window_size[0]}x{window_size[1]}"
        else:
            return "800x600"
            

class Application(Tk):
    def __init__(self,
        window_size: tuple = (800, 600)):
        super().__init__()

        self._window_size: str = Validator.window_size_for_geometry(window_size)

    @property
    def size(
            self):
        '''
            Gets window size: (width, height)
        '''
        return self._window_size
    
    @size.setter
    def size(
            self, 
            new_size: tuple):
        '''
            Sets new window size
        '''
        self._window_size = Validator.window_size_for_geometry(new_size)