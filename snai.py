import pygame
import random

# inicialização do pygame
pygame.init()

# dimensões da tela
largura = 500
altura = 500

# cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# criação da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")

# variáveis iniciais da cobra
tamanho_cobra = 20
x_cobra = largura / 2
y_cobra = altura / 2
velocidade_cobra = 5
movimento_x = 0
movimento_y = 0

# variáveis iniciais da comida
tamanho_comida = 20
x_comida = round(random.randrange(0, largura - tamanho_comida) / 10.0) * 10.0
y_comida = round(random.randrange(0, altura - tamanho_comida) / 10.0) * 10.0

# loop principal do jogo
jogo = True
while jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimento_x = -tamanho_cobra
                movimento_y = 0
            elif evento.key == pygame.K_RIGHT:
                movimento_x = tamanho_cobra
                movimento_y = 0
            elif evento.key == pygame.K_UP:
                movimento_y = -tamanho_cobra
                movimento_x = 0
            elif evento.key == pygame.K_DOWN:
                movimento_y = tamanho_cobra
                movimento_x = 0

    # atualização da posição da cobra
    x_cobra += movimento_x
    y_cobra += movimento_y

    # verifica se a cobra colidiu com as bordas da tela
    if x_cobra < 0 or x_cobra > largura - tamanho_cobra or y_cobra < 0 or y_cobra > altura - tamanho_cobra:
        jogo = False

    # desenha a cobra e a comida na tela
    tela.fill(branco)
    pygame.draw.rect(tela, vermelho, [x_comida, y_comida, tamanho_comida, tamanho_comida])
    pygame.draw.rect(tela, preto, [x_cobra, y_cobra, tamanho_cobra, tamanho_cobra])

    # verifica se a cobra colidiu com a comida
    if x_cobra == x_comida and y_cobra == y_comida:
        x_comida = round(random.randrange(0, largura - tamanho_comida) / 10.0) * 10.0
        y_comida = round(random.randrange(0, altura - tamanho_comida) / 10.0) * 10.0

    # atualiza a tela
    pygame.display.update()

    # define a velocidade da cobra
    pygame.time.Clock().tick(velocidade_cobra)

# encerra o pygame
pygame.quit()
