import random
import pygame
# Definitions and Constants 
# Define some colors
player1 = raw_input('Enter Player1 Name: ')
player2 = raw_input('Enter Player2 Name: ')

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

CARD_WIDTH = 100
CARD_HEIGHT = 100
BOARD_WIDTH = 4
BOARD_HEIGHT = 4

cards = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]

CARD_DOWN = 'DOWN'
CARD_UP = 'UP'
CARD_MATCHED = 'MATCHED'

board_state = []
board_layout = []
record_num = []


card_count = 0
card_back = None
game_over = False
#switch = 0
#switch_init = 1
reset = 0


firstcard = None

turn_list = [0,1]
def player_shuffle(turn_list):
    global turn
    random.shuffle(turn_list)
    turn = turn_list[0]



# Game Functions
def board_init(board_state):
    for y in range(BOARD_HEIGHT):
        row = []
        for x in range(BOARD_WIDTH):
            row.append(CARD_DOWN)
        board_state.append(row)



def board_shuffle(board_layout):
    

	random.shuffle(cards)
	i = 0
	for y in range(BOARD_HEIGHT):
		row = []
		for x in range(BOARD_WIDTH):
			row.append(cards[i])
			i += 1
		board_layout.append(row)


def get_board_pos(pixel_pos):
    return (pixel_pos[0] / CARD_WIDTH, pixel_pos[1] / CARD_HEIGHT)

def get_card_state(x, y):
    return board_state[y][x]

def set_card_down(x, y):
    board_state[y][x] = CARD_DOWN

def set_card_up(x, y):
    board_state[y][x] = CARD_UP

def set_card_matched(x, y):
    board_state[y][x] = CARD_MATCHED

def draw_all_cards(screen):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            card_state = get_card_state(x,y)
            if card_state == CARD_DOWN:
                screen.blit(card_back, [x*CARD_WIDTH,y*CARD_HEIGHT])
            else:
                pygame.draw.rect(screen, WHITE, 
                                 [x*CARD_WIDTH,y*CARD_HEIGHT,CARD_WIDTH,CARD_HEIGHT])
                card_num = board_layout[y][x]
                card_image = card_map[card_num]
                screen.blit(card_image, [x*CARD_WIDTH,y*CARD_HEIGHT])

    


def toggle_card(x, y):
    card_state = get_card_state(x, y)
    if card_state == CARD_UP:
        set_card_down(x, y)
    elif card_state == CARD_MATCHED:
        set_card_matched(x, y)
    else:
        set_card_up(x, y)

def play_turn(x, y):
    global turn, card_count
    
    # Check if we can flip card
    # If not, then return

    # Flip card
    toggle_card(x, y)

    card_count += 1

score1 = 0
score2 = 0
def check_match(x, y):
    global turn, card_count, temp, curr,xF,yF,xS,yS,score1,score2,countdown

    if card_count == 1:
        click_sound.play()
        temp = board_layout[y][x]
        xF = x
        yF = y
#        temp = 0

    if card_count == 2:

        click_sound.play()
        curr = board_layout[y][x]
        xS = x
        yS = y
        if (xS,yS) == (xF,yF):
            pass
            card_count = 1

        elif (xS,yS) != (xF,yF):

            if temp == curr:

                if turn == 0:

                    if (board_state[yS][xS] == CARD_UP) and (board_state[yF][xF] == CARD_UP):
                        score1 += 1
                        set_card_matched(xF,yF)
                        set_card_matched(xS,yS)
                    if (board_state[yS][xS] == CARD_MATCHED) and (board_state[yF][xF] == CARD_MATCHED):
                        score1 = score1

                if turn == 1:
    
                    if (board_state[yS][xS] == CARD_UP) and (board_state[yF][xF] == CARD_UP):
                
                        score2 += 1
                        set_card_matched(xF,yF)
                        set_card_matched(xS,yS)
                    if (board_state[yS][xS] == CARD_MATCHED) and (board_state[yF][xF] == CARD_MATCHED):
                        score2 = score2
            

            else:
            
                pygame.time.wait(500)
                set_card_down(xF, yF)
                set_card_down(xS, yS)
                pygame.display.flip()

        if temp == curr:
            if turn == 0:
                turn = 0
            elif turn == 1:
                turn = 1
            card_count = 0

            countdown = 30
        elif temp != curr:
            if turn == 0:
                turn = 1
            elif turn == 1:
                turn = 0
            card_count = 0  
            countdown = 30 

    if card_count == 2 and (xF,yF) != (xS,yS):
        countdown = 30

	

	


# Beginning of Code


board_init(board_state)
board_shuffle(board_layout)
player_shuffle(turn_list)
pygame.init()


# Time

font = pygame.font.SysFont(None, 20)
font1 = pygame.font.SysFont(None, 40)
TIMER_EVENT = pygame.USEREVENT
pygame.time.set_timer(TIMER_EVENT, 1000)
countdown = 30
# Set the width and height of the screen
size = [400, 600]
screen = pygame.display.set_mode(size)
screen.fill(WHITE)



pygame.display.set_caption("Halloween Memory Game")
card_back = pygame.image.load("pumpkin1.jpg").convert()
card_up0 = pygame.image.load("img0.jpg").convert()
card_up1 = pygame.image.load("img1.jpg").convert()
card_up2 = pygame.image.load("img2.jpg").convert()
card_up3 = pygame.image.load("img3.jpg").convert()
card_up4 = pygame.image.load("img4.jpg").convert()
card_up5 = pygame.image.load("img5.jpg").convert()
card_up6 = pygame.image.load("img6.jpg").convert()
card_up7 = pygame.image.load("img7.jpg").convert()
card_map = [card_up0, card_up1, card_up2, card_up3, card_up4, card_up5, card_up6, card_up7]
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

click_sound = pygame.mixer.Sound("click.wav")

clicked = False
# Main event loop

while not done:
    text_name1 = font.render(player1+' :'+ str(score1), True, (0,0,0))
    text_name2 = font.render(player2+' :'+ str(score2), True, (0,0,0))
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == TIMER_EVENT:
#        	seconds += 1
        	countdown -= 1
        	if countdown <= 0 or card_count==2:
        	    print
 
                
                if countdown == 0:
                    if turn == 1:
                        turn = 0
                    if turn == 0:
                        turn = 1

        		countdown = 30               
        	else:
        		pygame.draw.rect(screen, (255,255,255), 
                                 [15,15,375, 575])
                text1 = font.render('Time Count:', True, (0, 0, 0), (255, 255,255))
                text = font.render(str(countdown), True, (0, 0, 0), (255, 255, 255))
                screen.blit(text, (370,575))
                screen.blit(text1, (275,575))
                screen.blit(text_name1, (30,450))
                screen.blit(text_name2, (30,525))
                if turn == 0:
                    pygame.draw.rect(screen, WHITE,
                            [0,525,7,7])
                    pygame.draw.rect(screen, BLACK,
                            [0,450,7,7])
                elif turn == 1:
                    pygame.draw.rect(screen, WHITE,
                            [0,450,7,7])
                    pygame.draw.rect(screen, BLACK,
                            [0,525,7,7])

  
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            ex, ey = get_board_pos(event.pos)
            if ex <=3 and ey <=3:
                if (board_state[ey][ex] == CARD_MATCHED):
                    clicked = False
                else:
                    play_turn(ex, ey)
    
                    clicked = True 
                    toggle_card(ex, ey)
                    set_card_up(ex, ey)
            else:
                pass

                        

    draw_all_cards(screen)
    
    if score1 + score2 == 8:
        if score1 > score2:
            text = font1.render('PLAYER 1 WINS!!!', True, (0, 0, 0), (255, 255,255))
            text1 = font.render('Hit Esc to and run program again to play again', True, (0, 0, 0), (255, 255,255))

            screen.fill((255, 255, 255))
            screen.blit(text,
                (200 - text.get_width() // 2, 300 - text.get_height() // 2))
            screen.blit(text1,
                (150 - text.get_width() // 2, 400 - text.get_height() // 2))
    
            pygame.display.flip()
            clock.tick(20)

        if score2 > score1:
            text = font1.render('PLAYER 2 WINS!!!', True, (0, 0, 0), (255, 255,255))
            text1 = font.render('Hit Esc to and run program again to play again', True, (0, 0, 0), (255, 255,255))
            screen.fill((255, 255, 255))
            screen.blit(text,
                (200 - text.get_width() // 2, 300 - text.get_height() // 2))
            screen.blit(text1,
                (150 - text.get_width() // 2, 400 - text.get_height() // 2))
    
            pygame.display.flip()
            clock.tick(20)

        if score2 == score1:
            text = font1.render('PLAYERS TIED!!!', True, (0, 0, 0), (255, 255,255))
            text1 = font.render('Hit Esc to and run program again to play again', True, (0, 0, 0), (255, 255,255))
            screen.fill((255, 255, 255))
            screen.blit(text,
                (200 - text.get_width() // 2, 300 - text.get_height() // 2))
            screen.blit(text1,
                (150 - text.get_width() // 2, 400 - text.get_height() // 2))
    
            pygame.display.flip()
            clock.tick(20)


    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    if clicked:
        if get_card_state != CARD_MATCHED:
            check_match(ex, ey)
            clicked = False

     
# Exit cleanly
print "Exiting..."
pygame.quit()

