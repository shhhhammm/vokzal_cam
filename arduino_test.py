import serial
import time
def connect(com): # after using use time.sleep(2);
    return serial.Serial(com, 9600)

def send_to_board(board, mode,pin,  value=0):
    s = f"${mode} {pin} {value};"
    print(s)
    board.write(s.encode())

def set_pin(board, pin):
    send_to_board(board, 1, pin)

def digitalWrite(board, pin, value):
    send_to_board(board, 2, pin,  value)
