import tkinter as tk
from tkinter import *


class Spinbox(Frame):
    def __init__(self, master, name: str, value, max_value: float, min_value: float = 1, increment: float = 1,
                 width: int = 4, bg: str = None):
        super().__init__(master=master, bg=bg)
        l = tk.Label(self, text=str(name), bg=bg)
        l.grid(row=0, column=0, sticky="nsew")

        sb1 = tk.Spinbox(self, from_=min_value, to=max_value, width=int(width), increment=increment,
                         textvariable=value)
        sb1.grid(row=1, column=0, padx=5, sticky="nsew")


