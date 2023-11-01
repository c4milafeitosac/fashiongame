import pygame
import sys

#Inicialização do Pygame
pygame.init()

#Configurações da tela
largura_janela = 720
altura_janela = 426
pygame.display.set_caption("Fashion Game")
clock = pygame.time.Clock()
fgExit = False
tela = pygame.display.set_mode((largura_janela, altura_janela))

#Carregando a imagem do personagem
personagemImg = pygame.image.load('bonecaa.png')
personagemImg = pygame.transform.scale(personagemImg, (200, 250))

#Carregando o cenário
cenario = pygame.image.load('cenario.jpg')
tela.blit(cenario, (0, 0))
pygame.display.update()

#Lista de imagens de roupas
roupas = [
    pygame.image.load('roupaa.png'),
    pygame.image.load('roupaadois.png'),
    pygame.image.load('roupaatres.png'),
    pygame.image.load('roupaaquatro.png'),
    pygame.image.load('roupaacinco.png')
]

#Redimensionando as imagens de roupas
for i in range(len(roupas)):
    roupas[i] = pygame.transform.scale(roupas[i], (120, 120))

#Posição inicial do personagem
x = (largura_janela * 0.1)
y = (altura_janela * 0.1)

#Velocidades iniciais do personagem
x_speed = 0
y_speed = 0

#Roupa atual selecionada
roupa_selecionada = None

#Loop principal do jogo
while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                roupa_selecionada = roupas[int(event.key) - pygame.K_1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
            if event.key == pygame.K_RIGHT:
                x_speed = 5
            if event.key == pygame.K_UP:
                y_speed = -5
            if event.key == pygame.K_DOWN:
                y_speed = 5

    x += x_speed
    y += y_speed

    #Limpa a tela e redesenha o cenário
    tela.blit(cenario, (0, 0))

    #Desenha o personagem na tela
    tela.blit(personagemImg, (28, 13))

    #Se uma roupa estiver selecionada, desenha a roupa na posição do personagem
    if roupa_selecionada is not None:
        tela.blit(roupa_selecionada, (x, y))

    #Atualiza a tela
    pygame.display.update()
    clock.tick(60)

#Encerra o jogo
pygame.quit()
sys.exit()
