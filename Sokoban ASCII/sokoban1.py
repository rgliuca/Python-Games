import msvcrt
import os, sys
from random import randint
from time import sleep
from colorama import Fore, Back, Style, init

board = []
board_width = 16
board_height = 8
numof1s = 0
count = 0
user_row = randint(0, board_height-1)
user_col = randint(0, board_width-1)

top_row = [1] * 8
middle_rows = [0] * 8
bottom_row = top_row

#for the 5th slide, i just need to print the top row and the bottom row in a loop

def print_border(row, col, width, height):
    for i in range(height):
        for x in range(width):
            board.append((Fore.WHITE + '\033[{}{}H'.format(row + i, col + x) + '▓'))
    print(board)

if os.name == "nt":
    os.system("cls")

    import ctypes


    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    a_row = []

    # for i in range(int(board_width/2)):
        # a_row.append(1)
        # a_row.append(0)

    #for row in range(board_height):
        #a_row = []
        #for col in range(board_width):
            #a_row.append(randint(0, 3))
        #board.append(a_row)

    #box_row = randint(0, board_height - 2)
    #box_col = randint(0, board_width - 2)

    #if board[box_row][box_col] == 1:
        #board[box_row][box_col] = 2
    #if board[user_row][user_col] == 1:
        #board[user_row][user_col] = 0

    #for row in range(board_height):
        #print(board[row])

    print_border(5, 10, board_width, board_height)

    #for each_row in board:
        #for i in range(len(board[-1])):
            #if each_row[i] == 1:
                #print(' ', end='')
            #elif each_row[i] == 0:
                #print('Ö', end='')
            #elif each_row[i] == 2:
                #print('▓', end='')
            #else:
                #print('░', end='')
        #print()

# Ö▓░