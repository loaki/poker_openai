import tkinter as tk
from tkinter import ttk
import openai

def set_form(root, data):
    form_frame = tk.LabelFrame(root, text='form')

    start_x = 10
    start_y = 0
    pad_x = 100
    pad_y = 25
    n_y = 0

    table_nbplayer_label = tk.Label(form_frame, text='players max')
    table_nbplayer_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    table_nbplayer_options = [2,3,4,5,6,7,8,9]
    table_nbplayer_drop = ttk.Combobox(form_frame, value=table_nbplayer_options, width=10)
    table_nbplayer_drop.current(data.table_nbplayer)
    table_nbplayer_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    position_label = tk.Label(form_frame, text='position')
    position_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    position_drop = ttk.Combobox(form_frame, value=data.position_options, width=10)
    position_drop.current(data.position)
    position_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    nb_player_in_label = tk.Label(form_frame, text='players in')
    nb_player_in_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    nb_player_in_options = [0,1,2,3,4,5,6,7,8,9]
    nb_player_in_drop = ttk.Combobox(form_frame, value=nb_player_in_options, width=10)
    nb_player_in_drop.current(data.nb_player_in)
    nb_player_in_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    round_label = tk.Label(form_frame, text='round')
    round_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    round_drop = ttk.Combobox(form_frame, value=data.round_options, width=10)
    round_drop.current(data.round)
    round_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    n_y+=1

    stack_label = tk.Label(form_frame, text='stack')
    stack_label.place(x=start_x+pad_x*0, y=start_y+pad_y*(n_y))
    stack_val = tk.DoubleVar(value=data.stack)
    stack_input = ttk.Entry(form_frame, textvariable=stack_val, width=6)
    stack_input.place(x=start_x+pad_x*1, y=start_y+pad_y*(n_y))
    stack_max = 100 if data.stack < 100 else (int(data.stack / 100) + 1) * 100
    stack_scale = tk.Scale(form_frame, from_=0, to=stack_max, orient=tk.HORIZONTAL, length=100, variable=stack_val, showvalue=0)
    stack_scale.place(x=start_x+pad_x*1+50, y=start_y+pad_y*n_y)
    n_y+=1

    pot_label = tk.Label(form_frame, text='pot size')
    pot_label.place(x=start_x+pad_x*0, y=start_y+pad_y*(n_y))
    pot_val = tk.DoubleVar(value=data.pot)
    pot_input = ttk.Entry(form_frame, textvariable=pot_val, width=6)
    pot_input.place(x=start_x+pad_x*1, y=start_y+pad_y*(n_y))
    pot_max = 100 if data.pot < 100 else (int(data.pot / 100) + 1) * 100
    pot_scale = tk.Scale(form_frame, from_=0, to=pot_max, orient=tk.HORIZONTAL, length=100, variable=pot_val, showvalue=0)
    pot_scale.place(x=start_x+pad_x*1+50, y=start_y+pad_y*n_y)
    n_y+=1

    call_label = tk.Label(form_frame, text='min to call')
    call_label.place(x=start_x+pad_x*0, y=start_y+pad_y*(n_y))
    call_val = tk.DoubleVar(value=data.call)
    call_input = ttk.Entry(form_frame, textvariable=call_val, width=6)
    call_input.place(x=start_x+pad_x*1, y=start_y+pad_y*(n_y))
    call_max = 100 if data.call < 100 else (int(data.call / 100) + 1) * 100
    call_scall = tk.Scale(form_frame, from_=0, to=call_max, orient=tk.HORIZONTAL, length=100, variable=call_val, showvalue=0)
    call_scall.place(x=start_x+pad_x*1+50, y=start_y+pad_y*n_y)
    n_y+=1

    hand1_label = tk.Label(form_frame, text='hand1')
    hand1_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    hand_v1_drop = ttk.Combobox(form_frame, value=data.card_value_options, width=8)
    if data.hand_1[0] != -1:
        hand_v1_drop.current(data.hand_1[0])
    hand_v1_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    hand_s1_drop = ttk.Combobox(form_frame, value=data.card_symbol_options, width=8)
    if data.hand_1[1] != -1:
        hand_s1_drop.current(data.hand_1[1])
    hand_s1_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1
    
    hand2_label = tk.Label(form_frame, text='hand2')
    hand2_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    hand_v2_drop = ttk.Combobox(form_frame, value=data.card_value_options, width=8)
    if data.hand_2[0] != -1:
        hand_v2_drop.current(data.hand_2[0])
    hand_v2_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    hand_s2_drop = ttk.Combobox(form_frame, value=data.card_symbol_options, width=8)
    if data.hand_2[1] != -1:
        hand_s2_drop.current(data.hand_2[1])
    hand_s2_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card1_label = tk.Label(form_frame, text='card1')
    card1_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v1_drop = ttk.Combobox(form_frame, value=data.card_value_options, width=8)
    if data.board_1[0] != -1:
        card_v1_drop.current(data.board_1[0])
    card_v1_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s1_drop = ttk.Combobox(form_frame, value=data.card_symbol_options, width=8)
    if data.board_1[1] != -1:
        card_s1_drop.current(data.board_1[1])
    card_s1_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card2_label = tk.Label(form_frame, text='card2')
    card2_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v2_drop = ttk.Combobox(form_frame, value=data.card_value_options, width=8)
    if data.board_2[0] != -1:
        card_v2_drop.current(data.board_2[0])
    card_v2_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s2_drop = ttk.Combobox(form_frame, value=data.card_symbol_options, width=8)
    if data.board_2[1] != -1:
        card_s2_drop.current(data.board_2[1])
    card_s2_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card3_label = tk.Label(form_frame, text='card3')
    card3_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v3_drop = ttk.Combobox(form_frame, value=data.card_value_options, width=8)
    if data.board_3[0] != -1:
        card_v3_drop.current(data.board_3[0])
    card_v3_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s3_drop = ttk.Combobox(form_frame, value=data.card_symbol_options, width=8)
    if data.board_3[1] != -1:
        card_s3_drop.current(data.board_3[1])
    card_s3_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card4_label = tk.Label(form_frame, text='card4')
    card4_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v4_drop = ttk.Combobox(form_frame, value=data.card_value_options, width=8)
    if data.board_4[0] != -1:
        card_v4_drop.current(data.board_4[0])
    card_v4_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s4_drop = ttk.Combobox(form_frame, value=data.card_symbol_options, width=8)
    if data.board_4[1] != -1:
        card_s4_drop.current(data.board_4[1])
    card_s4_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    card5_label = tk.Label(form_frame, text='card5')
    card5_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)
    card_v5_drop = ttk.Combobox(form_frame, value=data.card_value_options, width=8)
    if data.board_5[0] != -1:
        card_v5_drop.current(data.board_5[0])
    card_v5_drop.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y)
    card_s5_drop = ttk.Combobox(form_frame, value=data.card_symbol_options, width=8)
    if data.board_5[1] != -1:
        card_s5_drop.current(data.board_5[1])
    card_s5_drop.place(x=start_x+pad_x*1+80, y=start_y+pad_y*n_y)
    n_y+=1

    send_btn = tk.Button(form_frame, text='send', command=lambda: send(
        form_frame,
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
    send_btn.place(x=start_x+pad_x*1, y=start_y+pad_y*n_y, height=25)
    n_y+=2

    form_frame.place(x=10, y=0, width=pad_x*3, height=start_y+pad_y*n_y)
    n_y+=1

    # answer_label = tk.Text(root, width=42, height= 20)
    # answer_label.insert(tk.INSERT, 'hello')
    # answer_label.place(x=start_x+pad_x*0, y=start_y+pad_y*n_y)


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
