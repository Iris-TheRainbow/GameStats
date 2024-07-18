class manPage():
    def __init__(self, name, short, alt):
        self.name = name
        self.short = short
        self.alt = alt

class manual:
    @staticmethod
    def single(name):
        find = manPage('find', 'Searches through all your libraries for games names containg the string', 'All strings are assessed as lowercase, so no case snesitve searching will work')

        commands = [find, ]
        for command in commands:
            if command.name == name:
                print(command.name + ': ')
                print(command.short)
                print(command.alt)
