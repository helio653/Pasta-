import pygame
import random

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura_tela = 400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo 2D Simples")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Variáveis do jogador
largura_jogador = 50
altura_jogador = 60
x_jogador = (largura_tela // 2) - (largura_jogador // 2)
y_jogador = altura_tela - altura_jogador - 10
velocidade_jogador = 5

# Variáveis do obstáculo
largura_obstaculo = 50
altura_obstaculo = 50
x_obstaculo = random.randint(0, largura_tela - largura_obstaculo)
y_obstaculo = -altura_obstaculo
velocidade_obstaculo = 5

# Pontuação
pontuacao = 0

# Função para exibir texto na tela
fonte = pygame.font.SysFont(None, 35)

def mostrar_texto(texto, cor, x, y):
    tela_texto = fonte.render(texto, True, cor)
    tela.blit(tela_texto, [x, y])

# Função principal do jogo
def jogo():
    global x_jogador, y_obstaculo, x_obstaculo, velocidade_obstaculo, pontuacao
    rodando = True
    relogio = pygame.time.Clock()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimento do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and x_jogador > 0:
            x_jogador -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and x_jogador < largura_tela - largura_jogador:
            x_jogador += velocidade_jogador

        # Atualizar a posição do obstáculo
        y_obstaculo += velocidade_obstaculo

        # Verificar se o obstáculo saiu da tela
        if y_obstaculo > altura_tela:
            y_obstaculo = -altura_obstaculo
            x_obstaculo = random.randint(0, largura_tela - largura_obstaculo)
            pontuacao += 1
            velocidade_obstaculo += 0.5  # Aumenta a velocidade dos obstáculos

        # Verificar colisão
        if (y_obstaculo + altura_obstaculo > y_jogador and
            x_jogador < x_obstaculo + largura_obstaculo and
            x_jogador + largura_jogador > x_obstaculo):
            mostrar_texto("Game Over", vermelho, largura_tela // 3, altura_tela // 2)
            pygame.display.update()
            pygame.time.delay(2000)
            pontuacao = 0
            velocidade_obstaculo = 5
            y_obstaculo = -altura_obstaculo
            x_jogador = (largura_tela // 2) - (largura_jogador // 2)

        # Atualizar o fundo
        tela.fill(branco)

        # Desenhar o jogador
        pygame.draw.rect(tela, verde, [x_jogador, y_jogador, largura_jogador, altura_jogador])

        # Desenhar o obstáculo
        pygame.draw.rect(tela, vermelho, [x_obstaculo, y_obstaculo, largura_obstaculo, altura_obstaculo])

        # Exibir pontuação
        mostrar_texto(f"Pontuação: {pontuacao}", preto, 10, 10)

        # Atualizar a tela
        pygame.display.update()

        # Definir a taxa de quadros por segundo (FPS)
        relogio.tick(60)

# Executar o jogo
jogo()

# Encerrar o Pygame
pygame.quit()


