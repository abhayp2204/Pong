import pygame
pygame.init()
from pygame.locals import *
from pygame import mixer

import sys
import random
import math
import time
import csv

def draw():
    # Draw Ball
    ball_location = (ball_x, ball_y)
    screen.blit(ball_img, ball_location)

    # Draw Player 1
    player1_location = (10, player1_y)
    screen.blit(player1_img, player1_location)

    # Draw Player 2
    player2_location = (screen_width-player2_size-10,player2_y)
    screen.blit(player2_img, player2_location)

    # Draw Nazgul
    if nazgul_summoned:
        nazgul_location = (nazgul_x, nazgul_y)
        screen.blit(nazgul_img, nazgul_location)

    # Draw Frodo
    if frodo_used:
        global frodo_album_index
        frodo_location = (frodo_x, frodo_y)
        screen.blit(frodo_album[frodo_album_index], frodo_location)

def ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, end

    # Ball Movements
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Boundaries: Up and Down
    if( ball_y >= screen_height-ball_size or ball_y <= 0 ):
        ball_speed_y *= -1
    # Boundaries: Left and Right
    if( ball_x >= screen_width-ball_size or ball_x <= 0 ):
        ball_speed_x *= -1

def player1():
    global player1_y, player1_size

    # Player Movements
    player1_y += player1_speed_y

    # Boundaries: Up and Down
    if( player1_y <= 0 ):
        player1_y = 0
    elif( player1_y >= screen_height-player1_size ):
        player1_y = screen_height-player1_size

def player2():
    global player2_y

    # Player Movements (AI)
    if player2_y > ball_y:
        player2_y -= player2_speed
    elif player2_y < ball_y:
        player2_y += player2_speed

def nazgul():
    global nazgul_x, nazgul_y, nazgul_speed_y_original
    global nazgul_speed_x, nazgul_speed_y
    global nazgul_summoned
    global nazgul_pi_smoothness

    # Nazgul Movements
    nazgul_x -= nazgul_speed_x

    if frodo_used:
        target = frodo_y
    else:
        target = player1_y
    
    dist_to_target = nazgul_y - target
    if abs(dist_to_target) <= pi*nazgul_pi_smoothness:
        nazgul_speed_y = nazgul_speed_y_original * (1 - math.cos(dist_to_target/nazgul_pi_smoothness))
    else:
        nazgul_speed_y = nazgul_speed_y_original

    # Nazgul follows Target(Gollum / Frodo)
    if nazgul_y > target:
        nazgul_y -= nazgul_speed_y
    elif nazgul_y < target:
        nazgul_y += nazgul_speed_y

def frodo(i):
    global frodo_used
    global frodo_x
    global frodo_y

def show_score():
    score_string = font.render("Score : " + str(score), True, white)
    score_location = (10,10)
    screen.blit(score_string, score_location)

    life_string = font.render("Lives : " + str(life), True, white)
    life_location = (290,10)
    screen.blit(life_string, life_location)

def isCollision(hazard_x, hazard_y, target_x, target_y):
    # If the hazard is right before target
    if hazard_x >= 10 + target_x + player1_size and hazard_x <= 10 + target_x + player1_size + 0.5 * game_speed:
        # Make sure the hazard hits target
        if( hazard_y + ball_size >= target_y and hazard_y <= target_y + player1_size ):
            return True
        else:
            return False
    
    return False

def isCollision2():
    global player2_y
    span = 0

    # If the ball is right before player 2
    if ball_x >= screen_width-10-player2_size-(0.5*game_speed)-44 and ball_x <= screen_width-10-player2_size-44:
        # Make sure the ball hits player 2
        if( ball_y + ball_size >= player2_y - span and ball_y <= player2_y + player2_size + span ):
            return True
        else:
            return False
    
    return False

def game_over(message):
    global saved_score
    global high_score

    # Immortal
    if immortal:
        return

    # "Game Over"
    game_over_text = big_text.render("Game Over", True, red)
    middle_screen_top= (screen_width/2-180,screen_height/2-60)

    # Death Message: "You Lost The Ring" or "Nazgul Killed You"
    death_context = small_text.render(message, True, red)
    middle_screen_middle = (screen_width/2-180 + 35,screen_height/2 + 14)

    # Save name and score to database
    if not saved_score:
        with open(path + 'high_scores.csv','a') as hs:
            csv_hs = csv.writer(hs)
            line = [user_name.strip()] + [score]
            csv_hs.writerow(line)

        with open(path + 'high_scores.csv','r') as hs:
            csv_hs = csv.reader(hs)
            for line in csv_hs:
                csv_name = line[0]
                csv_score = line[1]
                # print("csv score", csv_score)
                # print("high score", high_score)
                if int(csv_score) > int(high_score):
                    high_score = csv_score
        saved_score = True

    # "Score: X"
    final_score = small_text.render("Score : " + str(score), True, red)
    middle_screen_lower = (screen_width/2-180 + 110,screen_height/2 + 54)

    # "High Score: X"
    high_score_str = small_text.render("High Score : " + str(high_score), True, red)
    middle_screen_lowest = (screen_width/2-121, screen_height/2 + 95)

    # Write On Screen
    screen.blit(game_over_text, middle_screen_top)
    screen.blit(death_context, middle_screen_middle)
    screen.blit(final_score, middle_screen_lower)
    screen.blit(high_score_str, middle_screen_lowest)

    return True

# Game Variables
game_speed = 1.2
immortal = False
life = 4
pi = 3.14159

origin = (0,0)
start_game = False
high_score = 0
path = "/home/abhay/Desktop/Python/Games/Pong/"

# Create the screen
screen_width = 1200
screen_height = int(screen_width/4)*3

screenSize = (screen_width, screen_height)
screen = pygame.display.set_mode(screenSize)

# Background Image
# background = pygame.image.load('Images/background2.png')

# Background Music
mixer.music.load(path + 'Sound/digital.wav')
mixer.music.play(-1)

# Load Images
icon = pygame.image.load(path + 'Images/icon.png')
player1_img = pygame.image.load(path + 'Images/gollum.png').convert()
player2_img = pygame.image.load(path + 'Images/sauron.png').convert()
ball_img = pygame.image.load(path + 'Images/ring.png').convert()
nazgul_img = pygame.image.load(path + 'Images/wkoa5.jpg').convert()
frodo0_img = pygame.image.load(path + 'Images/frodo0.jpg').convert()
frodo1_img = pygame.image.load(path + 'Images/frodo1.jpg').convert()
frodo2_img = pygame.image.load(path + 'Images/frodo2.jpg').convert()

# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (250,150,0)

# Title and Icon
pygame.display.set_caption("Pong")
pygame.display.set_icon(icon)

# Ball : The One Ring
ball_size = 49

ball_x = screen_width/2-ball_size
ball_y = screen_height/2-ball_size

speed_wrt_screen = screen_width/1200
ball_velocity = 0.42 * game_speed
ball_speed_x = -0.3 * game_speed
ball_speed_y_initial = math.sqrt(ball_velocity**2 - ball_speed_x**2)
ball_speed_y = math.sqrt(ball_velocity**2 - ball_speed_x**2)

ball_acceleration_x = 0.02
ball_acceleration_y = 0.012

ball_jerk_x = 0.9
ball_jerk_y = 0.9

# Player 1 : Gollum
player1_size = 64
player1_x = 10
player1_y = screen_height/2-player1_size
player1_speed = 0.5*game_speed
player1_speed_y = 0

# Player 2 : Sauron
player2_size = 64
player2_x = screen_width-player2_size-10
player2_y = screen_height/2-player2_size
player2_speed = 0.9 * game_speed
player2_yChange = 0

# Score
saved_score = False
score = 0
score_copy = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Nazgul
nazgul_size = 64
nazgul_pi_smoothness = 20
nazgul_summoned = False

nazgul_x = player2_x
nazgul_y = player2_y

nazgul_speed_x = 0.4*game_speed
nazgul_speed_y = 0.16*game_speed
nazgul_speed_y_original = 0.22*game_speed


# Frodo
frodo_size = 64
frodo_used = False
frodo_ready = False

frodo_x = 0
frodo_y = -100

frodo_album = [frodo0_img, frodo1_img, frodo2_img]
frodo_album_index = 0

# Game Over
big_text = pygame.font.Font('freesansbold.ttf', 64)
small_text = pygame.font.Font('freesansbold.ttf', 32)

# Input player name variables
user_name = ""
keep_centering = screen_width/2 - 10 

# Start Screen
while True:
    # Refill with black
    screen.fill(black)

    # Enter your name
    start_message = big_text.render("Enter Your Name", True, red)
    middle_screen_top = (screen_width/2-280,screen_height/2-99)
    screen.blit(start_message, middle_screen_top)

    # Input player's name
    user_name_surface = big_text.render(user_name, True, orange)
    user_name_location = (keep_centering, screen_height/2)
    screen.blit(user_name_surface, user_name_location)

    # Events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Get Username
        if event.type == pygame.KEYDOWN:
            # Backspace
            if event.key == pygame.K_BACKSPACE:
                user_name = user_name[0:-1]
                keep_centering += 17
            # Delete
            elif event.key == pygame.K_DELETE:
                user_name = ""
                keep_centering = screen_width/2 - 10 
            # Alphanumeric
            else:
                user_name += event.unicode
                keep_centering -= 17

        # Start (RETURN = ENTER)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_game = True

    # Move to game loop
    if start_game:
        break

    pygame.display.update()

end = False
previous_key = 2
paused = True

# XBOX
pygame.joystick.init();
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
joystick_deadzone = 0.1

# Game Loop
while True:
    # Refill with black, otherwise the images paint the screen
    screen.fill(black)

    # Events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Keyboard Controls
        if event.type == pygame.KEYDOWN:
            # Move UP
            if event.key == pygame.K_w:
                player1_speed_y = -player1_speed
            # Move DOWN
            elif event.key == pygame.K_s:
                player1_speed_y = player1_speed
            # Bait Frodo
            elif event.key == pygame.K_e and frodo_ready and (not paused):   
                frodo_album_index = 0    
                frodo_used = True
                frodo_x = player1_x + player1_size + 10
                frodo_y = player1_y
                frodo_ready = False
            # Pause / Resume
            elif event.key == pygame.K_SPACE:
                paused = not paused

        # Mouse Controls
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Stop
            if event.button >= 1 and event.button <= 3:
                player1_speed_y = 0
            # Move UP
            if event.button == 4:
                player1_speed_y = -player1_speed
            # Move DOWN
            elif event.button == 5:
                player1_speed_y = player1_speed

        # XBOX Controls
        if event.type == JOYAXISMOTION:
            # axis 1 is Y axis
            if event.axis == 1:
                player1_speed_y = player1_speed * event.value

                # Deadzone
                if abs(event.value) < joystick_deadzone:
                    player1_speed_y = 0
        if event.type == JOYBUTTONDOWN:
            # Bait Frodo
            if event.button == 2 and frodo_ready and not paused:
                frodo_album_index = 0
                frodo_used = True
                frodo_x = player1_x + player1_size + 10
                frodo_y = player1_y
                frodo_ready = False
            # Pause / Resume
            if event.button == 7:
                paused = not paused
            # Exit
            if event.button == 6:
                pygame.quit()
                sys.exit()
        
        # Stop sliding
        if event.type == pygame.KEYUP:
            player1_speed_y = 0;

    # Movement Dynamics
    if not end or immortal:
        draw()

        if paused:
            pygame.display.update()
            continue

        player1()
        player2()
        ball()

        if nazgul_summoned:
            nazgul()
        if frodo_used:
            frodo(frodo_album_index)
        show_score()

    # Ability 1 : Frodo
    if score % 7 == 0 and score != 0 and score != score_copy:
        frodo_ready = True
        score_copy = score

    # Nazgul finds gollum
    if isCollision(nazgul_x, nazgul_y,0,player1_y):
        if nazgul_summoned:
            life -= 1
            nazgul_summoned = False

    # Nazgul doesn't find Gollum
    if nazgul_x <= 0:
        nazgul_summoned = False

    # Nazgul finds Frodo
    if isCollision(nazgul_x, nazgul_y, player1_size + 10,frodo_y):
        nazgul_summoned = False
        frodo_album_index += 1

        if frodo_album_index == len(frodo_album):
            frodo_used = False
            frodo_album_index = 0

    # Send nazgul back to Sauron
    if not nazgul_summoned:
        nazgul_x = player2_x - nazgul_size
        nazgul_y = player2_y

    # Summon Nazgul
    if ball_x >= screen_width * 0.8 and not nazgul_summoned:
        nazgul_summoned = True

    if( ball_x >= 200 and ball_x <= screen_width-200 ):
        justCollided = False

    # Collision
    if( (isCollision(ball_x, ball_y,0,player1_y) and (not justCollided)) or (isCollision2() and (not justCollided)) ):
        # Update Score
        if isCollision(ball_x, ball_y,0,player1_y):
            score += 1
        
        ball_speed_x *= -1

        # Slightly deviate from angle(i) = angle(r)
        deviation = 0.16
        ball_random_y = random.uniform(-deviation, deviation) * ball_velocity
        ball_speed_y = (ball_speed_y/abs(ball_speed_y)) * (ball_speed_y_initial + ball_random_y)

        justCollided = True
        
        if(ball_speed_x > 0):
            ball_speed_x += ball_acceleration_x
        else:
            ball_speed_x -= ball_acceleration_x

        if(ball_speed_y > 0):
            ball_speed_y += ball_acceleration_y
        else:
            ball_speed_y -= ball_acceleration_y

        ball_acceleration_x *= ball_jerk_x
        ball_acceleration_y *= ball_jerk_y

    # Game over
    end = False
    if( ball_x < player1_x or ball_x > player2_x ):
        end = game_over("You Lost The Ring")
    if life <= 0:
        end = game_over("Nazgul Killed You")
    
    # Update
    pygame.display.update()

    # XBOX
    # 0 : A
    # 1 : B
    # 2 : X
    # 3 : Y
    # 4 : LB
    # 5 : RB
    # 6 : Back
    # 7 : Start
    # 8 : XBOX
    # 9 : LS