import glob
import time
import os
def getFiles():
    dir = os.path.expanduser('~')
    if not os.path.exists(dir + '/.gamestats'):
        os.mkdir(dir + '/.gamestats')
    if not os.path.exists(dir + '/.gamestats/games'):
        os.mkdir(dir + '/.gamestats/games')
    files = glob.glob(dir + '/.gamestats/games/*')
    if len(files) == 0:
        print('please add library game lists to ~/.gamestats/gmames/')
        exit()
    return files
def find(string):
    files = getFiles()
    list = []
    for file in files:
        with open(file) as f:
            list.append((file, f.read().splitlines()))
    found = []
    result = []
    for library in list:
        games = library[1]
        index = 0
        result = []
        for game in games:
                if string.lower() in game.lower():
                    result.append(game)
        if result == []:
            continue
        print(library[0].split('/')[-1] + ':')
        for i in range(len(result)):
            print(result[i])

def number(string, ret = False):
    if string == 'all':
        ret = True
        string = ''
    files = getFiles()
    libs = []
    for file in files:
        if string in file:
            libs.append(file)
    num = 0
    for lib in libs:
        number = 0
        with open(lib, 'r') as f:
            games = f.read().splitlines()
            number = len(games)
            num += number
            if not ret:
                print('There are ' + str(number) + ' games in ' + lib.split('/')[-1])
    if ret:
        print("There are " + str(num) + ' games total across all libraries')


def numberAll():
    number('')
