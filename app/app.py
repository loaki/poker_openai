import os
import tkinter as tk
from dotenv import load_dotenv
from tkinter import ttk, filedialog
import openai
from PIL import ImageTk, Image
from extractor.extractor import extract_info
from extractor.table_formater import Table_data
from frames.forms import set_forms
from frames.tables import set_tables, select_log_path, select_history_path

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
HISTORY_PATH=''
LOG_PATH=''

def set_menu(root, menu):
    config_menu = tk.Menu(menu)
    menu.add_cascade(label='Config', menu=config_menu)
    config_menu.add_command(label='log', command=lambda: select_log_path(root))
    config_menu.add_command(label='historic', command=lambda: select_history_path(root))

def app():
    root = tk.Tk()
    root.title('Poker OpenAI')
    
    root.geometry('730x720')
    table_data = Table_data()
    menu = tk.Menu(root)
    root.config(menu=menu)
    set_menu(root, menu)
    set_forms(root, table_data)
    set_tables(root)
    root.mainloop()

if __name__ == '__main__':
    app()


