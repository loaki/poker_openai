import os
import tkinter as tk
from dotenv import load_dotenv
from tkinter import ttk, filedialog
import openai
from PIL import ImageTk, Image
from extractor.extractor import extract_info
from extractor.table_formater import Table_data

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
HISTORY_PATH=''
LOG_PATH=''

def set_menu(root, menu):
    config_menu = tk.Menu(menu)
    menu.add_cascade(label='Config', menu=config_menu)
    config_menu.add_command(label='log', command=lambda: select_log_path(root))
    config_menu.add_command(label='historic', command=lambda: select_history_path(root))

def set_forms(root, data):
    start_x = 0
    start_y = 0
    pad_x = 100
    pad_y = 25
    n_y = 0

    table_nbplayer_label = tk.Label(root, text='players on table')
    table_nbplayer_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    table_nbplayer_options = [2,3,4,5,6,7,8,9]
    table_nbplayer_drop = ttk.Combobox(root, value=table_nbplayer_options, width=10)
    table_nbplayer_drop.current(data.table_nbplayer)
    table_nbplayer_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    position_label = tk.Label(root, text='position')
    position_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    position_drop = ttk.Combobox(root, value=data.position_options, width=10)
    position_drop.current(data.position)
    position_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    nb_player_in_label = tk.Label(root, text='players in')
    nb_player_in_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    nb_player_in_options = [0,1,2,3,4,5,6,7,8,9]
    nb_player_in_drop = ttk.Combobox(root, value=nb_player_in_options, width=10)
    nb_player_in_drop.current(data.nb_player_in)
    nb_player_in_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    round_label = tk.Label(root, text='round')
    round_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    round_drop = ttk.Combobox(root, value=data.round_options, width=10)
    round_drop.current(data.round)
    round_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    stack_label = tk.Label(root, text='stack')
    stack_label.place(x=start_x+pad_x*0, y=start_y+pad_y*(n_y))
    stack_val = tk.DoubleVar(value=data.stack)
    stack_input = ttk.Entry(root, textvariable=stack_val, width=6)
    stack_input.place(x=start_x+pad_x*1, y=start_y+pad_y*(n_y))
    stack_max = 100 if data.stack < 100 else (int(data.stack / 100) + 1) * 100
    stack_scale = tk.Scale(root, from_=0, to=stack_max, orient=tk.HORIZONTAL, length=100, variable=stack_val, showvalue=0)
    stack_scale.place(x=start_x+pad_x*1+50, y=start_y+pad_y*n_y)
    n_y+=1

    pot_label = tk.Label(root, text='pot size')
    pot_label.place(x=start_x+pad_x*0, y=start_y+pad_y*(n_y))
    pot_val = tk.DoubleVar(value=data.pot)
    pot_input = ttk.Entry(root, textvariable=pot_val, width=6)
    pot_input.place(x=start_x+pad_x*1, y=start_y+pad_y*(n_y))
    pot_max = 100 if data.pot < 100 else (int(data.pot / 100) + 1) * 100
    pot_scale = tk.Scale(root, from_=0, to=pot_max, orient=tk.HORIZONTAL, length=100, variable=pot_val, showvalue=0)
    pot_scale.place(x=start_x+pad_x*1+50, y=start_y+pad_y*n_y)
    n_y+=1

    call_label = tk.Label(root, text='min to call')
    call_label.place(x=start_x+pad_x*0, y=start_y+pad_y*(n_y))
    call_val = tk.DoubleVar(value=data.call)
    call_input = ttk.Entry(root, textvariable=call_val, width=6)
    call_input.place(x=start_x+pad_x*1, y=start_y+pad_y*(n_y))
    call_max = 100 if data.call < 100 else (int(data.call / 100) + 1) * 100
    call_scall = tk.Scale(root, from_=0, to=call_max, orient=tk.HORIZONTAL, length=100, variable=call_val, showvalue=0)
    call_scall.place(x=start_x+pad_x*1+50, y=start_y+pad_y*n_y)
    n_y+=1

    hand1_label = tk.Label(root, text='hand1')
    hand1_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    hand_v1_drop = ttk.Combobox(root, value=data.card_value_options, width=10)
    if data.hand_1[0] != -1:
        hand_v1_drop.current(data.hand_1[0])
    hand_v1_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    hand_s1_drop = ttk.Combobox(root, value=data.card_symbol_options, width=10)
    if data.hand_1[1] != -1:
        hand_s1_drop.current(data.hand_1[1])
    hand_s1_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1
    
    hand2_label = tk.Label(root, text='hand2')
    hand2_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    hand_v2_drop = ttk.Combobox(root, value=data.card_value_options, width=10)
    if data.hand_2[0] != -1:
        hand_v2_drop.current(data.hand_2[0])
    hand_v2_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    hand_s2_drop = ttk.Combobox(root, value=data.card_symbol_options, width=10)
    if data.hand_2[1] != -1:
        hand_s2_drop.current(data.hand_2[1])
    hand_s2_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card1_label = tk.Label(root, text='card1')
    card1_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v1_drop = ttk.Combobox(root, value=data.card_value_options, width=10)
    if data.board_1[0] != -1:
        card_v1_drop.current(data.board_1[0])
    card_v1_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s1_drop = ttk.Combobox(root, value=data.card_symbol_options, width=10)
    if data.board_1[1] != -1:
        card_s1_drop.current(data.board_1[1])
    card_s1_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card2_label = tk.Label(root, text='card2')
    card2_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v2_drop = ttk.Combobox(root, value=data.card_value_options, width=10)
    if data.board_2[0] != -1:
        card_v2_drop.current(data.board_2[0])
    card_v2_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s2_drop = ttk.Combobox(root, value=data.card_symbol_options, width=10)
    if data.board_2[1] != -1:
        card_s2_drop.current(data.board_2[1])
    card_s2_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card3_label = tk.Label(root, text='card3')
    card3_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v3_drop = ttk.Combobox(root, value=data.card_value_options, width=10)
    if data.board_3[0] != -1:
        card_v3_drop.current(data.board_3[0])
    card_v3_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s3_drop = ttk.Combobox(root, value=data.card_symbol_options, width=10)
    if data.board_3[1] != -1:
        card_s3_drop.current(data.board_3[1])
    card_s3_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card4_label = tk.Label(root, text='card4')
    card4_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v4_drop = ttk.Combobox(root, value=data.card_value_options, width=10)
    if data.board_4[0] != -1:
        card_v4_drop.current(data.board_4[0])
    card_v4_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s4_drop = ttk.Combobox(root, value=data.card_symbol_options, width=10)
    if data.board_4[1] != -1:
        card_s4_drop.current(data.board_4[1])
    card_s4_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card5_label = tk.Label(root, text='card5')
    card5_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v5_drop = ttk.Combobox(root, value=data.card_value_options, width=10)
    if data.board_5[0] != -1:
        card_v5_drop.current(data.board_5[0])
    card_v5_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s5_drop = ttk.Combobox(root, value=data.card_symbol_options, width=10)
    if data.board_5[1] != -1:
        card_s5_drop.current(data.board_5[1])
    card_s5_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    send_btn = tk.Button(root, text='send', command=lambda: send(
        root,
        table_nbplayer_drop.get(),
        position_drop.get(),
        nb_player_in_drop.get(),
        round_drop.get(),
        stack_val.get(),
        pot_val.get(),
        call_val.get(),
        hand_v1_drop.get(),
        hand_s1_drop.get(),
        hand_v2_drop.get(),
        hand_s2_drop.get(),
        card_v1_drop.get(),
        card_s1_drop.get(),
        card_v2_drop.get(),
        card_s2_drop.get(),
        card_v3_drop.get(),
        card_s3_drop.get(),
        card_v4_drop.get(),
        card_s4_drop.get(),
        card_v5_drop.get(),
        card_s5_drop.get()
    ))
    send_btn.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)

    answer_label = tk.Text(root, width=42, height= 20)
    answer_label.insert(tk.INSERT, 'hello')
    answer_label.place(x=370, y=360)

def set_detection(root):
    start_x = 300
    start_y = 0
    pad_x = 100
    pad_y = 25
    n_y = 0
    window_pos = []
    window_selected = tk.IntVar(value=0)

    detection_label = tk.Label(root, text='tables')
    detection_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    add_btn = tk.Button(root, text='add', command=lambda: add_win(
        root,
        window_pos,
        window_selected))
    add_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    del_btn = tk.Button(root, text='del', command=lambda: del_win(
        root,
        window_pos,
        window_selected.get()))
    del_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    select_btn = tk.Button(root, text='select', command=lambda: select_win(
        root,
        window_pos,
        window_selected.get()))
    select_btn.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1
    
    select_log_dir = tk.Button(root, text='log', command=lambda: select_log_path(root))
    select_log_dir.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    select_history_dir = tk.Button(root, text='histo', command=lambda: select_history_path(root))
    select_history_dir.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    n_y += 1

    print_dir = tk.Button(root, text='print', command=lambda: extract_info(
        tournament_id='',
        log_path=LOG_PATH,
        history_path=HISTORY_PATH))
    print_dir.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)

def print_dire():
    print(LOG_PATH)

def select_log_path(root):
    global LOG_PATH
    LOG_PATH = filedialog.askdirectory()
    history_path_label = tk.Label(root, text=LOG_PATH)
    history_path_label.place(x=400, y=0)

def select_history_path(root):
    global HISTORY_PATH
    HISTORY_PATH = filedialog.askdirectory()
    history_path_label = tk.Label(root, text=HISTORY_PATH)
    history_path_label.place(x=400, y=25)

def add_win(root, window_pos, window_selected):
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
    win_btn = tk.Radiobutton(root, text=str(i), variable=window_selected, value=i)
    win_btn.grid(row=0, column=4+i)
    window_pos.append((win_btn, i, id, 0))
    
def del_win(root, window_pos, window_selected):
    for i, win in enumerate(window_pos):
        if win[1] == window_selected:
            win[0].grid_forget()
            window_pos.pop(i)

def select_win(root, window_pos, window_selected):

    win = next((w for w in window_pos if w[1] == window_selected), ('null', -1, 0))
    table_id_label = tk.Label(root, text=win[2])
    table_id_label.place(x=440, y=42)
    image = Image.open('screen.png')
    ratio = max(image.size[0] / 280, image.size[1] / 280)
    image = image.resize((int(image.size[0] / ratio), int(image.size[1] / ratio)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    img_label = tk.Label(root, image=img)
    img_label.image=img
    img_label.place(x=440, y=62)

    table_data = Table_data()
    table_data.pot = 30.2
    table_data.hand_1 = (3, 2)
    set_forms(root, table_data)

def send(root, table_nb_player=None, position=None, nb_player=None, round=None, stack=None, pot=None, call=None, hand_v1=None, hand_s1=None, hand_v2=None, hand_s2=None, card_v1=None, card_s1=None, card_v2=None, card_s2=None, card_v3=None, card_s3=None, card_v4=None, card_s4=None, card_v5=None, card_s5=None):
    openai.api_key = OPENAI_KEY

    board = ''
    if round=='Flop' or round=='Turn' or round=='River':
        board += f'the Flop is {card_v1} of {card_s1}, {card_v2} of {card_s2} and {card_v3} of {card_s3}'
        if round=='Turn' or round=='River':
            board += f', the river is {card_v4} of {card_s4}'
            if round=='River':
                board += f', the turn is {card_v5} of {card_s5}'

    msg = f"""
    In a poker texas holdem tournament,
    there is {table_nb_player} players on the table,
    you are on {position} position,
    there is {nb_player} players in
    you are at {round} round,
    you have {str(stack)} big blinds left,
    the pot size is {str(pot)} big blinds,
    the minimum to call is {str(call)} big blinds,
    your hand is {hand_v1} of {hand_s1} and {hand_v2} of {hand_s2}
    {board}
    what is the best move to do ?
    answer with only bet, raise, re-raise, check, fold, call, and amout
    next explain your move
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response['choices'][0]['text']

    text = ''
    line = ''
    words = answer.split()
    for word in words:
        if len(line + word) < 40:
            line += word + ' '
        else:
            text += '\n'+line
            line = word + ' '
    text += '\n'+line
    answer_label = tk.Text(root, width=42, height= 20)
    answer_label.insert(tk.INSERT, text)
    answer_label.place(x=370, y=360)

def app():
    root = tk.Tk()
    root.title('Poker OpenAI')
    
    root.geometry('730x720')
    table_data = Table_data()
    menu = tk.Menu(root)
    root.config(menu=menu)
    set_menu(root, menu)
    set_forms(root, table_data)
    set_detection(root)
    root.mainloop()

if __name__ == '__main__':
    app()


