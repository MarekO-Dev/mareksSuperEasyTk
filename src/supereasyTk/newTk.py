from tkinter import *
from typing import Any

class Validator:
    
    @classmethod
    def window_size_for_geometry(
            
            cls, 
            window_size: tuple, 
            geometry: bool = True) -> str:

        if type(window_size) == tuple or type(window_size) == list:
            return f"{window_size[0]}x{window_size[1]}"
        else:
            return "800x600"
            
class Application(Tk):
    
    # All elements created with add_element method
    _all_elements: list = []

    def __init__(
        
            self,
            window_size: tuple = (width := 800, height := 600),
            /,
            app_title = "tk"):
        
        super().__init__()
        self._window_size: str = Validator.window_size_for_geometry(window_size)
        self.title(app_title)

    def __call__(self):
        self.mainloop()

    @property
    def size(self):
        """
            Gets window size: (width, height)
        """
        return self._window_size
    
    @size.setter
    def size(
            self, 
            new_size: tuple):
        """
            Sets new window size
        """
        self._window_size = Validator.window_size_for_geometry(new_size)

    
    def add_element(
            self,
            /,
            element_reference, 
            element_options: dict,
            *,
            element_window_manager: str = "grid",
            element_window_manager_options: dict,
            overriden_master = None):

        """
            ### Args:

            #### element_reference: tkinter Widget
        
                - Button, Frame, Label etc

            #### element_window_manager: str
                - "grid", "pack", "place"

            #### element_window_manager_options: dict
                - example
                    ```python
                { 
                "row": 1,
                "column": 0,
                "sticky": NSEW
                }
                    ```

        """

        if overriden_master is not None:
            new_element = element_reference(overriden_master, **element_options)
        else:
            new_element = element_reference(self, **element_options)
        
        # Different actions based on different window manager

        match element_window_manager:
            case "grid":
                new_element.grid(**element_window_manager_options)
            case "place":
                new_element.place(**element_window_manager_options)
            case "pack":
                new_element.pack(**element_window_manager_options)

        self._all_elements.append(new_element)

        #return self for method chaining
        return self