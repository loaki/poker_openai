import tkinter as tk
import customtkinter
from configparser import ConfigParser
from extractor.table_formater import Table_data
from extractor.extractor import get_all_tournaments_id
from frames.form import set_form
from frames.selection import set_selection
from frames.tables import set_tables

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

parser = ConfigParser()
parser.read('config.ini')
LOG_PATH = parser.get('path', 'log')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Poker OpenAI')
        self.geometry('670x800')
        
        table_data = Table_data()
        menu = tk.Menu(self)
        self.config(menu=menu)
        form_frame = set_form(self, table_data)
        tables_frame = set_tables(self, [], form_frame)
        add_tables = get_all_tournaments_id(9, LOG_PATH)
        set_selection(self, form_frame, tables_frame, add_tables)

if __name__ == '__main__':
    app = App()
    app.mainloop()
