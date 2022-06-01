import pygame 
from board import Board
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Text:
    def __init__(self,text,pos):
        
        font = pygame.font.Font('freesansbold.ttf', 72)
        self.text = font.render(text, True, (255,0,0), (255,255,255))
        self.textRect = self.text.get_rect()
        self.textRect.center = self._convert_position(pos)

    def blit(self,screen):
        screen.blit(self.text, self.textRect)
    
    def _convert_position(self,pos):
        w = SCREEN_WIDTH//3
        h = SCREEN_HEIGHT//3
        p1 = pos[0]
        p2 = pos[1]
        return (w*p1 + w//2,h*p2+ h//2)

class pygameBoard(Board):
    def __init__(self):
        super().__init__()

    def pygame_display(self,screen):
        '''
        display the current board on the screen
        '''
        #There are 3 rows and 3 columns
        w1 = SCREEN_WIDTH//3
        h1 = SCREEN_HEIGHT//3


        for row in range(3):
            for col in range(3):
                if self.board[row][col] != ' ':
                    text = Text(self.board[row][col],(row ,col ))  
                     
                    text.blit(screen)


def reset_screen(screen):
    '''
    reset the screen and draw
    the tic tac toe lines
    '''
    w1 = SCREEN_WIDTH//3
    w2 = (2*SCREEN_WIDTH)//3
    h1 = SCREEN_HEIGHT//3
    h2 = (2*SCREEN_HEIGHT)//3
    screen.fill("White")
    pygame.draw.line(screen, (0,0,0), (w1, 0), (w1, SCREEN_HEIGHT))
    pygame.draw.line(screen, (0,0,0), (w2, 0), (w2, SCREEN_HEIGHT))
    pygame.draw.line(screen, (0,0,0), (0,h1), ( SCREEN_HEIGHT,h1))
    pygame.draw.line(screen, (0,0,0), (0,h2), (SCREEN_HEIGHT,h2))
    
    return screen