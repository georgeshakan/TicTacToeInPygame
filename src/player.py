class Player:

    
    def get_action(self,observation):
        '''
        Given an observation, return best action
        '''
        while True:
            x = int(input("Enter the row of your move (0,1,2):"))
            y = int(input("Enter the column of your move (0,1,2):"))
            if (x,y) in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
                if observation.board[x][y] == ' ':
                    return (x,y)
                else:
                    print("Invalid move")
            else:
                print("Please Enter a valid move")