def executar_jogo():
    import pygame
    import random

    from code.const import COLOR_WHITE, COLOR_BLACK, WIN_WIDTH, WIN_HEIGHT

    pygame.init()
    pygame.mixer.init()  # Inicializa o mixer de som

    # Toca música de fundo (loop infinito)
    pygame.mixer.music.load('Russe.mp3')
    pygame.mixer.music.play(-1)

    # Posição do jogador
    x = 210
    y = 50
    speed = 30

    # Janela
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    # Imagens
    background = pygame.image.load('Level2bg.png')
    player = pygame.image.load('Player.png')
    enemy1_img = pygame.image.load('Inimigo1.png')
    enemy2_img = pygame.image.load('Inimigo2.png')
    enemy3_img = pygame.image.load('Inimigo3.png')

    timer = 0
    timer_sec = 0

    font = pygame.font.SysFont('arial black', 30)
    text = font.render("time: ", True, (COLOR_WHITE), (COLOR_BLACK))
    pos_text = text.get_rect()
    pos_text.center = (65,50)

    #Estrutura dos inimigos
    enemies = [
        {'x': random.randint(0, 200), 'y': 800, 'speed': 40, 'image': enemy1_img, 'respawn_delay': 10},
        {'x': random.randint(250, 500), 'y': 800, 'speed': 40, 'image': enemy2_img, 'respawn_delay': 10},
        {'x': random.randint(350, 600), 'y': 800, 'speed': 40, 'image': enemy3_img, 'respawn_delay': 10}
    ]

    window_open = True
    while window_open:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and x<= 360:
            x += speed
        if key[pygame.K_LEFT] and x >= 10:
            x -= speed

        #timer para ver o tempo de jogo
        if (timer <20):
            timer +=1
        else:
            timer_sec +=1
            text = font.render("Time: "+str(timer_sec),True, (COLOR_WHITE), (COLOR_BLACK))
            timer = 0

        # Atualiza cada inimigo individualmente
        for enemy in enemies:
            if enemy['respawn_delay'] > 0:
                enemy['respawn_delay'] -= 1
                continue

            enemy['y'] -= enemy['speed']

            # Saiu da tela? Renasce com novo X e delay diferente
            if enemy['y'] <= -100:
                enemy['y'] = 800
                enemy['x'] = random.randint(0, 200)
                enemy['respawn_delay'] = random.randint(10, 50)  # tempo aleatório de espera
            if abs(enemy['y'] - y) < 50 and abs(enemy['x'] - x) < 50:
                print("COLISÃO DETECTADA!")
                window_open = False
        # Desenha tudo
        window.blit(background, (0, 0))
        window.blit(player, (x, y))
        window.blit(text, pos_text)


        for enemy in enemies:
            if enemy['respawn_delay'] == 0:
                window.blit(enemy['image'], (enemy['x'], enemy['y']))

        pygame.display.update()

    pygame.quit()

