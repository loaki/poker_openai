import tkinter as tk
import customtkinter
from tkinter import ttk
import openai
from extractor.table_formater import Table_data
from frames.form import set_form

FORM_FRAME = None

def set_tables(root, tables, form_frame, tables_frame=None):
    global FORM_FRAME
    if not FORM_FRAME:
        FORM_FRAME = form_frame

    if tables_frame:
        tables_frame.place_forget()
        tables_frame.destroy()

    start_x = 10
    start_y = 0
    pad_x = 90
    pad_y = 25
    n_y = 0

    tables_frame = customtkinter.CTkFrame(root)

    tables_label = customtkinter.CTkLabel(tables_frame, text='tables', font=customtkinter.CTkFont(size=15, weight="bold"))
    tables_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y+=2

    table_var = tk.IntVar(value=0)
    for i, table in enumerate(tables):
        table_drop = customtkinter.CTkRadioButton(tables_frame, text=table, variable=table_var, value=i+1, command=lambda: select_table(root, tables, table_var.get()))
        table_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
        n_y+=1

    n_y+=1
    tables_frame.place(x=pad_x*3+20, y=10, width=pad_x*2, height=start_y+pad_y*n_y)

    return tables_frame

def select_table(root, tables, value):
    print(tables[value - 1])
    table_data = Table_data()
    table_data.stack = 201
    table_data.pot = 30.2
    table_data.hand_1 = (3, 2)
    table_data.hand_2 = (1, 0)
    global FORM_FRAME
    FORM_FRAME = set_form(root, table_data, FORM_FRAME)