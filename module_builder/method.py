from .find_type import FindType


class Method:

    def __init__(self, new_name, new_return, new_input):
        self.name = new_name.replace("()", "").replace(" ", "")
        self.input = new_input.replace("()", "")
        self.return_type = self.get_return(new_return)

    def get_return(self, new_return):
        if new_return:
            return FindType.find_type(new_return)
        else:
            return "pass"

    def __str__(self):
        if self.input != "":
            return f"    def {self.name}" \
                f"(self, {self.input}) ->{self.return_type}:\n " \
                f"       # ToDo\n        pass\n\n"
        else:
            return f"    def {self.name}" \
                f"(self) ->{self.return_type}:\n        " \
                f"# ToDo\n        pass\n\n"
