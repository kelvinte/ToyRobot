from core.UserInputProcessor import UserInputProcessor


class StdinUserInputProcessor(UserInputProcessor):

    def __get_from_stdin(self):
        contents = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)
        return contents

    def get_input(self):
        return self.__get_from_stdin()

