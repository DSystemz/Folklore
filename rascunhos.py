player = pygame.image.load("C:\ProjetinhoFellas\Folks\Folkore\Img\characters.png")
move_d = load_image(player, 48, 32)
move_d2 = load_image(player, 64, 32)
move_d3 = load_image(player, 80, 32)
move_a = load_image(player, 48, 16)
move_a2 = load_image(player, 64, 16)
move_a3 = load_image(player, 80, 16)
move_w = load_image(player, 48, 48)
move_w2 = load_image(player, 64, 48)
move_w3 = load_image(player, 80, 48)
move_s = load_image(player, 48, 0)
move_s2 = load_image(player, 64, 0)
move_s3 = load_image(player, 80, 0)

keys = pygame.key.get_pressed()
        self.rect.topleft = 490, 700
        self.atual = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.image = self.spritesA[self.atual]
                self.rect = self.image.get_rect()
                self.atual = self.atual + 1
                if self.atual >= len(self.spritesA):
                    self.atual = 0
                self.image = self.spritesA[self.atual]
                self.vel_x = -6

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.image = self.spritesD[self.atual]
                self.rect = self.image.get_rect()
                self.atual = self.atual + 1
                if self.atual >= len(self.spritesD):
                    self.atual = 0
                self.image = self.spritesD[self.atual]
                self.vel_x = 6

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.image = self.spritesW[self.atual]
                self.rect = self.image.get_rect()
                self.atual = self.atual + 1
                if self.atual >= len(self.spritesW):
                    self.atual = 0
                self.image = self.spritesW[self.atual]
                self.vel_y = -6

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.image = self.spritesS[self.atual]
                self.rect = self.image.get_rect()
                self.atual = self.atual + 1
                if self.atual >= len(self.spritesS):
                    self.atual = 0
                self.image = self.spritesS[self.atual]
                self.vel_y = 6

        if keys == pygame.KEYUP:
            if keys in [pygame.K_a, pygame.K_d]:
                self.vel_x = 0.0
            if keys in [pygame.K_s, pygame.K_w]:
                self.vel_y = 0.0


# MOVIMENTOS USADOS PARA SE MOVER PELO METODE DO ALEXANDRE CARVALHO
def moves():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            self.vel_x = 3.0
            self.image = self.lista_md[self.image_ind]
            self.image_ind += 1
            if self.image_ind >= len(self.lista_md):
                self.image_ind = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            self.vel_x = -3.0
            self.image = self.lista_ma[self.image_ina]
            self.image_ina += 1
            if self.image_ina >= len(self.lista_ma):
                self.image_ina = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            self.vel_y = -3.0
            self.image = self.lista_mw[self.image_inw]
            self.image_inw += 1
            if self.image_inw >= len(self.lista_mw):
                self.image_inw = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            self.vel_y = 3.0
            self.image = self.lista_ms[self.image_ins]
            self.image_ins += 1
            if self.image_ins >= len(self.lista_ms):
                self.image_ins = 0

    if event.type == pygame.KEYUP:
        if event.key in [pygame.K_a, pygame.K_d]:
            self.vel_x = 0.0
        if event.key == pygame.K_s:
            self.vel_y = 0.0
            self.image = self.lista_ms[self.image_ins]
            self.image_ins += 2
            if self.image_ins >= len(self.lista_ms):
                self.image_ins = 0

        if event.key == pygame.K_w:
            self.vel_y = -3.0
            self.image = self.lista_mw[self.image_inw]
            self.image_inw += 2
            if self.image_inw >= len(self.lista_mw):
                self.image_inw = 0

# colidindo com objetos e quebrando os mesmos

colisoes_obj = colisao_mapa(self, obj, ["a", "b", "z","f", "h", "t"])
        for colisao in colisoes_obj:
            print ("linha: {}  Coluna: {}  Caracter: {}".format(colisao["linha"], colisao["coluna"], colisao["caracter"]))
            linha = obj[colisao["linha"]]
            lista = list(linha)
            lista[colisao["coluna"]] = " "
            linha_texto = "".join(lista)
            obj[colisao["linha"]] = linha_texto

# Colisão da parte de cima e de baixo do mapa
clock = pygame.time.Clock()
clock.tick(30)
if self.rect.top < 0:
    self.rect.top = 0
elif self.rect.bottom > 750:
    self.rect.bottom = 750
elif self.rect.right


    player = pygame.image.load("C:\ProjetinhoFellas\Folks\Folkore\Img\characters.png")
    drawGroup = pygame.sprite.Group()

    hero = pygame.sprite.Sprite(drawGroup)
    move_s = load_image(player, 48, 0)  # 1
    move_s2 = load_image(player, 64, 0)  # 2
    move_s3 = load_image(player, 80, 0)  # 3
    hero.image = [move_s, move_s2, move_s3]
    image_ins = 1
    image = move_s
    hero.rect = pygame.Rect((32, 32), (block_width, block_height))
    grupo_heroi = pygame.sprite.Group(hero)


        self.lista_md = [move_d, move_d2, move_d3]
        self.image_ind = 1
        self.image = move_d
        self.rect = pygame.Rect((32, 32), (block_width, block_height))
          # 3
        self.lista_ma = [move_a, move_a2, move_a3]
        self.image_ina = 1
        self.image = move_a
        self.rect = pygame.Rect((32, 32), (block_width, block_height))
          # 3
        self.lista_mw = [move_w, move_w2, move_w3]
        self.image_inw = 1
        self.image = move_w
        self.rect = pygame.Rect((32, 32), (block_width, block_height))
          # 3
        self.lista_ms = [move_s, move_s2, move_s3]
        self.image_ins = 1
        self.image = move_s
        self.rect = pygame.Rect((32, 32), (block_width, block_height))

self.spritesA = []
self.spritesA.append(move_a)
self.spritesA.append(move_a2)
self.spritesA.append(move_a3)
self.spritesD = []
self.spritesD.append(move_d)
self.spritesD.append(move_d2)
self.spritesD.append(move_d3)
self.spritesW = []
self.spritesW.append(move_w2)
self.spritesW.append(move_w3)
self.spritesW.append(move_w)
self.spritesS = []
self.spritesS.append(move_s)
self.spritesS.append(move_s2)
self.spritesS.append(move_s3)

self.image = self.spritesW[self.atual]
self.rect = self.image.get_rect()
self.image = self.spritesA[self.atual]
self.rect = self.image.get_rect()
self.image = self.spritesS[self.atual]
self.rect = self.image.get_rect()
self.image = self.spritesD[self.atual]
self.rect = self.image.get_rect()