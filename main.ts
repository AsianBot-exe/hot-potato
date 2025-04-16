//  timer = 0
//  def on_button_pressed_a():
//      basic.show_icon(IconNames.CHESSBOARD)
//      basic.pause(1000 * randint(5, 15))
//      basic.show_icon(IconNames.SKULL)
//  input.on_button_pressed(Button.A, on_button_pressed_a)
//  -1 is false
//  1 is true
//  this is so that the radio is able to brodcast booleans
let lobby_id = 1000
let microbit_id = 0
let init_player_with_potato = 0
let player_0_has_potato = -1
let player_1_has_potato = -1
let player_2_has_potato = -1
let player_3_has_potato = -1
let game_started = -1
radio.setGroup(lobby_id)
function on_button_pressed_b() {
    pass_potato()
}

function pass_potato() {
    
    if (microbit_id == 0 && player_0_has_potato) {
        radio.sendValue("player_0_has_potato", -1)
        radio.sendValue("player_1_has_potato", 1)
    } else if (microbit_id == 1 && player_1_has_potato) {
        radio.sendValue("player_1_has_potato", -1)
        radio.sendValue("player_2_has_potato", 1)
    } else if (microbit_id == 2 && player_2_has_potato) {
        radio.sendValue("player_2_has_potato", -1)
        radio.sendValue("player_3_has_potato", 1)
    } else if (microbit_id == 3 && player_3_has_potato) {
        radio.sendValue("player_3_has_potato", -1)
        radio.sendValue("player_0_has_potato", 1)
    }
    
}

function assign_initial_potato() {
    
    init_player_with_potato = randint(0, 3)
    if (init_player_with_potato == 0) {
        radio.sendValue("player_0_has_potato", 1)
    } else if (init_player_with_potato == 1) {
        radio.sendValue("player_1_has_potato", 1)
    } else if (init_player_with_potato == 2) {
        radio.sendValue("player_2_has_potato", 1)
    } else {
        radio.sendValue("player_3_has_potato", 1)
    }
    
}

function main() {
    
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    assign_initial_potato()
    console.log(init_player_with_potato)
})
console.log("started")
main()
