import tkinter as tk
from extractor.table_formater import Table_data
from frames.form import set_form
from frames.tables import set_tables, select_log_path, select_history_path

def set_menu(root, menu):
    config_menu = tk.Menu(menu)
    menu.add_cascade(label='Config', menu=config_menu)
    config_menu.add_command(label='log path', command=lambda: select_log_path())
    config_menu.add_command(label='history path', command=lambda: select_history_path())

def app():
    root = tk.Tk()
    root.title('Poker OpenAI')
    root.geometry('630x610')
    table_data = Table_data()
    menu = tk.Menu(root)
    root.config(menu=menu)
    set_menu(root, menu)
    set_form(root, table_data)
    set_tables(root)
    root.mainloop()

if __name__ == '__main__':
    app()
