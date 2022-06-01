from board import Board 
from random import randint

class Agent:
    def __init__(self):
        self.values = {}

    def train(self):
        '''
        Train the agent
        '''
        
        self.get_value((" ",)*9)


    def get_value(self,board_tuple):
        '''
        Get the value of a state
        '''

        ##first check i the state is in the values dictionary
        board = self._tuple_to_board(board_tuple)
        if board_tuple in self.values:
            return self.values[board_tuple]
        

        elif board.check_win() is not None:
            self.values[board_tuple] = board.check_win()
            return  board.check_win()
        elif board.num_moves == 9:
            self.values[board_tuple] = "Tie"
            return "Tie"
        else:
            ##get all the possible moves and evaluate them
            checks = []
            for (row,col) in board.legal_moves():
                 board.make_move((row,col))
                 temp = self.get_value(board.convert_board())
                 checks.append((temp, (row,col)))
                 
                 board.del_move((row,col))
                 if temp == board.get_turn():
                     self.values[board_tuple] = board.get_turn() 
                     return board.get_turn()
            for u in checks:
                if u[0] == "Tie":
                    self.values[board_tuple] = "Tie"
                    return "Tie"   
            self.values[board_tuple] = board.last_turn()
            return board.last_turn()         

                        
    def get_action(self,board):
        '''
        Get the action to take
        given a partiular board
        '''
        
        ties = []
        for row,col in board.legal_moves():  
            board.make_move((row,col))
            temp = self.get_value(board.convert_board())
            board.del_move((row,col))
            
            if temp == board.get_turn():
                return (row,col)
            elif temp == board.last_turn():
                pass
            else:
                ties.append((row,col))
        ind = randint(0,len(ties)-1)
        return ties[ind]
        
    

    def _tuple_to_board(self,board_tuple):
        '''
        convert board tuple to board
        '''
        board = Board()
        for row in range(3):
            for col in range(3):
                if board_tuple[3*row + col] != " ":
                    board.board[row][col] = board_tuple[3*row + col]
                    board.num_moves +=1
        return board

if __name__== "__main__":
    agent = Agent()
    agent.train()
