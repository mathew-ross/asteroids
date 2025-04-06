import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
  pygame.init()
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  dt = 0
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)

  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  asteroidfield = AsteroidField()
  
  loop_state = True
  while loop_state == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    updatable.update(dt)

    screen.fill("black")
    
    for obj in drawable:
      obj.draw(screen)
    
    pygame.display.flip()
    

    # Limiting framerate to 60FPS
    dt = clock.tick(60)/1000

if __name__ == "__main__":
  main()
