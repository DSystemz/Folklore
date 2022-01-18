import pygame, os
from pygame.locals import *
from sys import exit


menu_selecao = 1

width = 800
height = 700
FPS = 30

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height), 0,32)
enter = False

def events():
    global menu_selecao, enter

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                menu_selecao += 1

            if event.key == K_UP:
                menu_selecao -= 1

            if event.key == K_RETURN:
                menu_selecao += 10

def select():
    global menu_selecao, enter

    if menu_selecao == 1:
        screen.fill((0, 0, 0))

        fonte =  pygame.font.SysFont("Arial", 20, False, False)
        new_game = fonte.render("==>      Novo Jogo     ", True, (80, 80, 80))
        screen.blit(new_game, ((width/2)-55, (height/2)))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        load_game = fonte.render("        Carregar Jogo    ", True, (80, 80, 80))
        screen.blit(load_game, ((width/2)-50, (height/2)+22))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        cfg_game = fonte.render("        Configurações    ", True, (80, 80, 80))
        screen.blit(cfg_game, ((width/2)-50, (height/2)+44))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        abt_game = fonte.render("        Sobre    ", True, (80, 80, 80))
        screen.blit(abt_game, ((width/2)-20, (height/2)+66))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        ext_game = fonte.render("        Sair    ", True, (80, 80, 80))
        screen.blit(ext_game, ((width/2)-15, (height/2)+88))

    if menu_selecao == 2:
        screen.fill((0, 0, 0))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        new_game = fonte.render("             Novo Jogo     ", True, (80, 80, 80))
        screen.blit(new_game, ((width / 2) - 55, (height / 2)))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        load_game = fonte.render("=>      Carregar Jogo    ", True, (80, 80, 80))
        screen.blit(load_game, ((width / 2) - 65, (height / 2) + 22))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        cfg_game = fonte.render("        Configurações    ", True, (80, 80, 80))
        screen.blit(cfg_game, ((width / 2) - 50, (height / 2) + 44))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        abt_game = fonte.render("        Sobre    ", True, (80, 80, 80))
        screen.blit(abt_game, ((width / 2) - 20, (height / 2) + 66))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        ext_game = fonte.render("        Sair    ", True, (80, 80, 80))
        screen.blit(ext_game, ((width / 2) - 15 , (height / 2) + 88))

    if menu_selecao == 3:
        screen.fill((0, 0, 0))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        new_game = fonte.render("             Novo Jogo     ", True, (80, 80, 80))
        screen.blit(new_game, ((width / 2) - 55, (height / 2)))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        load_game = fonte.render("        Carregar Jogo    ", True, (80, 80, 80))
        screen.blit(load_game, ((width / 2) - 50, (height / 2) + 22))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        cfg_game = fonte.render("=>      Configurações    ", True, (80, 80, 80))
        screen.blit(cfg_game, ((width / 2) - 65, (height / 2) + 44))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        abt_game = fonte.render("        Sobre    ", True, (80, 80, 80))
        screen.blit(abt_game, ((width / 2) - 20, (height / 2) + 66))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        ext_game = fonte.render("        Sair    ", True, (80, 80, 80))
        screen.blit(ext_game, ((width / 2) - 15, (height / 2) + 88))

    if menu_selecao == 4:
        screen.fill((0, 0, 0))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        new_game = fonte.render("             Novo Jogo     ", True, (80, 80, 80))
        screen.blit(new_game, ((width / 2) - 55, (height / 2)))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        load_game = fonte.render("        Carregar Jogo    ", True, (80, 80, 80))
        screen.blit(load_game, ((width / 2) - 50, (height / 2) + 22))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        cfg_game = fonte.render("        Configurações    ", True, (80, 80, 80))
        screen.blit(cfg_game, ((width / 2) - 50, (height / 2) + 44))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        abt_game = fonte.render("=>      Sobre    ", True, (80, 80, 80))
        screen.blit(abt_game, ((width / 2) - 35, (height / 2) + 66))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        ext_game = fonte.render("        Sair    ", True, (80, 80, 80))
        screen.blit(ext_game, ((width / 2) - 15, (height / 2) + 88))

    if menu_selecao == 5:
        screen.fill((0, 0, 0))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        new_game = fonte.render("             Novo Jogo     ", True, (80, 80, 80))
        screen.blit(new_game, ((width / 2) - 55, (height / 2)))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        load_game = fonte.render("        Carregar Jogo    ", True, (80, 80, 80))
        screen.blit(load_game, ((width / 2) - 50, (height / 2) + 22))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        cfg_game = fonte.render("        Configurações    ", True, (80, 80, 80))
        screen.blit(cfg_game, ((width / 2) - 50, (height / 2) + 44))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        abt_game = fonte.render("        Sobre    ", True, (80, 80, 80))
        screen.blit(abt_game, ((width / 2) - 20, (height / 2) + 66))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        ext_game = fonte.render("=>      Sair    ", True, (80, 80, 80))
        screen.blit(ext_game, ((width / 2) - 15, (height / 2) + 88))
    if menu_selecao == 6:
        menu_selecao = 5

    if menu_selecao == 0:
        menu_selecao = 1

    if menu_selecao == 14:
        menu_selecao = 400

    if menu_selecao == 400:
        screen.fill((0, 0, 0))

        fonte = pygame.font.SysFont("Arial", 20, False, False)
        fonte_render = fonte.render("============> Folkore <============ ", True, (255, 0, 0))
        fonte_render2 = fonte.render("=====>        V.0.1         <=====", True, (255, 0, 0))
        voltar_rend = fonte.render("> Voltar <", True, (80,80,80))
        screen.blit(fonte_render, ((width/2)-130, (height/2)))
        screen.blit((fonte_render2), ((width/2)-130, (height/2)+20))
        screen.blit(voltar_rend, ((width/2)-45), (height/2)+300)

    if menu_selecao == 401:
        menu_selecao = 400

    if menu_selecao == 399:
        menu_selecao = 400

    if menu_selecao == 410:
        menu_selecao = 4

    if menu_selecao == 15:
        menu_selecao = 500

    if menu_selecao == 500:
        pygame.quit()
        exit()

while True:
    clock.tick(FPS)
    events()
    select()

    pygame.display.update()