radio.onReceivedNumber(function (receivedNumber) {
    basic.clearScreen()
    if (receivedNumber > mi_numero) {
        basic.showIcon(IconNames.Sad)
    } else if (receivedNumber < mi_numero) {
        basic.showIcon(IconNames.Heart)
    } else {
        basic.showIcon(IconNames.Confused)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("Hola")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onGesture(Gesture.Shake, function () {
    mi_numero = randint(1, 6)
    basic.showNumber(mi_numero)
    basic.pause(1000)
    radio.sendNumber(mi_numero)
})
let mi_numero = 0
radio.setGroup(1)
