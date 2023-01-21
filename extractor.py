import os
import glob
import re
import openai

openai.api_key = "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"
WINA_LOG_FOLDER = "/mnt/c/Users/YaminLEGZOULI/AppData/Roaming/winamax/logs"

hand_pattern = re.compile(r'hand (\S+)')
action_pattern = re.compile(r'action (\S+) login="(\S+)" amount="(\S+)"')
cards_pattern = re.compile(r'cards login="(\S+)" (\S+)')
round_pattern = re.compile(r'round (\S+) (\S+)')

def extract_info_from_logfile(log_file):
    hands = []
    with open(log_file, 'r') as f:
        for line in f:
            hand_match = hand_pattern.search(line)
            if hand_match:
                hands = []
                hands.append(hand_match.group(0))
            action_match = action_pattern.search(line)
            if action_match:
                hands.append(action_match.group(0))
            cards_match = cards_pattern.search(line)
            if cards_match:
                hands.append(cards_match.group(0))
            round_match = round_pattern.search(line)
            if round_match:
                hands.append(round_match.group(0))
    return hands


def extract_current_hands():
    dir_path = WINA_LOG_FOLDER 
    list_of_files = glob.glob(dir_path + '/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    # latest_file = dir_path + "/1673740996.log"

    hands = extract_info_from_logfile(latest_file)
    
    return hands


def get_response(msg = None):
    hands = extract_current_hands()
    hands_txt = "\n".join(hands)

    if msg is None:
        msg = f"""
We going to play a poker tournament, 6player players, winner take all
I am player YL_ML_GL_42

Here is a list of action wich describe the poker hand

{hands_txt}

first I want you to give me an evaluation of my hand
I want you to give me my position (BTN, UTG, etc..)


Using this information, I want you to give me the best move you think I should do using your poker theorie knowledge
I wan't you to answer with only [bet, raise, re-raise, check fold, call, amout] then explain your move
I want you to always put in your answer: [Action, value] for exemple [raise, 4] or [fold]
        """

        print(hands_txt, "\n#########################################\n")

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

    print(answer)


# msg = """
# Do you now poker theorie ?

# here is some informations about poker theorie I want you to remember

# Manage your chip stack effectively: Your chip stack is your lifeline in a tournament, so it's important to manage it well. This means avoiding big losses, protecting your stack when necessary, and making the most of opportunities to build it.

# Pay attention to the blinds and antes: The blinds and antes increase over time, so it's important to be aware of their level and how they impact your stack. You'll need to adjust your strategy accordingly as the tournament progresses.

# Play tight early on: In the early stages of a tournament, it's best to play tight and only enter pots with strong hands. This will help you build your stack and avoid costly mistakes.

# Be aggressive when necessary: As the tournament progresses and the blinds increase, you'll need to become more aggressive in order to build your stack and put pressure on your opponents.

# Be aware of the players around you: Knowing the playing styles of your opponents can give you an edge in a tournament. Pay attention to how they play and adjust your strategy accordingly.

# Have a plan for the final table: Having a plan for the final table can make all the difference in a tournament. Think about your chip stack, the playing styles of your opponents, and the size of the blinds.

# Stay focused and disciplined: Tournaments can be long and grueling, so it's important to stay focused and disciplined throughout. Avoid distractions and stay in the game mentally.

# """

# response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=msg,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )

# print(response['choices'][0]['text'])

msg = """
We're going to start a game of poker
expresso:
    - 3 player
    - start: 500
    - winner take all

I'm going to give you some hand.


first I want you to give me an evaluation of my hand
I want you to give me my position (BTN, UTG, etc..)


Using this information, I want you to give me the best move you think I should do using your poker theorie knowledge
I wan't you to answer with only [bet, raise, re-raise, check fold, call, amout] then explain your move
I want you to always put in your answer: [Action, value]

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

print(response['choices'][0]['text'])

while 1:
    print("\nINPUT: ")
    test = input()
    if test == "":
        get_response()
    else:
        get_response(test)



# for test in hands:
#     print(test)
