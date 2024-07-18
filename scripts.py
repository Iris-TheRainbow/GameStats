import glob
import time
def find(string):
    files = glob.glob('./games/*')
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
        while index < len(games):
            for i in range(len(games)):
                index = i + 1
                if string.lower() in games[i].lower():
                    result.append(games[i])
        if result == []:
            continue
        print(library[0] + ':')
        for i in range(len(result)):
            print(result[i])
