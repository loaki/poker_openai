import tkinter as tk
import customtkinter
from tkinter import ttk
import openai
from extractor.table_formater import Table_data
from frames.form import set_form

RANGES_FRAME = None

def set_ranges(root, ranges_table=None, ranges_frame=None):
    if ranges_frame:
        ranges_frame.place_forget()
        ranges_frame.destroy()

    start_x = 5
    start_y = 0
    pad_x = 90
    pad_y = 25
    n_y = 0

    ranges_frame = customtkinter.CTkFrame(root)

    tables_label = customtkinter.CTkLabel(ranges_frame, text='ranges', font=customtkinter.CTkFont(size=15, weight="bold"))
    tables_label.place(x=start_x+pad_x*1, y=pad_y*n_y)
    n_y+=2

    # table_var = tk.IntVar(value=0)
    ranges_table = {
            "AAo":1,"AKs":1,"AQs":0,"AJs":0,"ATs":0,"A9s":0,"A8s":0,"A7s":0,"A6s":0,"A5s":0,"A4s":0,"A3s":0,"A2s":0,
            "AKo":1,"KKo":1,"KQs":0,"KJs":0,"KTs":0,"K9s":0,"K8s":0,"K7s":0,"K6s":0,"K5s":0,"K4s":0,"K3s":0,"K2s":0,
            "AQo":1,"KQo":0,"QQo":0,"QJs":0,"QTs":0,"Q9s":0,"Q8s":0,"Q7s":0,"Q6s":0,"Q5s":0,"Q4s":0,"Q3s":0,"Q2s":0,
            "AJo":1,"KJo":0,"QJo":0,"JJo":0,"JTs":0,"J9s":0,"J8s":0,"J7s":0,"J6s":0,"J5s":0,"J4s":0,"J3s":0,"J2s":0,
            "ATo":0,"KTo":0,"QTo":0,"JTo":0,"TTo":0,"T9s":0,"T8s":0,"T7s":0,"T6s":0,"T5s":0,"T4s":0,"T3s":0,"T2s":0,
            "A9o":0,"K9o":0,"Q9o":0,"J9o":0,"T9o":0,"99o":0,"98s":0,"97s":0,"96s":0,"95s":0,"94s":0,"93s":0,"92s":0,
            "A8o":0,"K8o":0,"Q8o":0,"J8o":0,"T8o":0,"98o":0,"88o":0,"87s":0,"86s":0,"85s":0,"84s":0,"83s":0,"82s":0,
            "A7o":0,"K7o":0,"Q7o":0,"J7o":0,"T7o":0,"97o":0,"87o":0,"77o":0,"76s":0,"75s":0,"74s":0,"73s":0,"72s":0,
            "A6o":0,"K6o":0,"Q6o":0,"J6o":0,"T6o":0,"96o":0,"86o":0,"76o":0,"66o":0,"65s":0,"64s":0,"63s":0,"62s":0,
            "A5o":0,"K5o":0,"Q5o":0,"J5o":0,"T5o":0,"95o":0,"85o":0,"75o":0,"65o":0,"55o":0,"54s":0,"53s":0,"52s":0,
            "A4o":0,"K4o":0,"Q4o":0,"J4o":0,"T4o":0,"94o":0,"84o":0,"74o":0,"64o":0,"54o":0,"44o":0,"43s":0,"42s":0,
            "A3o":0,"K3o":0,"Q3o":0,"J3o":0,"T3o":0,"93o":0,"83o":0,"73o":0,"63o":0,"53o":0,"43o":0,"33o":0,"32s":0,
            "A2o":0,"K2o":0,"Q2o":0,"J2o":0,"T2o":0,"92o":0,"82o":0,"72o":0,"62o":0,"52o":0,"42o":0,"32o":0,"22o":0
        }
    for i, cell in enumerate(ranges_table):
        color = 'grey80' if ranges_table[cell] == 1 else 'grey50'
        cell_label = customtkinter.CTkLabel(ranges_frame, text=cell, width=19, height=19, fg_color=(color), text_color='black', font=customtkinter.CTkFont(size=8))
        cell_label.place(x=start_x+20*int(i%13), y=start_y+pad_y*n_y+20*int(i/13))

    n_y+=11
    ranges_frame.configure(width=pad_x*3, height=pad_y*n_y)
    ranges_frame.place(x=10, y=470)

    return ranges_frame
