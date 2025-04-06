import pygame
from constants import *

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  loop_state = True
  while loop_state == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    screen.fill("black")
    pygame.display.flip()
    
    # Limiting framerate to 60FPS
    dt = clock.tick(60)/1000

if __name__ == "__main__":
  main()
