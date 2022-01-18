import pygame.time
from pygame.locals import *
from utils import *
from mapas import mapa, obj
from Images import load_image

clock = pygame.time.Clock()
clock.tick(120)

def colisao_mapa(personagem, map, lista_char):
    colisions = []
    for id_linha, linha in enumerate(map):
        for id_column, character in enumerate(linha):
            if character in lista_char:
                x = id_column * block_width
                y = id_linha * block_height
                r = pygame.Rect((x, y), (block_width, block_height))
                r2 = personagem.rect.copy()
                r2.move_ip(personagem.vel_x, personagem.vel_y)
                if r.colliderect(r2):
                    colisao = {"linha": id_linha, "coluna": id_column, "Caracter": character}
                    colisions.append(colisao)
    return colisions

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\ProjetinhoFellas\Folks\Folkore\Img\characters.png")
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.spritesS = []
        self.spritesS.append(move_s)
        self.spritesS.append(move_s2)
        self.spritesS.append(move_s3)
        self.spritesW = []
        self.spritesW.append(move_w2)
        self.spritesW.append(move_w3)
        self.spritesW.append(move_w)
        self.spritesD = []
        self.spritesD.append(move_d)
        self.spritesD.append(move_d2)
        self.spritesD.append(move_d3)
        self.spritesA = []
        self.spritesA.append(move_a)
        self.spritesA.append(move_a2)
        self.spritesA.append(move_a3)

    def processa(self, event):
        clock = pygame.time.Clock()
        clock.tick(120)


    def update(self, *args):
        colisoes = colisao_mapa(self, mapa, ["g"])
        if len(colisoes) == 0:
            self.rect.move_ip(self.vel_x, self.vel_y)


def draw(map, char_img):
    for id_linha, linha in enumerate(map):
        for id_column, character in enumerate(linha):
            if character in char_img:
                x = id_column * block_width
                y = id_linha * block_height
                imgur = char_img[character]
                screen.blit(imgur, (x, y))

hero = Player()
all_sprites = pygame.sprite.Group(hero)
grupo_heroi = pygame.sprite.Group(hero)

while True:
    pygame.display.update()
    draw(mapa, {"p": img.castle, "c": img.gramado1, "n": img.gramado2, "g": img.castlebrick, "q": img.mid})
    draw(obj, {"a": img.arvores, "b": img.fountain, "z": img.sarc, "f": img.castle2, "h": img.castle3, "t": img.arvore})

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        hero.processa(event)
    all_sprites.draw(screen)
    all_sprites.update()
    grupo_heroi.draw(screen)
    grupo_heroi.update()
    pygame.display.flip()




