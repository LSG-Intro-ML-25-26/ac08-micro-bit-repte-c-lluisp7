mi_numero = 0
radio.set_group(1)

def on_button_pressed_a():
    radio.send_string("Hola")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global mi_numero
    mi_numero = randint(1, 6)
    basic.show_number(mi_numero)
    basic.pause(1000)
    radio.send_number(mi_numero)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_received_number(receivedNumber):
    basic.clear_screen()
    if receivedNumber > mi_numero:
        basic.show_icon(IconNames.SAD)
    elif receivedNumber < mi_numero:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.CONFUSED)
radio.on_received_number(on_received_number)