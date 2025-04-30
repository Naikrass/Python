class User:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def print_first_name(self):
        print(self.first)

    def print_last_name(self):
        print(self.last)

    def print_last_and_first_name(self):
        print(self.first, self.last)
