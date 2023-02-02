from extractor.extractor import Log_data

class Table_data():
    def __init__(self):
        self.table_nbplayer=-1
        self.position=-1
        self.nb_player_in=-1
        self.round=-1
        self.stack=0
        self.pot=0
        self.call=0
        self.hand_1=(-1, -1)
        self.hand_2=(-1, -1)
        self.board_1=(-1, -1)
        self.board_2=(-1, -1)
        self.board_3=(-1, -1)
        self.board_4=(-1, -1)
        self.board_5=(-1, -1)
        self.players_options = ['0','1','2','3','4','5','6','7','8','9']
        self.position_options = ['SB','BB','BTN','UTG','UTG+1','UTG+2','UTG+3','UTG+4','UTG+5']
        self.round_options = ['Pre-Flop','Flop','Turn','River']
        self.card_value_options = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        self.card_symbol_options = ['clubs','diamonds','hearts','spades']

def format_table_data(data):
    table_data = Table_data()
    table_data.table_nbplayer = len(data.players)
    if data.login in data.players:
        table_data.position = table_data.position_options.index(data.players[data.login]['position'])
    table_data.nb_player_in = 0
    table_data.round=2
    table_data.stack=120
    table_data.pot=34.5
    table_data.call=10
    table_data.hand_1=(3, 1)
    table_data.hand_2=(1, 0)
    return table_data

    