import pygame
from constants import *

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  loop_state = True
  while loop_state == True:
    screen.fill("black")
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

if __name__ == "__main__":
  main()
