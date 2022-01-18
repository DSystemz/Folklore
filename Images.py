import pygame


def load_image(img_set, x, y):
    width = 800
    height = 440
    block_width = width // 40
    block_height = height // 20
    img_orig = img_set.subsurface((x, y), (16, 16))
    img_scaled = pygame.transform.scale(img_orig, (42, 42))
    return img_scaled


class Images:
    fountain = pygame.image.load("Maps\\Dungeon Crawl Stone Soup Full\\dungeon\\blood_fountain.png")
    sarc = pygame.image.load("Maps\\Dungeon Crawl Stone Soup Full\\dungeon\\dry_fountain.png")
    floor = pygame.image.load("C:\\ProjetinhoFellas\\Folks\\Folkore\\Img\\basictiles.png")

    gramado1 = load_image(floor, 80, 16) #gramado
    gramado2 = load_image(floor, 64, 16) #gramado com plantas
    arvores = load_image(floor, 80, 144) #duas arvores
    arvore = load_image(floor, 64, 144) # uma arvore
    castle = load_image(floor, 16, 96)  #musgo nas pedras
    castle2 = load_image(floor, 64, 112) # pilar quebrado
    castle3 = load_image(floor, 80, 112) # pilar golfinho
    castlebrick = load_image(floor, 0, 0) #brick castelo
    mid = load_image(floor, 0, 64) #mid part

#class Moves:
#    player = pygame.image.load("C:\ProjetinhoFellas\Folks\Folkore\Img\characters.png")
#    move_d = load_image(player, 48, 32)
#    move_d2 = load_image(player, 64, 32)
#    move_d3 = load_image(player, 80, 32)
#    move_a = load_image(player, 48, 16)
#    move_a2 = load_image(player, 64, 16)
#    move_a3 = load_image(player, 80, 16)
#    move_w = load_image(player, 48, 48)
#    move_w2 = load_image(player, 64, 48)
#    move_w3 = load_image(player, 80, 48)
#    move_s = load_image(player, 48, 0)
#    move_s2 = load_image(player, 64, 0)
#    move_s3 = load_image(player, 80, 0)