
class same(object):
    data = []

    def load_file(self, file):
        with open(file) as board:
            for line in board:
                self.data.append(line.split())

    def print_board(self):
        for row in self.data:
            for element in row:
                print element, ' ',
            print

    def click(self, x, y):
        # Jeffrey
        pass

    def normalize(self):
        # Johan
        pass

    def group():
        pass