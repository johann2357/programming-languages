
class same(object):
    """
           y  y  y
        x [1, 3, 1]
        x [1, 3, 1]
        x [1, 3, 1]
    """
    position = [(0, 1), (2, 1), (1, 2), (1, 0)]
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

    def is_clickable(self, x, y):
        """
            Return if we can click that coordinate
        """
        return

    def click(self, x, y):
        # Jeffrey
        pass

    def normalize(self):
        """
            Return board in tuples
        """
        # Johan
        pass

    def is_done(self):
        for row in self.data:
            for elem in row:
                if not elem == 0:
                    return False
        return True

    def next_click(self, x, y):
        """
            Return the next click coordinate if is_Possible
            otherwise None
        """

    def solve(self, path, x, y):
        """
            path = [((x, y), tuple(map(tuple, self.data)))
        """
        if self.is_done():
            print 'solve'
            return


