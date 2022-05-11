# Code to make a pong game

# Things to implement:
# 1. Make a very basic pong game
# 2. Change players to LOTR pictures
# 3. Add abilities
# 4. Defeat Sauron

# Import pygame and sys
import pygame, sys, random

# Global Variables
direction = (-1,1)

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, enemy_score

    screen.blit(ball_image,(300,300))

    # Movement Dynamics
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Boundaries: roof/floor
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        pygame.mixer.Sound.play(plob_sound)

    # Boundaries: left/right
    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0:
            enemy_score += 1
        elif ball.right >= screen_width:
            player_score += 1
        ball_respawn()

        pygame.mixer.Sound.play(score_sound)


    # Collisions
    if ball.colliderect(player) or ball.colliderect(enemy):
        ball_speed_x *= -1
        pygame.mixer.Sound.play(plob_sound)

    screen.blit(ball_image,(300,300))

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def enemy_animation():
    if enemy.top < ball.y:
        enemy.top += enemy_speed
    elif enemy.top > ball.y:
        enemy.bottom -= enemy_speed

    if enemy.top <= 0:
        enemy.top = 0
    if enemy.bottom >= screen_height:
        enemy.bottom = screen_height

def ball_respawn():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)

    ball_speed_y *= random.choice(direction)
    ball_speed_x *= random.choice(direction)

# Setup pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the screen
screen_width = 1200
screen_height = 900
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

# Caption
pygame.display.set_caption('Pong')

# Game Rectangles
ball_size = 30
ball_image = pygame.image.load('ball.png')
ball = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size, ball_size)

player_length = 140
player_width = 10
player = pygame.Rect(10, screen_height/2 - player_length/2, player_width, player_length)
enemy = pygame.Rect(screen_width - player_width - 10, screen_height/2 - player_length/2, player_width, player_length)

bg_color = pygame.Color('black')
white = (255,255,255)

# Game Variables
ball_speed_x = 7 * random.choice(direction)
ball_speed_y = 7 * random.choice(direction)
player_speed = 0
enemy_speed = 6.2

# Score
player_score = 0
enemy_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

# Sound
plob_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

# Game Loop ------------------------------------------------------
while True:
    # Close the window
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()                         # Uninitialize the pygame module
            sys.exit()                            # Closes the entire program
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 12
            if event.key == pygame.K_UP:
                player_speed -= 12
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 12
            if event.key == pygame.K_UP:
                player_speed += 12

    ball_animation()
    screen.blit(ball_image,(300,300))
    player_animation()
    enemy_animation()

    # Fill Screen
    screen.fill(bg_color)
    
    # Draw Player, Enemy and Ball Rectangles
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, enemy)
    pygame.draw.ellipse(screen, white, ball)

    # Line separating the two sides
    mid_top = (screen_width/2, 0)
    mid_bottom = (screen_width/2, screen_height)
    pygame.draw.aaline(screen, white, mid_top, mid_bottom)

    # Score display
    player_text = basic_font.render(f'{player_score}', False, white)
    screen.blit(player_text, (300,20))

    enemy_text = basic_font.render(f'{enemy_score}', False, white)
    screen.blit(enemy_text, (900,20))
    
    # Update the window
    pygame.display.flip()
    clock.tick(60)                                # Set the fps
# ----------------------------------------------------------------