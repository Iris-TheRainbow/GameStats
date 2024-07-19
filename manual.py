import scripts
class manPage():
    def __init__(self, name, short, alt):
        self.name = name
        self.short = short
        self.alt = alt

class manual:
    @staticmethod
    def single(name,):
        find = manPage('find', 'Searches through all your libraries for games names containg the string', 'All strings are assessed as lowercase, so no case snesitve searching will work')
        number = manPage('number', 'Finds the number of games in a given library', 'No argumens will find the number of games in each library. All will combine the number from each library into one list. Any other string will be used to find a library name to search')
        libraries = manPage('Libraries', 'Libraries are lists of your games put in ~/.gamestats/games', 'Libraries are just text list of games, stored in extnsionless files with the name of their launcher')
        help = manPage('help', 'Shows this page', 'Come on, it\'s a help command you dont need help with it')
        commands = [find, number, libraries, help]
        for command in commands:
            if name in command.name:
                print(command.name + ': ')
                print(command.short)
                print(command.alt)

    @staticmethod
    def manual(args):
        string = scripts.argsToString(args)
        manual.single(string)
