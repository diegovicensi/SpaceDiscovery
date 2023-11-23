from tkinter import simpledialog
import tkinter as tk
import pygame
import math
pygame.init()
tamanho = (1000,563) #tupla
pygame.display.set_caption("Space Marker")
tela = pygame.display.set_mode ( tamanho )
gameIcon = pygame.image.load("spacee.png")
clock = pygame.time.Clock()
pygame.display.set_icon(gameIcon)
estrelas =[]
rodando = True
tela.fill ( branco )
tela.blit (fundo, (0,0))
primeiro = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            estrela = fonteEstrela.render(item, True, branco)
            tela.blit(estrela, (pos))
            if primeiro == True:
                anterior = pos
                primeiro = False
            else:
                pygame.draw.line(tela, branco, anterior, pos, 2)
                anterior = pos
            pygame.draw.circle(tela, branco, pos, 5)
            pygame.display.update()
            if item == None:
                item = "desconhecido"+str(pos)
            estrelas[item] = pos

    f10 = fonte.render("A salvar as marcações F10", True, branco)
    f11 = fonte.render("Carregar as marcações salvas F11", True, branco)
    f12 = fonte.render("Excluir todas as marcações F12", True, branco)
    tela.blit(f10, (10,2))
    tela.blit(f11, (300,2))
    tela.blit(f12, (650,2))
    #pygame.draw.line(tela, preto, (1,1), (800,600), 2)

    
    pygame.display.update()
pygame.quit()