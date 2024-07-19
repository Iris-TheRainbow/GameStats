import os
import sys
from scripts import *
from manual import *
from parser import parser

cmdParser = parser('GameStats: command not found')
cmdParser.add(['find'], find)
cmdParser.add(['number', 'num'], number)
cmdParser.add(['help', '-h', '--h'], manual.manual)
cmdParser.add(['version', '-v', '--v'], version)
cmdParser.add(['exit', 'exit()'], close)
cmdParser.add(['libs', 'libraries'], libraries)
args = sys.argv
args.pop(0)
print(args)
if len(args) == 0:
    while True:
        args = input('> ').split()
        cmdParser.check(args)
else:
    cmdParser.check(args)
