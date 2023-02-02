import os
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import ImageTk, Image
from dotenv import load_dotenv
from configparser import ConfigParser
from extractor.extractor import extract_info, get_all_tournaments_id, get_tournament_name
from extractor.table_formater import Table_data, format_table_data
from frames.tables import set_tables

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

parser = ConfigParser()
parser.read('config.ini')
LOG_PATH = parser.get('path', 'log')
HISTORY_PATH = parser.get('path', 'history')

FORM_FRAME = None
TABLES_FRAME = None

def set_selection(root, form_frame, tables_frame, tables=[], selection_frame=None):
    global FORM_FRAME
    global TABLES_FRAME
    FORM_FRAME = form_frame
    TABLES_FRAME = form_frame

    start_x = 10
    start_y = 0
    pad_x = 90
    pad_y = 25
    n_y = 0

    selection_frame = customtkinter.CTkFrame(root)

    selection_label = customtkinter.CTkLabel(selection_frame, text='selection', font=customtkinter.CTkFont(size=15, weight="bold"))
    selection_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y+=2

    table_label = customtkinter.CTkLabel(selection_frame, text='tables config')
    table_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y+=1

    add_table_list = get_all_tournaments_id(10, LOG_PATH)
    add_table_var = customtkinter.StringVar(value='')
    add_drop = customtkinter.CTkOptionMenu(selection_frame, values=add_table_list, width=80, height=25, variable=add_table_var, command=lambda table: add_table(
        root,
        tables,
        selection_frame,
        tables_frame,
        table
    ))
    add_drop.set('add')
    add_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, height=25)
    n_y += 1

    del_table_var = customtkinter.StringVar(value='')
    del_drop = customtkinter.CTkOptionMenu(selection_frame, values=tables, width=80, height=25, variable=del_table_var, command=lambda table: del_table(
        root,
        tables,
        selection_frame,
        tables_frame,
        table
    ))
    del_drop.set('del')
    del_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, height=25)
    n_y += 2

    path_label = customtkinter.CTkLabel(selection_frame, text='path config')
    path_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y+=1

    log_drop = customtkinter.CTkButton(selection_frame, text='log', command=select_log_path)
    log_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, width=80, height=25)
    n_y += 1

    history_drop = customtkinter.CTkButton(selection_frame, text='history', command=select_history_path)
    history_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, width=80, height=25)
    n_y += 2

    reload_drop = customtkinter.CTkButton(selection_frame, text='reload', command=lambda: reload(
        root,
        tables,
        selection_frame
    ))
    reload_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, width=80, height=25)
    n_y += 2

    selection_frame.place(x=pad_x*5+30, y=10, width=pad_x*2, height=start_y+pad_y*n_y)

def select_log_path():
    global LOG_PATH
    LOG_PATH = filedialog.askdirectory()
    parser = ConfigParser()
    parser.read('config.ini')
    parser.set('path', 'log', LOG_PATH)
    with open('config.ini', 'w') as f:
        parser.write(f)

def select_history_path():
    global HISTORY_PATH
    HISTORY_PATH = filedialog.askdirectory()
    parser = ConfigParser()
    parser.read('config.ini')
    parser.set('path', 'history', HISTORY_PATH)
    with open('config.ini', 'w') as f:
        parser.write(f)

def add_table(root, tables, selection_frame, tables_frame, table):
    global FORM_FRAME
    tables.append(table)
    print(tables)
    print(table)
    set_selection(root, FORM_FRAME, tables_frame, tables, selection_frame)
    set_tables(root, tables, FORM_FRAME, tables_frame)
    
def del_table(root, tables, selection_frame, tables_frame, table):
    global FORM_FRAME
    tables.remove(table)
    set_selection(root, FORM_FRAME, tables_frame, tables, selection_frame)
    set_tables(root, tables, FORM_FRAME, tables_frame)


def reload(root, tables, selection_frame):
    global FORM_FRAME
    set_selection(root, FORM_FRAME, tables, selection_frame)
