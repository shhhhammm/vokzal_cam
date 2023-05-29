import pyfirmata2
import settings


def connect():
    port = pyfirmata2.Arduino.AUTODETECT
    board = pyfirmata2.Arduino(port)
    return board


def digitalWrite(board, value):
    board.digital[settings.PIN].write(value)

