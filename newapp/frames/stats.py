import tkinter as tk
import customtkinter
from tkinter import ttk
import openai
from extractor.table_formater import Table_data
from frames.form import set_form

STATS_FRAME = None

def set_stats(root, stats_frame=None):
    if stats_frame:
        stats_frame.place_forget()
        stats_frame.destroy()

    start_x = 10
    start_y = 0
    pad_x = 90
    pad_y = 25
    n_y = 0

    stats_frame = customtkinter.CTkFrame(root)

    tables_label = customtkinter.CTkLabel(stats_frame, text='stats', font=customtkinter.CTkFont(size=15, weight="bold"))
    tables_label.place(x=start_x+pad_x*1, y=pad_y*n_y)
    n_y+=2

    stats_frame.configure(width=pad_x*4+10, height=pad_y*19)
    stats_frame.place(x=290, y=320)

    return stats_frame
