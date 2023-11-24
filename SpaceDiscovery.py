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


def abrir_caixa_de_pergunta(posicao):
    root = tk.Tk()
    root.withdraw()
    resposta = simpledialog.askstring("Pergunta", "Qual é o nome da estrela? ")
    if resposta is None or resposta.strip() == "":
        resposta = "desconhecido"
    resposta += f" ({posicao[0]}, {posicao[1]})"
    estrelas.append((posicao, resposta))

def desenhar_estrelas():
    for posicao, nome in estrelas:
        pygame.draw.circle(tela, (255, 255, 255), posicao, 5)
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (posicao[0] + 10, posicao[1] - 10))

def salvar_pontos_arquivo():
    with open("pontos.txt", "w") as arquivo:
        for posicao, nome in estrelas:
            arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")


def desenhar_linhas():
    if len(estrelas) >= 2:
        for i in range(len(estrelas) - 1):
            ponto1, nome1 = estrelas[i]
            ponto2, nome2 = estrelas[i+1]
            pygame.draw.line(tela, (255, 255, 255), ponto1, ponto2, 2)
            distancia = calcular_distancia(ponto1, ponto2)
            texto_distancia = f"Distância: {distancia:.2f}"
            fonte_distancia = pygame.font.Font(None, 20)
            texto_renderizado_distancia = fonte_distancia.render(texto_distancia, True, (255, 255, 255))
            posicao_texto_distancia = ((ponto1[0] + ponto2[0]) // 2, (ponto1[1] + ponto2[1]) // 2 - 10)
            tela.blit(texto_renderizado_distancia, posicao_texto_distancia)

def carregar_pontos_arquivo():
    try:
        with open("pontos.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")
                x = int(partes[0])
                y = int(partes[1])
                nome = ",".join(partes[2:])
                estrelas.append(((x, y), nome))
    except FileNotFoundError:
        pass

def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def excluir_marcacoes():
    estrelas.clear()
    


def jogo():
    branco = (255,255,255)
    preto = (0,0,0)
    fundo = pygame.image.load("bg.jpg")
    running = True
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(-1)
    fonte = pygame.font.Font(None, 25)
    f10 = "Pressione F10 para Salvar os pontos"
    f11 = "Pressione F11 para Carregar os pontos"
    f12 = "Pressione F12 para Deletar os pontos"
    texto_f10 = fonte.render(f10, True, branco)
    texto_f11 = fonte.render(f11, True, branco)
    texto_f12 = fonte.render(f12, True, branco)
    posicao_texto1 = (2, 2)
    posicao_texto2 = (345, 2)
    posicao_texto3 = (690, 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    abrir_caixa_de_pergunta(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    salvar_pontos_arquivo()
                elif event.key == pygame.K_F11:
                    carregar_pontos_arquivo()
                elif event.key == pygame.K_F12:
                    excluir_marcacoes()
                elif event.key== pygame.K_ESCAPE:
                    running = False
        


        tela.blit(fundo, (0,0))
        desenhar_linhas()
        desenhar_estrelas()
        tela.blit(texto_f10, posicao_texto1)
        tela.blit(texto_f11, posicao_texto2)
        tela.blit(texto_f12, posicao_texto3)
        pygame.display.update()
        clock.tick(60)







jogo()