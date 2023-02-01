import os
import glob
import sys
import re

HISTORY_PATH='./history/'
LOG_PATH='./logs/'

class Log_data():
    def __init__(self):
        self.tournament = {}
        self.players = {}
        self.actions = []
        self.login = ''
        self.cards = ''
        self.hand_id = ''

def parse_hand(data, line):
    data.hand_id = line.split('hand ')[1]

def parse_action(data, line):
    positions = ['BTN', 'SB', 'BB', 'UTG', 'UTG+1', 'UTG+2', 'UTG+3', 'UTG+4', 'UTG+5']
    data.actions.append('action '+line.split('action ')[1])
    if 'login=' in line:
        login = line.split('login=')[1].split('"')[1]
        if login not in data.players:
            data.players[login] = {}
            if 'SB' in line.split()[6]:
                data.players[login]['position'] = 'SB'
            elif 'BB' in line.split()[6]:
                data.players[login]['position'] = 'BB'
            else:
                data.players[login]['position'] = 'BTN'
                if data.players[list(data.players)[-2]]['position'] == 'BTN':
                    data.players[list(data.players)[-2]]['position'] = positions[positions.index(data.players[list(data.players)[-3]]['position']) + 1]

def parse_cards(data, line):
    data.login = line.split('login=')[1].split('"')[1]
    data.cards = line.split()[7]

def parse_round(data, line):
    data.actions.append('round '+line.split('round ')[1])

def get_hand_info(data, curr_hand, table_id):
    parsing_fcts = {
        'hand' : parse_hand,
        'action' : parse_action,
        'cards' : parse_cards,
        'round' : parse_round
    }
    for line in reversed(curr_hand):
        if re.search(rf'.*inf \[table\].*t{table_id}.*', line):
            if line.split()[5] in parsing_fcts:
                parsing_fcts[line.split()[5]](data, line)

def reverse_readline(filename, buf_size=8192):
    """A generator that returns the lines of a file in reverse order"""
    with open(filename) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        file_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(file_size, offset + buf_size)
            fh.seek(file_size - offset)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split('\n')
            # The first line of the buffer is probably not a complete line so
            # we'll save it and append it to the last line of the next buffer
            # we read
            if segment is not None:
                # If the previous chunk starts right from the beginning of line
                # do not concat the segment to the last line of new chunk.
                # Instead, yield the segment first 
                if buffer[-1] != '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if lines[index]:
                    yield lines[index]
        # Don't yield None if the file was empty
        if segment is not None:
            yield segment

def get_last_table_id(file, tournament_id):
    for line in reverse_readline(file):
        if re.search(rf'.*Execution done: wam://table-open.*\.t{tournament_id}.*', line):
            match = re.search(rf'\.t(\d+)\&.*\.t{tournament_id}', line)
            print(line)
            return match.group(1)
    return None

def get_last_hand(file, tournament_id):
    table_id = get_last_table_id(file, tournament_id)
    if not table_id:
        return None

    curr_hand = []
    for line in reverse_readline(file):
        if re.search(rf'.*inf \[table\].*\.t{table_id} .*', line):
            curr_hand.append(line)

        # hand info completed
        if re.search(rf'.*inf \[table\].*\.t{table_id} hand.*', line):
            return curr_hand, table_id

    print(f'###parsing error\nfile: {file}\ntournament id: {table_id}')
    return None, None

def get_tournaments_id(file, tournament_nb=1):
    tournament_ids = []
    for line in reverse_readline(file):
        # get tournament id in switch case
        if re.search(r'.*inf \[network\].*TOURNAMENT:GET_TABLE_OK', line):
            match = re.search(r"\.t(\d+) ", line)
            if match and match.group(1) not in tournament_ids:
                tournament_ids.append(match.group(1))
        
        # get tournament id
        if re.search(r'.*inf \[router\] .* done: wam://table.*', line):
            match = re.search(r'\.t(\d+).*\.t(\d+)', line)
            if match and match.group(1) not in tournament_ids:
                tournament_ids.append(match.group(1))

        if len(tournament_ids) >= tournament_nb:
            break
    return tournament_ids

def parse_tournament(data, hand):
    bets = ['posts', 'bets', 'calls', 'raises']
    player_bets = {}
    round = 0
    for line in hand:
        if len(line.split()) == 3 and line.split()[0] == '***' and line.split()[2] == '***':
            if round > 1:
                for player in player_bets:
                    data.players[player]['stack'] -= player_bets[player]
            round += 1
        if 'Winamax Poker - ' in line:
            data.tournament['name'] = line.split('Winamax Poker - ')[1].split(' buyIn:')[0]
            data.tournament['level'] = line.split('level: ')[1].split()[0]
            data.tournament['blinds'] = line.split('Holdem no limit (')[1].split(')')[0]
        if len(line.split()) >= 4 and line.split()[0] == 'Seat':
            if line.split()[2] in data.players:
                if line.split()[3].split(')')[0].split(',')[0][1:].isnumeric():
                    data.players[line.split()[2]]['stack'] = int(line.split()[3].split(')')[0].split(',')[0][1:])
        if len(line.split()) >= 3 and line.split()[0] in data.players:
            if line.split()[1] in bets:
                for word in reversed(line.split()):
                    if word.isnumeric():
                        if line.split()[1] == 'raises':
                            player_bets[line.split()[0]] = int(word)
                        else:    
                            player_bets[line.split()[0]] = int(word) + player_bets[line.split()[0]] if line.split()[0] in player_bets else int(word)
                        break
        if len(line.split()) >= 3 and ' and won' in ' '.join(line.split()[3:]):
            data.players[line.split()[2]]['stack'] += int(line.split(' and won ')[1].split()[0])

def get_tournament_info(data, tournament_id, history_path=HISTORY_PATH):
    data.tournament['id'] = tournament_id
    list_files = os.listdir(history_path)
    for file in list_files:
        if tournament_id in file:
            if '_summary' in file:
                pass
            else:
                hand = []
                status = 0
                with open(history_path+file) as f:
                    id = data.hand_id.split('-')[0]+'-'+str(int(data.hand_id.split('-')[1])-1)
                    id_curr = data.hand_id.split('-')[0]+'-'+str(int(data.hand_id.split('-')[1]))
                    for line in f:
                        if id in line:
                            status = 1
                        if status == 1:
                            if id_curr in line:
                                break
                            hand.append(line)
                parse_tournament(data, hand)

def format_info(file, tournament_id='', history_path=HISTORY_PATH):
    data = Log_data()
    if not tournament_id:
        tournament_id = get_tournaments_id(file, 1)
        if not tournament_id:
            return None
        tournament_id = tournament_id[0]
    curr_hand, table_id = get_last_hand(file, tournament_id)
    if curr_hand == None:
        return data
    get_hand_info(data, curr_hand, table_id)
    get_tournament_info(data, tournament_id, history_path)
    return data

def print_data(data):
    print(
        '\n########## tournament ##########\n',data.tournament,
        '\n########## players ##########\n',str(data.players).replace('}, ', '\n'),
        '\n########## actions ##########\n','\n'.join(data.actions),
        '\n########## login ##########\n',data.login,
        '\n########## cards ##########\n',data.cards,
        '\n########## hand_id ##########\n',data.hand_id)

def extract_info(tournament_id='', log_path=LOG_PATH, history_path=HISTORY_PATH):
    print(tournament_id, log_path, history_path)
    last_file = max(glob.iglob(f'{log_path}/*.log'), key=os.path.getmtime)
    if tournament_id:
        list_files = sorted(glob.iglob(f'{log_path}/*.log'), key=os.path.getmtime)
        for file in reversed(list_files):
            with open(file, 'r') as r_file:
                if tournament_id in r_file.read():
                    last_file = file
                    break            
    data = format_info(last_file, tournament_id, history_path)
    if data:
        print_data(data)

if __name__ == '__main__':
    tournament_id = '' if len(sys.argv) == 1 else sys.argv[1]
    extract_info(tournament_id, log_path=LOG_PATH, history_path=HISTORY_PATH)
