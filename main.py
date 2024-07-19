import os
import sys
from scripts import *
from manual import *
from parser import parser

cmdParser = parser('GameStats: command not found')
cmdParser.add(['find'], find)
cmdParser.add(['number', 'num'], number)
cmdParser.add(['help', '-h', '--help'], manual.manual)
cmdParser.add(['version', '-v', '--version'], version)
cmdParser.add(['exit', 'exit()'], close)
cmdParser.add(['libs', 'libraries'], libraries)

args = sys.argv
args.pop(0)

if len(args) == 0:
    print('GameStats: an easy way to look for games')
    while True:
        args = input('> ').split()
        cmdParser.check(args)
else:
    cmdParser.check(args)
