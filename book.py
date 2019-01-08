class Book(object):
    def __init__(self):
        self.name = "Default Name"
        print("Init Book")
    def print_name(self):
        print(self.name)