import tkinter as tk
from tkinter import ttk
from tkinter import *


class OptionMenu(Frame):
    def __init__(self, master, name: str, value: StringVar, values: tuple | dict, bg: str = None):
        super().__init__(master=master, bg=bg)
        tk.Label(self, text=str(name), bg=bg).grid(row=0, column=0, sticky="nsew")
        option_menu = ttk.OptionMenu(self, value, values[0], *values)
        option_menu.grid(row=1, column=0, padx=5, sticky="nsew")
