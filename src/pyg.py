import pygame
import sys
from agent import Agent
from pygamehelpers import pygameBoard, reset_screen, Text, SCREEN_WIDTH, SCREEN_HEIGHT
import time 

def run_game():
    '''
    main game loop 

    To DO: Put Player and ai win into the board class
            and put more of the game logic from the 
            game loop into the board class.
    '''

    #agent is quick to train on this one!
    board= pygameBoard()
    agent = Agent()
    agent.train()
    pygame.init()

    pygame.display.set_caption("Tic Tac Toe")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    #add player wins text
    player_wins = 0
    font = pygame.font.Font('freesansbold.ttf', 24)
    player_text = font.render(f"Player: {player_wins}", True, (0,255,0), (255,255,255))
    player_textRect = player_text.get_rect()
    player_textRect.center = (60,12)

    #add ai wins text 
    ai_wins = 0 
    font = pygame.font.Font('freesansbold.ttf', 24)
    #(string, antialias, color, background)
    ai_text = font.render(f"AI: {ai_wins}", True, (0,0,255), (255,255,255))
    ai_textRect = ai_text.get_rect()
    ai_textRect.center = (SCREEN_WIDTH-60,12)

    screen = reset_screen(screen)

    while True:
        
        ai_text = font.render(f"AI: {ai_wins}", True, (0,0,255), (255,255,255))
        screen.blit(player_text, player_textRect)
        screen.blit(ai_text, ai_textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                u,v = pygame.mouse.get_pos()
                p1 = u//200
                p2 = v//200
                if board.board[p1][p2] == ' ':
                    board.make_move((p1,p2))
                    board.pygame_display(screen)
                    time.sleep(.1)
                    if board.check_win():
                        player_wins+=1
                        board.restart()
                        screen = reset_screen(screen)
                        board.pygame_display(screen)
                        break
                    if board.num_moves == 9:
                       
                        board.restart()
                        screen = reset_screen(screen)
                        board.pygame_display(screen)
                        break
                    
                    a1,a2 = agent.get_action(board)
                    board.make_move((a1,a2))
                    if board.check_win():
                        ai_wins+=1
                        time.sleep(.1)
                        board.restart()
                        screen = reset_screen(screen)
                        board.pygame_display(screen)
                    board.pygame_display(screen)

    
        pygame.display.update()
        clock.tick(30)



if __name__ == "__main__":
    run_game()