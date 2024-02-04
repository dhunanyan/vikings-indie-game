import pygame

from config import config
from config import assets

from components.viking import Viking
from components.background import Background

pygame.init()

screen_size = (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)

Clock = pygame.time.Clock()

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
  Background(0, sprites)
  Background(1, sprites)
  
  return Viking(sprites)

viking = create_sprites()

direction = 'right'
running = True
game_over = False
game_started = False
FPS = config.FPS

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  viking.update(direction, keys)
  
  screen.fill('pink')
  sprites.draw(screen)

  if game_started and not game_over:
    sprites.update()
  
  pygame.display.flip()
  Clock.tick(FPS)

pygame.quit()