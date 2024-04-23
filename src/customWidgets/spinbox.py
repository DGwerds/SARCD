from customtkinter import CTkFrame, CTkLabel
from tkinter import Spinbox


class CSpinbox(CTkFrame):
    def __init__(self, master, value, name: str, max_value: float, min_value: float = 1, increment: float = 1,
                 width: int = 4):
        super().__init__(master=master)
        label = CTkLabel(self, text=str(name))
        label.grid(row=0, column=0, sticky="nsew")

        sb1 = Spinbox(self, from_=min_value, to=max_value, width=int(width), increment=increment,
                      textvariable=value)
        sb1.grid(row=1, column=0, padx=5, sticky="nsew")
