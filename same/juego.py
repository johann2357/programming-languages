class SameGame(object):

    """
           y  y  y
        x [1, 3, 1]
        x [1, 3, 1]
        x [1, 3, 1]
    """

    SOLVED = False
    SPREAD = ((-1, 0), (0, 1), (1, 0), (0, -1))
    DATA = (
        (2, 1, 3, 1),
        (2, 2, 2, 3),
        (2, 3, 3, 1),
    )
    EMPTY = 0

    def __init__(self, *args, **kwargs):
        file_ = kwargs.pop('file_name', None)
        if file_ is not None:
            self.load_file(file_)

    def load_file(self, file_):
        self.DATA = []
        with open(file_) as board:
            for line in board:
                self.DATA.append(tuple(line.split()))
        self.DATA = tuple(self.DATA)

    def print_board(self, board=None):
        if board is None:
            board = self.DATA
        for row in board:
            for element in row:
                print element, ' ',
            print

    def print_path(self, path):
        print "==== BOARD ===="
        self.print_board(self.DATA)
        print "\n==== SOLUTION ===="
        for position,  board in path:
            print
            print position[0], position[1]
            print
            self.print_board(board)

    def is_clickable(self, x, y, board):
        """
            Return if we can click that coordinate
        """
        if board[x][y] == self.EMPTY:
            return False
        for offset_x, offset_y in self.SPREAD:
            try:
                if board[x + offset_x][y + offset_y] == board[x][y]:
                    return True
            except IndexError:
                pass
        return False

    def make_editable(self, board):
        return map(list, list(board))

    def save_board(self, board):
        return tuple(map(tuple, board))

    def click(self, x, y, board):
        core = board[x][y]
        board = self.make_editable(board)
        self.click_(x, y, board, core)
        return self.save_board(self.normalize(board))

    def click_(self, x, y, board, core):
        if x < 0 or y < 0:
            return
        elif board[x][y] == core:
            board[x][y] = self.EMPTY
        for offset_x, offset_y in self.SPREAD:
            new_x = offset_x + x
            new_y = offset_y + y
            try:
                if board[new_x][new_y] == core:
                    self.click_(new_x, new_y, board, core)
            except IndexError:
                return

    def normalize(self, board):
        """
            Return board in tuples
        """
        self.normalize_columns(board)
        return board

    def normalize_columns(self, board, done=0):
        for y in xrange(len(board[0]) - done):
            empty_col = True
            col_as_list = []
            for x in xrange(len(board)):
                if board[x][y] != self.EMPTY:
                    empty_col = False
                col_as_list.append(board[x][y])
            if empty_col:
                self.drop_empty_col(board, y)
                self.normalize_columns(board, done + 1)
            else:
                self.drop_col(board, y, col_as_list)

    def drop_empty_col(self, board, idx):
        for x in xrange(len(board)):
            del board[x][idx]
            board[x].append(self.EMPTY)

    def drop_col(self, board, idx_col, col_as_list):
        new_col = [self.EMPTY] * col_as_list.count(self.EMPTY) + \
                  [x for x in col_as_list if x != self.EMPTY]
        if new_col != col_as_list:
            for x in xrange(len(board)):
                board[x][idx_col] = new_col[x]

    def is_done(self, board):
        for row in board:
            for elem in row:
                if not elem == 0:
                    return False
        return True

    def next_click(self, x, y, board):
        """
            Return the next click coordinate if is_Possible
        """
        if self.SOLVED:
            yield (None, None)
        for i in xrange(x, len(board)):
            for j in xrange(y, len(board[i])):
                if self.is_clickable(i, j, board):
                    yield (i, j)

    def solve(self):
        x = 0
        y = 0
        self.solve_(
            x=x,
            y=y,
            board=self.DATA,
            path=[],
        )

    def solve_(self, x, y, board, path):
        """
            path = [((x, y), board), ((x, y), board), ... ]
        """
        if self.SOLVED:
            return
        if self.is_done(board):
            self.print_path(path)
            self.SOLVED = True
            return
        for new_x, new_y in self.next_click(x, y, board):
            if new_x is None or new_y is None:
                return
            new_board = self.click(new_x, new_y, board)
            self.solve_(
                x=0, y=0,
                board=new_board,
                path=path + [((new_x, new_y), new_board)]
            )


def main():
    s = raw_input('Enter the file location: ')
    x = SameGame(file_name=s)
    x.solve()

if __name__ == "__main__":
    main()
