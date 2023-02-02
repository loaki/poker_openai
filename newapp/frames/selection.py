import os
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import ImageTk, Image
from dotenv import load_dotenv
from configparser import ConfigParser
from extractor.extractor import extract_info, get_all_tournaments_id
from extractor.table_formater import Table_data, format_table_data
from frames.form import set_form

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

parser = ConfigParser()
parser.read('config.ini')
LOG_PATH = parser.get('path', 'log')
HISTORY_PATH = parser.get('path', 'history')

FORM_FRAME = None

def set_selection(root, form_frame, selection_form=None):
    global FORM_FRAME
    FORM_FRAME = form_frame

    start_x = 10
    start_y = 0
    pad_x = 90
    pad_y = 25
    n_y = 0
    window_pos = []
    window_selected = tk.IntVar(value=0)

    selection_frame = customtkinter.CTkFrame(root)

    selection_label = customtkinter.CTkLabel(selection_frame, text='selection', font=customtkinter.CTkFont(size=15, weight="bold"))
    selection_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y+=2

    table_label = customtkinter.CTkLabel(selection_frame, text='tables config')
    table_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y+=1

    add_table_list = ['hehe', '132', '321']
    add_drop = customtkinter.CTkOptionMenu(selection_frame, values=add_table_list, width=80, height=25, command=lambda: add_table(
        selection_frame,
        window_pos,
        window_selected))
    add_drop.set('add')
    add_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, height=25)
    n_y += 1

    del_table_list = ['aze', '132', '321']
    del_drop = customtkinter.CTkOptionMenu(selection_frame, values=del_table_list, width=80, height=25, command=lambda: del_table(
        selection_frame,
        window_pos,
        window_selected))
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

    reload_drop = customtkinter.CTkButton(selection_frame, text='reload')
    reload_drop.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, width=80, height=25)
    n_y += 2

    selection_frame.place(x=pad_x*5+30, y=10, width=pad_x*2, height=start_y+pad_y*n_y)

    return del_table_list

# def table_info(root, tournament_id, log_path=LOG_PATH, history_path=HISTORY_PATH):
#     tournament_id = '603580838'
#     data = extract_info(tournament_id, log_path=LOG_PATH, history_path=HISTORY_PATH)
#     table_data = format_table_data(data)
#     set_form(root, table_data)

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

def add_table(selection_frame, window_pos, window_selected):
    tournaments_id = get_all_tournaments_id(10, LOG_PATH)

    
    if len(window_pos) >= 6:
        return
    if len(window_pos):
        i = 0
        for a, b in enumerate(sorted(window_pos, key = lambda x: x[1]), 1):
            if a != b[1]:
                break
            i = a
        i += 1
    else:
        i = 1
    id = '1111'
    win_btn = tk.Radiobutton(selection_frame, text=str(i), variable=window_selected, value=i)
    win_btn.grid(row=0, column=6+i)
    window_pos.append((win_btn, i, id, 0))
    
def del_table(selection_frame, window_pos, window_selected):
    for i, win in enumerate(window_pos):
        if win[1] == window_selected:
            win[0].grid_forget()
            window_pos.pop(i)

# def select_table(root, selection_frame, window_pos, window_selected):
#     win = next((w for w in window_pos if w[1] == window_selected), ('null', -1, 0))
#     table_id_label = tk.Label(selection_frame, text=win[2])
#     table_id_label.place(x=440, y=42)
#     image = Image.open('screen.png')
#     ratio = max(image.size[0] / 280, image.size[1] / 280)
#     image = image.resize((int(image.size[0] / ratio), int(image.size[1] / ratio)), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(image)
#     img_label = tk.Label(selection_frame, image=img)
#     img_label.image=img
#     img_label.place(x=440, y=62)

#     table_data = Table_data()
#     table_data.pot = 30.2
#     table_data.hand_1 = (3, 2)
#     global FORM_FRAME
#     FORM_FRAME = set_form(root, table_data, FORM_FRAME)
