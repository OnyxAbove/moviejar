import libmoviejar
import cmd


class Repl(cmd.Cmd):
    filename = None
    intro = " ######    ###  ##   ##  ##  ####          ##    ##   #####\n## ## ## ##  ##  ## ##  ##  ####      ##  ##   ####  #####\n#    ##   ###     ###  ##  ####        ###   ##  ## ## ## \n"
    prompt = "MovieJar >>> "

    def __init__(self, jar: libmoviejar.Jar):
        super().__init__()
        self.jar = jar

    def do_clear(self, arg: str):
        self.jar.clear()

    def do_list(self, arg: str):
        self.jar.list()

    def do_add(self, arg: str):
        self.jar.new()

    def do_pick(self, arg: str):
        print(self.jar.pickrand())

    def do_exit(self, arg: str):
        return True


if __name__ == "__main__":
    jar = libmoviejar.Jar()
    repl = Repl(jar)
    repl.cmdloop()
