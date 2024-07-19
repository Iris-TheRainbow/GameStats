import os
import sys
from scripts import *
from manual import *

def process():
    if not len(sys.argv) == 1:
        command = input('> ').split()
    else:
        command = sys.argv
    if command[0] == 'find':
        string = ''
        command.pop(0)
        for i in range(len(command)):
            string += command[i]
            if i+1 != len(command):
                string += ' '
        find(string)
    elif command[0] == 'number':
        if len(command) == 1:
            numberAll()
        else:
            number(command[1])
    elif command[0] == 'help':
        if len(command) == 1:
            manual.all()
        else:
            manual.single(command[1])
    elif command[0] == '-v' or command[0] == '--version' or command[0] == 'version':
            print('GameStats\nVersion: 0.1.1')
    elif command[0] == 'exit':
        exit()
    else:
        string = ''
        for i in range(len(command)):
            string += command[i]
            if i+1 != len(command):
                string += ' '
        print('Gamestats: Command not found: ' + string)

if not len(sys.argv) > 2:
    while True:
        process()
else:
    process()
