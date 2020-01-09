import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Space invaders')
icon = pygame.image.load('food.png')
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load('food.png')
playerX = 300
playerY = 300
def player(x, y):
  screen.blit(player_image, (x, y))

# game loop
running = True
while running:
  screen.fill((10,50,80))
  for event in pygame.event.get():
    playerX_change = 0
    playerY_change = 0

    if event.type == pygame.QUIT:
      running = False
    # if keystroke is pressed, check wether right or left
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -10
      if event.key == pygame.K_RIGHT:
        playerX_change = 10
      if event.key == pygame.K_UP:
        playerY_change = -10
      if event.key == pygame.K_DOWN:
        playerY_change = 10


    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        playerY_change = 0
  playerX += playerX_change
  playerY += playerY_change

  if playerX > 600:
    playerX = 600
  elif playerX < 0:
    playerX = 0
  if playerY > 500:
    playerY = 500
  elif playerY < 0:
    playerY = 0

  player(playerX, playerY)
  pygame.display.update()
