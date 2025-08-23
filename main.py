import pygame

print('Setup Start')
pygame.init() #initialize pygame
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Setup Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit() #fechar pygame
