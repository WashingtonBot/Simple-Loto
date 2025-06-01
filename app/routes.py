from flask import Flask, request, render_template
import json
from app import app
import sys
sys.path.append(
    "C:\\Users\\azert\\Documents\\GitHub\\Simple-Loto\\src")
from loto import *
from loto import LotoConstants

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

min_value = LotoConstants.MIN_VALUE
max_value = LotoConstants.MAX_VALUE
grid_length = LotoConstants.GRID_LENGTH


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', messages=messages)


# `read-form` endpoint
@app.route('/read-form', methods=['POST'])
def read_form():

    # Get the form data as Python ImmutableDict datatype
    data = request.form
    # Return the extracted information
    user_input_list: list[int] = []
    user_input_list.append(int(data['userNumber_1']))
    user_input_list.append(int(data['userNumber_2']))
    user_input_list.append(int(data['userNumber_3']))
    user_input_list.append(int(data['userNumber_4']))
    user_input_list.append(int(data['userNumber_5']))
    user_input_list.append(int(data['userNumber_6']))


    list_computer = generate_winner_list(min_value, max_value, grid_length)

    num_players = set(user_input_list)
    num_computers = set(list_computer)
    loto_grids_combined = list(set(num_players.intersection(num_computers)))

    player_gains = compute_gains(loto_grids_combined, min_value, grid_length)
    with open("C:\\Users\\azert\\Documents\\GitHub\\Simple-Loto\\src\\wager_details.json", "w", encoding="utf-8") as fp:
        json_wager_infos = {'Your list': tuple(sorted(user_input_list)),
                            'Winning List': tuple(sorted(list_computer)),
                            'Your winning numbers': tuple(loto_grids_combined),
                            'Your gains': f"{player_gains}$",
                            "Amount of numbers you've played": f"{grid_length} numbers"}
        json.dump(json_wager_infos, fp, indent=2)
    with open("C:\\Users\\azert\\Documents\\GitHub\\Simple-Loto\\src\\wager_details.json", "r", encoding="utf-8") as fp:
        data = fp.read()

    return render_template('answer.html', title="page", jsonfile=json.dumps(data))

