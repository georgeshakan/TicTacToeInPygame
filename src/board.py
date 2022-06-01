class Board:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.num_moves = 0

    def __str__(self):
        '''
        overwrite print(board)
        with a more readable format
        '''
        temp = [
            [self.board[0][0],'|', self.board[0][1],'|', self.board[0][2]],
            ['-','-','-','-','-',],
            [self.board[1][0],'|', self.board[1][1],'|', self.board[1][2]],
            ['-','-','-','-','-',],
            [self.board[2][0],'|', self.board[2][1],'|', self.board[2][2]],
        ]
        return '\n' + '\n'.join([' '.join(row) for row in temp])

    def get_turn(self):
        '''
        Given a tic tac toe board, we 
        can determine whose turn it is
        returns: "X" or "O"
        '''
        marker = "X"
        if self.num_moves % 2 == 1:
            marker = "O"
        return marker
    
    def last_turn(self):
        '''
        Get who last played
        '''
        return "O" if self.get_turn() == "X" else "X"


    def check_win(self):
        '''
        returns: The last player to play
        if board is a win, otherwise returns
        None
        '''
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None



    def make_move(self, position):
        '''
        Make a move on the board,
        given a (row,col) position
        '''
        move = self.get_turn()
        if self.board[position[0]][position[1]] == ' ':
            self.board[position[0]][position[1]] = move
            self.num_moves +=1
        else:
            raise ValueError('Invalid move')
    
    def del_move(self,position):
        '''
        Delete a move on the board
        (useful for training)
        '''
        if self.board[position[0]][position[1]] == ' ':
            raise ValueError('Invalid deletion')
        self.board[position[0]][position[1]] = ' '
        self.num_moves -=1

    def convert_board(self):
        '''
        Convert board to a tuple,
        which can be used during training
        '''
        return tuple([self.board[row][col] for row in range(3) for col in range(3)])

    def legal_moves(self):
        '''
        Get all legal moves
        '''
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    yield (row,col)
    
    def restart(self):
        '''
        reset the board
        '''
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.num_moves = 0
    
