from board import Board 
from player import Player
from agent import Agent 

##A class to run cmd line tic tac toe
class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        
    def restart(self):
        self.board = Board()
        self.run()

    def run(self):
        print(self.board)
        while True:
            self.step()
            
    def step(self):
        if self.board.num_moves % 2 == 0:
            self.play_turn(self.player1)
        else:
            self.play_turn(self.player2)
        
    def play_turn(self,player):

        action = player.get_action(self.board)
        
        u,v = action
        self.board.make_move((u,v))
        print(self.board)
        
        if self.board.check_win():
            print(f"Player {1 + (self.board.num_moves % 2)} wins!")
            self.restart()
        if self.board.num_moves == 9:
            print("Draw!")
            self.restart()
    
if __name__ == "__main__":
    '''
    Used to play tic tac toe 
    with the terminal
    '''
    player1 = Player()
    player2 = Agent()
    player2.train()
    game = Game(player1,player2)
    game.run()