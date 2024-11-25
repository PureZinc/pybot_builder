import tkinter as tk


class ViewScreen:
    def __init__(self, width:int=500, height:int=500) -> None:
        self.width = width
        self.height = height
        self.dimensions = (width, height)

    def convert_to_tk(self) -> tk.Tk:
        root = tk.Tk()
        root.title("Robot Interface")
        root.geometry(f"{self.width}x{self.height}")
        # Extras Here
        return root


class Controller:
    pass
