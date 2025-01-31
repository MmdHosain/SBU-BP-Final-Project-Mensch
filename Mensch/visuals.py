import pygame
import SecondMenu as sec
import FirstMenu as fir
import dice 
import confirmation as con

# colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 230, 0)
GREEN = (0, 150, 0)
BIEGE = (200, 174, 126)
LIGHT_GREEN = (144, 238, 144)
LIGHT_RED = (255, 104, 101)
LIGHT_BLUE = (173, 216, 230)
LIGHT_YELLOW = (255, 255, 102)

def board(click_volume , music_volume):
    # Initialize Pygame
    pygame.init()

    # Set initial width and height
    WIDTH, HEIGHT = 600, 600
    screen_board = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mnech")
    screen_board.fill(BIEGE)

    running = True
    confirm_exit = False
    selected_option = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    WIDTH, HEIGHT = 300, 400
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption("Mensch")
                    fir.Lobby(screen, WIDTH, HEIGHT,click_volume , music_volume )
                    confirm_exit = True
                

        # if confirm_exit:
        #     # Draw confirmation box
        #     result = con.confirm(screen_board, selected_option)
        #     if result is False:
        #         confirm_exit = False
        #     elif result is True:
        #         running = False


                        
    # making dice work with keyboard and mouse
        def dice_loc(screen_board) :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    return dice.dice_roll(screen_board)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()
                if 260 <= mouse_pos[0] <= 340 and 260 <= mouse_pos[1] <= 340:
                    
                    return dice.dice_roll(screen_board)  # use dice by click on it
                
            else :
                pass
            
            
        def start_end():

            # Draw starter pieces location  - Red
            pygame.draw.circle(screen_board, RED, (50, 40), 20)  
            pygame.draw.circle(screen_board, RED, (120, 40), 20)  
            pygame.draw.circle(screen_board, RED, (50, 120), 20)  
            pygame.draw.circle(screen_board, RED, (120,120), 20)
            # final locations for Red
            pygame.draw.circle(screen_board, LIGHT_RED, (90, 300), 20)
            pygame.draw.circle(screen_board, LIGHT_RED, (140, 300), 20) 
            pygame.draw.circle(screen_board, LIGHT_RED, (190, 300), 20)
            pygame.draw.circle(screen_board, LIGHT_RED, (240, 300), 20)
            
            
            # Draw starter pieces location  - Blue
            pygame.draw.circle(screen_board, BLUE, (50, 560), 20)  
            pygame.draw.circle(screen_board, BLUE, (120, 560), 20)  
            pygame.draw.circle(screen_board, BLUE, (50, 480), 20)  
            pygame.draw.circle(screen_board, BLUE, (120, 480), 20) 
            # final locations for Blue
            pygame.draw.circle(screen_board, LIGHT_BLUE, (300, 500), 20)
            pygame.draw.circle(screen_board, LIGHT_BLUE, (300, 450), 20)
            pygame.draw.circle(screen_board, LIGHT_BLUE, (300, 400), 20)
            pygame.draw.circle(screen_board, LIGHT_BLUE, (300, 350), 20)
            
            
            
            # Draw starter pieces location  - Green
            pygame.draw.circle(screen_board, GREEN, (550, 40), 20)  
            pygame.draw.circle(screen_board, GREEN, (480, 120), 20)  
            pygame.draw.circle(screen_board, GREEN, (480, 40), 20)  
            pygame.draw.circle(screen_board, GREEN, (550, 120), 20) 
            # final locations for Green
            pygame.draw.circle(screen_board, LIGHT_GREEN, (300, 100), 20)
            pygame.draw.circle(screen_board, LIGHT_GREEN, (300,150), 20)  
            pygame.draw.circle(screen_board, LIGHT_GREEN, (300, 200), 20)
            pygame.draw.circle(screen_board, LIGHT_GREEN, (300, 250), 20)      
            
            
            
            # Draw starter pieces location  - Yellow
            pygame.draw.circle(screen_board, YELLOW, (550, 560), 20)  
            pygame.draw.circle(screen_board, YELLOW, (480, 560), 20)  
            pygame.draw.circle(screen_board, YELLOW, (480, 480), 20)  
            pygame.draw.circle(screen_board, YELLOW, (550 ,480), 20) 
            
            # final locations for Yellow
            pygame.draw.circle(screen_board, LIGHT_YELLOW, (510, 300), 20)
            pygame.draw.circle(screen_board, LIGHT_YELLOW, (460, 300), 20) 
            pygame.draw.circle(screen_board, LIGHT_YELLOW, (410, 300), 20)
            pygame.draw.circle(screen_board, LIGHT_YELLOW, (360, 300), 20)
        
        
        def path_way():
            """create path of pieces path of pieces""" 
            x = 40 
            y = 250
            for i in range(1, 40):
                if x < 240 and y == 250:
                    while x < 240:
                        pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                        x += 50
                elif x == 240 and y <= 250:
                    while y >= 50:
                        pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                        y -= 50

                    x = 360   
                    if x == 360 and y == 0:
                        while y < 250:
                            y += 50
                            pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                            
                    if x == 360 and y == 250:
                        while x <= 550:
                            x += 50
                            pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                    
                    y = 350
                    if x == 560 and y == 350:
                        while x > 360:
                            pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                            x -= 50
                    
                    if x == 360 and y == 350:
                        while y <= 550:
                            pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                            if y == 550:
                                break
                            y += 50
                            
                    x = 240       
                    if x == 240 and y == 550:
                        while y > 350:
                            pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                            y -= 50
                    if x == 240 and y == 350:
                        while x >= 40:
                            pygame.draw.circle(screen_board, WHITE, (x, y), 20)
                            x -= 50
                            
            #start location
            pygame.draw.circle(screen_board, LIGHT_RED, (40,250 ), 20)
            pygame.draw.circle(screen_board, LIGHT_GREEN, (360, 50), 20)
            pygame.draw.circle(screen_board, LIGHT_BLUE, (240, 550), 20)
            pygame.draw.circle(screen_board, LIGHT_YELLOW, (560, 350), 20)
            
            pygame.draw.circle(screen_board, WHITE, (40, 300), 20)
            pygame.draw.circle(screen_board, WHITE, (40, 300), 20)
            pygame.draw.circle(screen_board, WHITE, (300, 50), 20)
            pygame.draw.circle(screen_board, WHITE, (300, 550), 20)
            pygame.draw.circle(screen_board, WHITE, (560, 300), 20)
        
                    

        def arrows():
            
        
            # Horizontal arrow
            #Red
            pygame.draw.line(screen_board, BLACK, (40, 200), (100, 200), 8)
            pygame.draw.line(screen_board, BLACK, (100, 200), (90, 190), 8)
            pygame.draw.line(screen_board, BLACK, (100, 200), (90, 210), 8)
            #Yellow
            pygame.draw.line(screen_board, BLACK, (560, 400), (500, 400), 8)
            pygame.draw.line(screen_board, BLACK, (500, 400), (510, 390), 8)
            pygame.draw.line(screen_board, BLACK, (500, 400), (510, 410), 8)
            
            #vertical arrow
            #Green
            pygame.draw.line(screen_board, BLACK, (410, 50), (410, 110), 8)
            pygame.draw.line(screen_board, BLACK, (410, 110), (420, 100), 8)
            pygame.draw.line(screen_board, BLACK, (410, 110), (400, 100), 8)
            #Blue
            pygame.draw.line(screen_board, BLACK, (190, 550), (190, 490), 8)
            pygame.draw.line(screen_board, BLACK, (190, 490), (180, 500), 8)
            pygame.draw.line(screen_board, BLACK, (190, 490), (200, 500), 8)
            
        dice_loc(screen_board)
        path_way()
        arrows()
        start_end()
        
        # Update the display
        pygame.display.flip()
   

    pygame.display.flip()
    
    pygame.quit()
    
    
    
                   
        


   




