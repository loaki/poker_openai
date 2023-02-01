import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from extractor.extractor import extract_info
from extractor.table_formater import Table_data
from frames.forms import set_forms

OPENAI_KEY = os.getenv('OPENAI_KEY')
HISTORY_PATH=''
LOG_PATH=''

def set_tables(root):
    tables_frame = tk.LabelFrame(root, text='tables')

    start_x = 10
    start_y = 0
    pad_x = 100
    pad_y = 25
    n_y = 0
    window_pos = []
    window_selected = tk.IntVar(value=0)

    add_btn = tk.Button(tables_frame, text='add', command=lambda: add_win(
        tables_frame,
        window_pos,
        window_selected))
    add_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    del_btn = tk.Button(tables_frame, text='del', command=lambda: del_win(
        tables_frame,
        window_pos,
        window_selected.get()))
    del_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    select_btn = tk.Button(tables_frame, text='select', command=lambda: select_win(
        root,
        tables_frame,
        window_pos,
        window_selected.get()))
    select_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    print_dir = tk.Button(tables_frame, text='print', command=lambda: extract_info(
        tournament_id='',
        log_path=LOG_PATH,
        history_path=HISTORY_PATH))
    print_dir.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y+=1

    tables_frame.place(x=320, y=start_y, width=pad_x*3, height=start_y+pad_y*16)

def print_dire():
    print(LOG_PATH)

def select_log_path(tables_frame):
    global LOG_PATH
    LOG_PATH = filedialog.askdirectory()
    history_path_label = tk.Label(tables_frame, text=LOG_PATH)
    history_path_label.place(x=400, y=0)

def select_history_path(tables_frame):
    global HISTORY_PATH
    HISTORY_PATH = filedialog.askdirectory()
    history_path_label = tk.Label(tables_frame, text=HISTORY_PATH)
    history_path_label.place(x=400, y=25)

def add_win(tables_frame, window_pos, window_selected):
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
    win_btn = tk.Radiobutton(tables_frame, text=str(i), variable=window_selected, value=i)
    win_btn.grid(row=0, column=6+i)
    window_pos.append((win_btn, i, id, 0))
    
def del_win(tables_frame, window_pos, window_selected):
    for i, win in enumerate(window_pos):
        if win[1] == window_selected:
            win[0].grid_forget()
            window_pos.pop(i)

def select_win(root, tables_frame, window_pos, window_selected):

    win = next((w for w in window_pos if w[1] == window_selected), ('null', -1, 0))
    table_id_label = tk.Label(tables_frame, text=win[2])
    table_id_label.place(x=440, y=42)
    image = Image.open('screen.png')
    ratio = max(image.size[0] / 280, image.size[1] / 280)
    image = image.resize((int(image.size[0] / ratio), int(image.size[1] / ratio)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    img_label = tk.Label(tables_frame, image=img)
    img_label.image=img
    img_label.place(x=440, y=62)

    table_data = Table_data()
    table_data.pot = 30.2
    table_data.hand_1 = (3, 2)
    set_forms(root, table_data)
