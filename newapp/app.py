import tkinter as tk
import customtkinter

from extractor.table_formater import Table_data
from frames.form import set_form
from frames.selection import set_selection, select_log_path, select_history_path
from frames.tables import set_tables

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Poker OpenAI')
        self.geometry('800x800')
        
        table_data = Table_data()
        menu = tk.Menu(self)
        self.config(menu=menu)
        form_frame = set_form(self, table_data)
        tables = set_selection(self, form_frame)
        set_tables(self, tables, form_frame)

if __name__ == '__main__':
    app = App()
    app.mainloop()
