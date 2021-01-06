from . import create_sequence


class Executor:
    def __init__(self):
        self.__sequence = []

    def run(self):
        while True:
            res = self.run_once()
            if not res:
                break

    def run_once(self):
        command = input()
        sequence = []
        if command.startswith("Create Sequence "):
            return self.__handle_create(command)

        elif command.startswith("Locate "):
            return self.__handle_locate(command)

        elif command == "Stop":
            return self.__handle_stop(command)
        return True

    def __handle_create(self, command):
        number = int(command.split()[-1])
        self.__sequence = create_sequence(number)
        print(' '.join(str(i) for i in self.__sequence))
        return True

    def __handle_locate(self, command):
        search_number = int(command.split()[-1])
        try:
            pos = self.__sequence.index(search_number)
            print(f"The number - {search_number} is at index {pos}")
        except ValueError:
            print(f"The number {search_number} is not in the sequence")
        return True

    def __handle_stop(self, command):
        return False