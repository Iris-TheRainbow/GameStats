import os
from scripts import *

print('GameStats: easily search your games')
while True:
    command = input('> ').split()
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
    else:
        string = ''
        for i in range(len(command)):
            string += command[i]
            if i+1 != len(command):
                string += ' '
        print('Gamestats: Command not found: ' + string)
