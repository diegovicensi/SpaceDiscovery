import pygame   
pygame.init()
tamanho = (1000,563) #tupla
branco = (255,255,255)
preto = (0,0,0)
tela = pygame.display.set_mode ( tamanho )
fundo = pygame.image.load("bg.jpg")
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill ( branco )
    tela.blit (fundo, (0,0))
    #pygame.draw.line(tela, preto, (1,1), (800,600), 2)

    
    pygame.display.update()
pygame.quit()