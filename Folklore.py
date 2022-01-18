import pygame
from player import Player

pygame.init()
display = pygame.display.set_mode((950, 680), pygame.FULLSCREEN)  # definindo full screen
pygame.display.set_caption("Folks")  # Título da janela

# Objects
objectGp = pygame.sprite.Group()
player = Player(objectGp)


# adicionando musica de fundo
pygame.mixer.music.load("C:\\ProjetinhoFellas\\Folks\\Sounds\\storm.mp3")
pygame.mixer.music.play(-1)

gameLoop = True               # Linha de codigos
clock = pygame.time.Clock()

while gameLoop:               # Para definir a
    pygame.display.update()   # Persistência da janela
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    #  Desenhando:
    display.fill([19, 173, 235])

    objectGp.update()
    objectGp.draw(display)
