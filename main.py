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
