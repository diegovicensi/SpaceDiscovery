import pygame 
import random

pygame.init()
tamanho = (800,535) #tupla
pygame.display.set_caption("Game do Marcão")
branco = (255,255,255) #Tupla
clock = pygame.time.Clock()
preto = (0,0,0) #tuplha
fonte = pygame.font.Font("freesansbold.ttf", 25)
tela = pygame.display.set_mode ( tamanho )
fundo = pygame.image.load("Campo.png")
bola = pygame.image.load("bola.png")
goleiro = pygame.image.load("goleiro.png")
gols = 0
movYgoleiro = 200
movYbolinha = 245
posicaoXbolinha = 0
velXbolinha = 5
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                movYgoleiro = movYgoleiro + 5
            elif evento.key == pygame.K_UP:
                movYgoleiro = movYgoleiro -5

    
    tela.fill ( branco )
    tela.blit (fundo, (0,0))
    tela.blit (goleiro, (650,movYgoleiro))
    tela.blit (bola, (posicaoXbolinha,movYbolinha))    
    texto = fonte.render("Gols: " +str(gols), True, branco)
    tela.blit(texto, (10,2))

    #pygame.draw.circle(tela, preto, (posicaoXbolinha, 300), 20)      #circulo
    if posicaoXbolinha <= 800:
        posicaoXbolinha = posicaoXbolinha + velXbolinha
    else:
        gols += 1
        posicaoXbolinha = 0
        #velXbolinha = velXbolinha + 5
        movYbolinha = random.randint(30,395)

    pygame.display.update()
    clock.tick(60)
    
    
    pygame.display.update()
pygame.quit()