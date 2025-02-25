from typing import override


class Addition :
    def __init__(self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c
    
    def add(self):
            return self.a + self.b 
    @override
    def add(self):
            return self.a + self.b + self.c
