class parser:
    def __init__(self, notfoundmsg):
        self.commands = []
        self.notfoundmsg = notfoundmsg

    def check(self, args):
        string = args[0]
        args = args.pop(0)
        for command in self.commands:
                for name in command[0]:
                    if name == string:
                        command[1](args)
                        return
        self.notFound()

    def add(self, names, func):
        self.commands.append((names, func))

    def remove(self, name):
        try:
            self.commands.remove(name)
        except ValueError:
            self.notFound()

    def notFound(self):
        print(self.notfoundmsg)

    def list(self):
        for command in self.commands:
            names = ''
            for name in self.commands[0]:
                names += name
                if not name == command[0][-1]:
                    names += ', '
            cmdname = str(command[1].__name__)
            print(str(names) + ': ' + cmdname + '()')
