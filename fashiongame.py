import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_janela = 720
altura_janela = 426
pygame.display.set_caption("Fashion Game")
clock = pygame.time.Clock()
fgExit = False
tela = pygame.display.set_mode((largura_janela, altura_janela))

# Carregando a imagem do personagem
personagemImg = pygame.image.load('bonecaa.png')
personagemImg = pygame.transform.scale(personagemImg, (170, 250))

# Carregando o cenário
cenario = pygame.image.load('cenario.jpg')

# Lista de imagens de roupas
roupas = [
    pygame.image.load('roupaa.png'),
    pygame.image.load('roupaadois.png'),
    pygame.image.load('roupaatres.png'),
    pygame.image.load('roupaaquatro.png'),
    pygame.image.load('roupaacinco.png')
]

# Redimensionando as imagens de roupas
for i in range(len(roupas)):
  roupas[i] = pygame.transform.scale(roupas[i], (100, 125))

# Posição inicial do personagem
x = (largura_janela * 0.1)
y = (altura_janela * 0.1)

# Velocidades iniciais do personagem
x_speed = 0
y_speed = 0

# Roupa atual selecionada
roupa_selecionada = None

# Estado do jogo
estado_jogo = "abertura"

# Loop principal do jogo
while not fgExit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      fgExit = True
    elif estado_jogo == "abertura" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
      # Se a tecla Enter for pressionada na tela de abertura, muda para o estado principal do jogo
      estado_jogo = "principal"

  if estado_jogo == "abertura":
    # Limpa a tela e redesenha o cenário
    tela.blit(cenario, (0, 0))

    # Desenha o nome do jogo na tela de abertura
    fonte_abertura = pygame.font.Font(None, 48)
    texto_abertura = fonte_abertura.render("Fashion Style - Jogo de Vestir",
                                           True, (255, 255, 255))
    tela.blit(texto_abertura,
              (largura_janela // 3 - texto_abertura.get_width() // 2.5,
               altura_janela // 3 - texto_abertura.get_height() // 2))

    # Atualiza a tela
    pygame.display.update()
  elif estado_jogo == "principal":
    # Lógica do jogo principal
    keys = pygame.key.get_pressed()
    if keys is not False:
      print(keys)

    for event in pygame.event.get():
      print(event)
      if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        roupa_selecionada = None  # Reseta a roupa selecionada ao pressionar Enter

      if event.type == pygame.KEYDOWN:
        print(event.key)
        if event.key == pygame.K_1:
          roupa_selecionada = roupas[0]
        elif event.key == pygame.K_2:
          roupa_selecionada = roupas[1]
        elif event.key == pygame.K_3:
          roupa_selecionada = roupas[2]
        elif event.key == pygame.K_4:
          roupa_selecionada = roupas[3]
        elif event.key == pygame.K_5:
          roupa_selecionada = roupas[4]

    # x += x_speed
    # y += y_speed

    # Posição da roupa em relação ao personagem
    roupa_x = 0
    roupa_y = 0

    # Se uma roupa estiver selecionada, desenha a roupa na posição do personagem
    if roupa_selecionada is not None:
      tela.blit(roupa_selecionada, (x + roupa_x, y + roupa_y))

    # Se uma roupa estiver selecionada, desenha a roupa na posição do personagem
    if roupa_selecionada is not None:
      tela.blit(roupa_selecionada, (x + roupa_x, y + roupa_y))

    # Lógica para atualizar a posição da roupa
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      roupa_x -= 5
    elif keys[pygame.K_RIGHT]:
      roupa_x += 5
    elif keys[pygame.K_UP]:
      roupa_y -= 5
    elif keys[pygame.K_DOWN]:
      roupa_y += 5

    # Limpa a tela e redesenha o cenário
    tela.blit(cenario, (0, 0))

    # Desenha o personagem na tela
    tela.blit(personagemImg, (x, y))

    # Se uma roupa estiver selecionada, desenha a roupa na posição do personagem
    if roupa_selecionada is not None:
      tela.blit(roupa_selecionada, (x + 40, y + 27))

    # Atualiza a tela
    pygame.display.update()
    clock.tick(60)

# Encerra o jogo
pygame.quit()
sys.exit()
