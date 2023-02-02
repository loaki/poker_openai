import os
import tkinter as tk
from tkinter import filedialog
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

def set_tables(root, form_frame):
    global FORM_FRAME
    FORM_FRAME = form_frame

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
    add_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, height=25)
    n_y += 1

    del_btn = tk.Button(tables_frame, text='del', command=lambda: del_win(
        tables_frame,
        window_pos,
        window_selected.get()))
    del_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, height=25)
    n_y += 1

    select_btn = tk.Button(tables_frame, text='select', command=lambda: select_win(
        root,
        tables_frame,
        window_pos,
        window_selected.get()))
    select_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, height=25)
    n_y += 1

    print_dir = tk.Button(tables_frame, text='print', command=lambda: table_info(
        root,
        tournament_id='',
        log_path=LOG_PATH,
        history_path=HISTORY_PATH))
    print_dir.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y, height=25)
    n_y+=1

    tables_frame.place(x=320, y=start_y, width=pad_x*3, height=start_y+pad_y*16)

def table_info(root, tournament_id, log_path=LOG_PATH, history_path=HISTORY_PATH):
    tournament_id = '603580838'
    data = extract_info(tournament_id, log_path=LOG_PATH, history_path=HISTORY_PATH)
    table_data = format_table_data(data)
    set_form(root, table_data)

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

def add_win(tables_frame, window_pos, window_selected):
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
    global FORM_FRAME
    FORM_FRAME = set_form(root, table_data, FORM_FRAME)
