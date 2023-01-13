import os
import tkinter as tk
from dotenv import load_dotenv
from tkinter import ttk
import openai

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
ANSWER = ''

def forms(root):

    table_nbplayer_label = tk.Label(root, text='players on table')
    table_nbplayer_label.grid(row=0, column=0, padx=10, pady=10)
    table_nbplayer_options = [2,3,4,5,6,7,8,9]
    table_nbplayer_drop = ttk.Combobox(root, value=table_nbplayer_options, width=10)
    table_nbplayer_drop.current(0)
    table_nbplayer_drop.grid(row=0, column=1, padx=10, pady=10)

    position_label = tk.Label(root, text='position')
    position_label.grid(row=1, column=0, padx=10, pady=10)
    position_options = ['SB','BB','BTN','UTG','UTG+1','UTG+2','UTG+3','UTG+4','UTG+5']
    position_drop = ttk.Combobox(root, value=position_options, width=10)
    position_drop.current(0)
    position_drop.grid(row=1, column=1, padx=10, pady=10)

    nb_player_in_label = tk.Label(root, text='players in')
    nb_player_in_label.grid(row=2, column=0, padx=10, pady=10)
    nb_player_in_options = [0,1,2,3,4,5,6,7,8,9]
    nb_player_in_drop = ttk.Combobox(root, value=nb_player_in_options, width=10)
    nb_player_in_drop.current(0)
    nb_player_in_drop.grid(row=2, column=1, padx=10, pady=10)

    round_label = tk.Label(root, text='round')
    round_label.grid(row=3, column=0, padx=10, pady=10)
    round_options = ['Pre-Flop','Flop','Turn','River']
    round_drop = ttk.Combobox(root, value=round_options, width=10)
    round_drop.current(0)
    round_drop.grid(row=3, column=1, padx=10, pady=10)

    stack_label = tk.Label(root, text='stack')
    stack_label.grid(row=4, column=0, padx=10, pady=10)
    stack_val = tk.DoubleVar(value=0)
    stack = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, length=200, variable=stack_val)
    stack.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
    stack_input = ttk.Entry(root, textvariable=stack_val, width=6)
    stack_input.grid(row=4, column=4)

    pot_label = tk.Label(root, text='pot size')
    pot_label.grid(row=5, column=0, padx=10, pady=10)
    pot_val = tk.DoubleVar(value=0)
    pot = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, length=200, variable=pot_val)
    pot.grid(row=5, column=1, padx=10, pady=10, columnspan=2)
    pot_input = ttk.Entry(root, textvariable=pot_val, width=6)
    pot_input.grid(row=5, column=4)

    call_label = tk.Label(root, text='min to call')
    call_label.grid(row=6, column=0, padx=10, pady=10)
    call_val = tk.DoubleVar(value=0)
    call = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, length=200, variable=call_val)
    call.grid(row=6, column=1, padx=10, pady=10, columnspan=2)
    call_input = ttk.Entry(root, textvariable=call_val, width=6)
    call_input.grid(row=6, column=4)

    card_value_options = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    card_symbol_options = ['clubs','diamonds','hearts','spades']

    hand1_label = tk.Label(root, text='hand1')
    hand1_label.grid(row=7, column=0, padx=10, pady=10)
    hand_v1_drop = ttk.Combobox(root, value=card_value_options, width=10)
    hand_v1_drop.grid(row=7, column=1, padx=10, pady=10)
    hand_s1_drop = ttk.Combobox(root, value=card_symbol_options, width=10)
    hand_s1_drop.grid(row=7, column=2, padx=10, pady=10)
    
    hand2_label = tk.Label(root, text='hand2')
    hand2_label.grid(row=8, column=0, padx=10, pady=10)
    hand_v2_drop = ttk.Combobox(root, value=card_value_options, width=10)
    hand_v2_drop.grid(row=8, column=1, padx=10, pady=10)
    hand_s2_drop = ttk.Combobox(root, value=card_symbol_options, width=10)
    hand_s2_drop.grid(row=8, column=2, padx=10, pady=10)

    card1_label = tk.Label(root, text='card1')
    card1_label.grid(row=9, column=0, padx=10, pady=10)
    card_v1_drop = ttk.Combobox(root, value=card_value_options, width=10)
    card_v1_drop.grid(row=9, column=1, padx=10, pady=10)
    card_s1_drop = ttk.Combobox(root, value=card_symbol_options, width=10)
    card_s1_drop.grid(row=9, column=2, padx=10, pady=10)

    card2_label = tk.Label(root, text='card2')
    card2_label.grid(row=10, column=0, padx=10, pady=10)
    card_v2_drop = ttk.Combobox(root, value=card_value_options, width=10)
    card_v2_drop.grid(row=10, column=1, padx=10, pady=10)
    card_s2_drop = ttk.Combobox(root, value=card_symbol_options, width=10)
    card_s2_drop.grid(row=10, column=2, padx=10, pady=10)

    card3_label = tk.Label(root, text='card3')
    card3_label.grid(row=11, column=0, padx=10, pady=10)
    card_v3_drop = ttk.Combobox(root, value=card_value_options, width=10)
    card_v3_drop.grid(row=11, column=1, padx=10, pady=10)
    card_s3_drop = ttk.Combobox(root, value=card_symbol_options, width=10)
    card_s3_drop.grid(row=11, column=2, padx=10, pady=10)

    card4_label = tk.Label(root, text='card4')
    card4_label.grid(row=12, column=0, padx=10, pady=10)
    card_v4_drop = ttk.Combobox(root, value=card_value_options, width=10)
    card_v4_drop.grid(row=12, column=1, padx=10, pady=10)
    card_s4_drop = ttk.Combobox(root, value=card_symbol_options, width=10)
    card_s4_drop.grid(row=12, column=2, padx=10, pady=10)

    card5_label = tk.Label(root, text='card5')
    card5_label.grid(row=13, column=0, padx=10, pady=10)
    card_v5_drop = ttk.Combobox(root, value=card_value_options, width=10)
    card_v5_drop.grid(row=13, column=1, padx=10, pady=10)
    card_s5_drop = ttk.Combobox(root, value=card_symbol_options, width=10)
    card_s5_drop.grid(row=13, column=2, padx=10, pady=10)

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
    send_btn.grid(row=14, column=1, sticky='NESW')

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
    answer with only bet, raise, re-raise, check, fold, call, and amout,
    next explain your move
    """

    print(msg)
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

    answer_label = tk.Text(root, width=60, height= 10)
    answer_label.insert(tk.INSERT, answer)
    answer_label.grid(row=15, column=0, padx=10, columnspan=5, rowspan=2)

def app():
    root = tk.Tk()
    root.title('Poker OpenAI')
    root.geometry('550x800')
    ANSWER = tk.StringVar('')
    forms(root)
    while True:
        root.mainloop()

if __name__ == '__main__':
    app()


