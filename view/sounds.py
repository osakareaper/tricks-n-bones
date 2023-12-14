import pygame

# Sounds

pygame.mixer.init()

scoreUp = pygame.mixer.Sound("assets/sounds/scoreUp.wav")
nextLevel = pygame.mixer.Sound("assets/sounds/nextLevel.wav")
walk = pygame.mixer.Sound("assets/sounds/walk.wav")
death = pygame.mixer.Sound("assets/sounds/death.wav")
noKey = pygame.mixer.Sound("assets/sounds/noKey.wav")