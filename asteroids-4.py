# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'Imagens')

# Dados gerais do jogo.
WIDTH = 1000 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Classe Jogador que representa a nave
class Boneco(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, 'boneco pulando.png')).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (80,137 ))
        
        # Deixando transparente.

        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx =  WIDTH - 950 
        self.rect.bottom = HEIGHT - 65
        
        
        
        # Velocidade do boneco
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
        
        def bon_anim(self, center, boneco_anim):
            # Carrega a animação de explosão
            self.boneco_anim = boneco_anim
    
            # Inicia o processo de animação colocando a primeira imagem na tela.
            self.frame = 0
            self.image = self.boneco_anim[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
    
            # Guarda o tick da primeira imagem
            self.last_update = pygame.time.get_ticks()
    
            # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
            self.frame_ticks = 50
        def update(self):
        # Verifica o tick atual.
            now = pygame.time.get_ticks()
    
            # Verifica quantos ticks se passaram desde a ultima mudança de frame.
            elapsed_ticks = now - self.last_update
    
            # Se já está na hora de mudar de imagem...
            if elapsed_ticks > self.frame_ticks:
    
                # Marca o tick da nova imagem.
                self.last_update = now
    
                # Avança um quadro.
                self.frame += 1
    
                # Verifica se já chegou no final da animação.
                if self.frame == len(self.explosion_anim):
                    # Se sim, tchau explosão!
                    self.kill()
                else:
                    # Se ainda não chegou ao fim da explosão, troca de imagem.
                    center = self.rect.center
                    self.image = self.explosion_anim[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    # Metodo que atualiza a posição do boneco
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        

        # Mantem dentro da tela
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("PitFall")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 1.jpg')).convert()
background_rect = background.get_rect()


# Cria uma nave. O construtor será chamado automaticamente.
player = Boneco()

# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
         
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                if event.key == pygame.K_SPACE:
                    player.speedy = -10
              
                    
                    
        # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_SPACE:
                    if player.rect.bottom <= 700:
                        player.speedy = 10
                    if player.rect.bottom >= 1000:
                        player.speedy =0
                        
                  
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    
    pygame.quit()
