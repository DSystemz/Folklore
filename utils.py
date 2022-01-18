import pygame
from Images import Images
# CONFIGURAÇÕES INICIAIS
width = 800
height = 440
pygame.init()
block_width = width // 40
block_height = height // 20
img = Images()

# CARREGAMENTO DE MÚSICAS E SONS
pygame.mixer.music.load("C:\ProjetinhoFellas\Folks\Folkore\Sounds\8bit Bossa.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Folks")
screen = pygame.display.set_mode((950, 440), pygame.FULLSCREEN)