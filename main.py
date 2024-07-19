import os
import sys
from scripts import *
from manual import *
from parser import parser

cmdParser = parser('GameStats: command not found')
cmdParser.add(['find'], find)
cmdParser.add(['number', 'num'], number)
cmdParser.add(['help', '-h', '--h'], help)
cmdParser.add(['version', '-v', '--v'], version)
cmdParser.add(['exit', 'exit()'])
def process():
    if not len(sys.argv) > 1:
        command = input('> ').split()
    else:
        command = sys.argv
        command.pop(0)
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
    elif command[0] == 'exit' or command[0] == 'exit()':
        exit()
    elif command[0] == 'libraries':
        libraries()
    else:
        string = ''
        for i in range(len(command)):
            string += command[i]
            if i+1 != len(command):
                string += ' '
        print('Gamestats: Command not found: ' + string)

if not len(sys.argv) > 1:
    while True:
        process()
else:
    process()
