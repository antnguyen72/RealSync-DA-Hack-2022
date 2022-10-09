from unicodedata import name


class person(object):
    
    # Constructor
    def __init__(self, name='John Doe', age=18):
        self.name = name
        self.age = age 

test_person = person('Thomas Li',26)