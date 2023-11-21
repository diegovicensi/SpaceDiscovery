from tkinter import simpledialog
import pygame
pygame.init()
tamanho = (1000,563) #tupla
branco = (255,255,255)
preto = (0,0,0)
pygame.display.set_caption("Space Marker")
fonte = pygame.font.Font("freesansbold.ttf", 20)
tela = pygame.display.set_mode ( tamanho )
gameIcon = pygame.image.load("spacee.png")
pygame.display.set_icon(gameIcon)
fundo = pygame.image.load("bg.jpg")
estrelas ={}
pygame.display.update()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            estrela = fonte.render(item, True, branco)
            tela.blit(estrela, (pos))
            pygame.draw.circle(tela, branco, pos, 20)
            pygame.display.update()
            if item == None:
                item = "desconhecido"+str(pos)
            estrelas[item] = pos
    tela.fill ( branco )
    tela.blit (fundo, (0,0))
    #pygame.draw.line(tela, preto, (1,1), (800,600), 2)

    
    pygame.display.update()
pygame.quit()