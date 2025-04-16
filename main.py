# timer = 0
# def on_button_pressed_a():
#     basic.show_icon(IconNames.CHESSBOARD)
#     basic.pause(1000 * randint(5, 15))
#     basic.show_icon(IconNames.SKULL)

# input.on_button_pressed(Button.A, on_button_pressed_a)

# -1 is false
# 1 is true
# this is so that the radio is able to brodcast booleans

lobby_id = 1000
microbit_id = 0

init_player_with_potato = 0
player_0_has_potato = -1
player_1_has_potato = -1
player_2_has_potato = -1
player_3_has_potato = -1

player_0 = player_0_has_potato == 1 and microbit_id == 0
player_1 = player_1_has_potato == 1 and microbit_id == 1
player_2 = player_2_has_potato == 1 and microbit_id == 2
player_3 = player_3_has_potato == 1 and microbit_id == 3

game_started = -1

radio.set_group(lobby_id)

def on_button_pressed_a():
    global game_started, init_player_with_potato
    assign_initial_potato()
    print(init_player_with_potato)

def on_button_pressed_b():
    pass_potato()

def pass_potato():
    global microbit_id, player_0, player_1, player_2, player_3

    if player_0:
        radio.send_value("player_0_has_potato", -1)
        radio.send_value("player_1_has_potato", 1)
    elif player_1:
        radio.send_value("player_1_has_potato", -1)
        radio.send_value("player_2_has_potato", 1)
    elif player_2:
        radio.send_value("player_2_has_potato", -1)
        radio.send_value("player_3_has_potato", 1)
    elif player_3:
        radio.send_value("player_3_has_potato", -1)
        radio.send_value("player_0_has_potato", 1)

def assign_initial_potato():
    global init_player_with_potato
    init_player_with_potato = randint(0, 3)
    if init_player_with_potato == 0:
        radio.send_value("player_0_has_potato", 1)
    elif init_player_with_potato == 1:
        radio.send_value("player_1_has_potato", 1)
    elif init_player_with_potato == 2:
        radio.send_value("player_2_has_potato", 1)
    else:
        radio.send_value("player_3_has_potato", 1)




def main():
    global init_player_with_potato, game_started

input.on_button_pressed(Button.A, on_button_pressed_a)


print("started")
main()