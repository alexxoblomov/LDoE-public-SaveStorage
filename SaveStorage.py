import json
import sys
import os
import PySimpleGUI as sg


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_player_json(filename):
    file_path = get_resource_path(filename)
    with open(file_path, mode='rt') as file:
        return json.load(file)


def create_player_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


player_json = load_player_json('new_player.json')


def tutor_ch_1_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_1_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_1_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_1_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_1_quest_3():
    global player_json
    player_json = load_player_json('tutor_ch_1_quest_3.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_2_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_2_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_2_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_2_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_2_quest_4():
    global player_json
    player_json = load_player_json('tutor_ch_2_quest_4.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_2_quest_5():
    global player_json
    player_json = load_player_json('tutor_ch_2_quest_5.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_2_quest_6():
    global player_json
    player_json = load_player_json('tutor_ch_2_quest_6.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_3_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_3_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_3_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_3_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_3_quest_3():
    global player_json
    player_json = load_player_json('tutor_ch_3_quest_3.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_3_quest_4():
    global player_json
    player_json = load_player_json('tutor_ch_3_quest_4.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_3_quest_5():
    global player_json
    player_json = load_player_json('tutor_ch_3_quest_5.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_3_quest_6():
    global player_json
    player_json = load_player_json('tutor_ch_3_quest_6.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_3_quest_7():
    global player_json
    player_json = load_player_json('tutor_ch_3_quest_7.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_3():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_3.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_4():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_4.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_5():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_5.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_6():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_6.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_7():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_7.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_8():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_8.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_9():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_9.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_4_quest_10():
    global player_json
    player_json = load_player_json('tutor_ch_4_quest_10.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_5_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_5_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_5_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_5_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_5_quest_3():
    global player_json
    player_json = load_player_json('tutor_ch_5_quest_3.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_5_quest_4():
    global player_json
    player_json = load_player_json('tutor_ch_5_quest_4.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_5_quest_5():
    global player_json
    player_json = load_player_json('tutor_ch_5_quest_5.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_5_quest_6():
    global player_json
    player_json = load_player_json('tutor_ch_5_quest_6.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_6_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_6_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_6_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_6_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_6_quest_3():
    global player_json
    player_json = load_player_json('tutor_ch_6_quest_3.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_6_quest_4():
    global player_json
    player_json = load_player_json('tutor_ch_6_quest_4.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_6_quest_5():
    global player_json
    player_json = load_player_json('tutor_ch_6_quest_5.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_7_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_7_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_7_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_7_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_7_quest_3():
    global player_json
    player_json = load_player_json('tutor_ch_7_quest_3.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_8_quest_1():
    global player_json
    player_json = load_player_json('tutor_ch_8_quest_1.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_8_quest_2():
    global player_json
    player_json = load_player_json('tutor_ch_8_quest_2.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_8_quest_3():
    global player_json
    player_json = load_player_json('tutor_ch_8_quest_3.json')
    create_player_json(player_json, 'player.json')


def tutor_ch_8_quest_4():
    global player_json
    player_json = load_player_json('tutor_ch_8_quest_4.json')
    create_player_json(player_json, 'player.json')


functions = {
    'tutor_ch_1_quest_1': tutor_ch_1_quest_1,
    'tutor_ch_1_quest_2': tutor_ch_1_quest_2,
    'tutor_ch_1_quest_3': tutor_ch_1_quest_3,
    'tutor_ch_2_quest_1': tutor_ch_2_quest_1,
    'tutor_ch_2_quest_2': tutor_ch_2_quest_2,
    'tutor_ch_2_quest_4': tutor_ch_2_quest_4,
    'tutor_ch_2_quest_5': tutor_ch_2_quest_5,
    'tutor_ch_2_quest_6': tutor_ch_2_quest_6,
    'tutor_ch_3_quest_1': tutor_ch_3_quest_1,
    'tutor_ch_3_quest_2': tutor_ch_3_quest_2,
    'tutor_ch_3_quest_3': tutor_ch_3_quest_3,
    'tutor_ch_3_quest_4': tutor_ch_3_quest_4,
    'tutor_ch_3_quest_5': tutor_ch_3_quest_5,
    'tutor_ch_3_quest_6': tutor_ch_3_quest_6,
    'tutor_ch_3_quest_7': tutor_ch_3_quest_7,
    'tutor_ch_4_quest_1': tutor_ch_4_quest_1,
    'tutor_ch_4_quest_2': tutor_ch_4_quest_2,
    'tutor_ch_4_quest_3': tutor_ch_4_quest_3,
    'tutor_ch_4_quest_4': tutor_ch_4_quest_4,
    'tutor_ch_4_quest_5': tutor_ch_4_quest_5,
    'tutor_ch_4_quest_6': tutor_ch_4_quest_6,
    'tutor_ch_4_quest_7': tutor_ch_4_quest_7,
    'tutor_ch_4_quest_8': tutor_ch_4_quest_8,
    'tutor_ch_4_quest_9': tutor_ch_4_quest_9,
    'tutor_ch_4_quest_10': tutor_ch_4_quest_10,
    'tutor_ch_5_quest_1': tutor_ch_5_quest_1,
    'tutor_ch_5_quest_2': tutor_ch_5_quest_2,
    'tutor_ch_5_quest_3': tutor_ch_5_quest_3,
    'tutor_ch_5_quest_4': tutor_ch_5_quest_4,
    'tutor_ch_5_quest_5': tutor_ch_5_quest_5,
    'tutor_ch_5_quest_6': tutor_ch_5_quest_6,
    'tutor_ch_6_quest_1': tutor_ch_6_quest_1,
    'tutor_ch_6_quest_2': tutor_ch_6_quest_2,
    'tutor_ch_6_quest_3': tutor_ch_6_quest_3,
    'tutor_ch_6_quest_4': tutor_ch_6_quest_4,
    'tutor_ch_6_quest_5': tutor_ch_6_quest_5,
    'tutor_ch_7_quest_1': tutor_ch_7_quest_1,
    'tutor_ch_7_quest_2': tutor_ch_7_quest_2,
    'tutor_ch_7_quest_3': tutor_ch_7_quest_3,
    'tutor_ch_8_quest_1': tutor_ch_8_quest_1,
    'tutor_ch_8_quest_2': tutor_ch_8_quest_2,
    'tutor_ch_8_quest_3': tutor_ch_8_quest_3,
    'tutor_ch_8_quest_4': tutor_ch_8_quest_4,
}

layout = [
    [sg.Text('Select Trophy Road chapter:')],
    [sg.Combo(list(functions.keys()), key='COMBO', enable_events=True)],
    [sg.Button('Execute'), sg.Button('Exit')]
]

window = sg.Window('Save Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Execute':
        selected_function = values['COMBO']
        if selected_function in functions:
            functions[selected_function]()

window.close()
