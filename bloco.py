class Bloco:
    def __init__(self):
        self.tag = 'x'
        self.info = '0'
        self.val = 0

    def write(self, tag):
        self.tag = tag
        self.val = 1
