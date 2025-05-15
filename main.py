import pygame
from pygame.locals import *
from sys import exit
import sys
from random import uniform
import json
import os
import time
from main import *

import tkinter as tk
from tkinter import messagebox

def show_error_screen():
    messagebox.showerror("????????", "Você não devia ter feito isso...")
def show_error_screen2():
    messagebox.showerror("Erro Crítico", "O sistema encontrou uma falha crítica e precisa fechar o jogo. abra novamente em alguns instantes")
def mostrar_erro():
    show_error_screen()
    show_error_screen2()
# Criar a janela principal
root = tk.Tk()
root.withdraw()  # Ocultar a janela principal

# Exibir a mensagem de erro



# Fechar a janela principal
root.destroy()




def get_platform():
    if sys.platform.startswith('linux'):
         return 'linux' 
    elif sys.platform in ('win32', 'cygwin'): 
        return 'windows' 
    elif sys.platform == 'darwin': 
        return 'macos' 
    elif sys.platform == 'android': 
        return 'android' 
    else: 
        return 'unknown'
    
def get_path():
    global celular
    platform = get_platform()
    if platform == 'android':
        path = "/data/data/jean2011ofic.pingpong/files/app/"
        celular = True
    elif platform == 'linux':
        path = "./"
    else:
        path = "./"
    return path



current_path = get_path()
file_path = current_path + 'dados.json'

with open(file_path, 'r') as arquivo:
    dados = json.load(arquivo)



contador = 1
contador2 = 1

ja_fez = False

x_mouse = 0
y_mouse = 0


tocou = False
celular = False



y_player2 = 200



bola3_morreu = False
bola4_morreu = False
bola5_morreu = False

pygame.init()

rebateu2 = False

largula = 640
altura = 480
relogio = pygame.time.Clock()
y_player_principal = 200
x_player_principal = 60
x_bot = 570
y_bot = 60
x_bola = 310
y_bola = 240
x_move_bola = 0
y_move_bola = 0
bola_morreu = False
pontos = dados[0]['recorde']
recorde = dados[0]['recorde']
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largula, altura))
pygame.display.set_caption('ping pong')
jogo_nao_comecou = True
dificuldade = 'normal'
dificuldade_selecionada = 'a'
fonte2 = pygame.font.SysFont('arial', 18, True, True)
mensagem2 = 'precione a ou d para selecionar a dificuldade depois precione espaço'

texto_formatado2 = fonte2.render(mensagem2, True, (255,255,255))
ret_texto = texto_formatado2.get_rect()
vidas = 0
morreu = False
recorde = 0
rebateu = False
#dificuldade nightmare
nightmare_desbloqueado = dados[1]['nightmare']
cena_desbloqueo_nightmare = False
tela_desbloqueio_nightmare = 0

insano_desbloqueado = dados[2]['insano']
cena_desbloqueo_insano = False
tela_desbloqueio_insano = 0
# dificuldade glith     nome a pensar
glith_desbloqueado = dados[3]['glith']
cena_desbloqueo_glith = False
tela_desbloqueio_glith = 0

glith2_desbloqueado = dados[4]['glith2']
cena_desbloqueo_glith2 = False
tela_desbloqueio_glith2 = 1

glith3_desbloqueado = dados[5]['glith3']
cena_desbloqueo_glith3 = False
tela_desbloqueio_glith3 = 1

third_infernal_desbloqueado = dados[6]['third_infernal']
cena_desbloqueo_third_infernal = False
tela_desbloqueio_third_infernal = 1

second_infernal_desbloqueado = dados[7]['second_infernal']

super_especial_glith3 = False
super_especial_glith3_fase = 1

ticks_falso = 16

x_bola2 = 290
y_bola2 = 240
x_move_bola2 = 0
y_move_bola2 = 0
bola2_morreu = False

x_bola3 = 310
y_bola3 = 240
x_move_bola3 = 0
y_move_bola3 = 0

x_bola4 = 310
y_bola4 = 240
x_move_bola4 = 0
y_move_bola4 = 0

x_bola5 = 310
y_bola5 = 240
x_move_bola5 = 0
y_move_bola5 = 0

ticks = 19


def salvar_jogo():
    dados[0]['recorde'] = recorde
    dados[1]['nightmare'] = nightmare_desbloqueado
    dados[2]['insano'] = insano_desbloqueado
    dados[3]['glith'] = glith_desbloqueado
    dados[4]['glith2'] = glith2_desbloqueado
    dados[5]['glith3'] = glith3_desbloqueado
    dados[6]['third_infernal'] = third_infernal_desbloqueado
    dados[7]['second_infernal'] = second_infernal_desbloqueado
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def ir_para_proxima_dificudade():
                global dificuldade
                if second_infernal_desbloqueado:
                    if dificuldade == "third_infernal":
                        dificuldade = "second_infernal"
                if third_infernal_desbloqueado:
                    if dificuldade == 'glith3':
                        dificuldade = 'third_infernal'
                if dificuldade == 'glith2':
                    if glith3_desbloqueado:
                        dificuldade = 'glith3'
                if dificuldade == 'glith':
                    if glith2_desbloqueado:
                        dificuldade = 'glith2'
                if dificuldade == 'insano':
                    if glith_desbloqueado:
                        dificuldade = 'glith'
                if dificuldade == 'nightmare':
                    if insano_desbloqueado:
                        dificuldade ='insano'
                if dificuldade == 'hardcore':
                     if nightmare_desbloqueado:
                          dificuldade = 'nightmare'
                if dificuldade == 'dificil':
                            dificuldade = 'hardcore'
                if dificuldade == 'normal':
                            dificuldade = 'dificil'
                if dificuldade == '2_players':
                    dificuldade = 'normal'
                
def ir_para_dificuldade_anterior():
                global dificuldade
                if dificuldade == 'dificil':
                        dificuldade = 'normal'
                if dificuldade == 'normal':
                    dificuldade = '2_players'
                if dificuldade == 'hardcore':
                        dificuldade = 'dificil'
                if dificuldade =='nightmare':
                     dificuldade = 'hardcore'
                if dificuldade == 'insano':
                    dificuldade = 'nightmare'
                if dificuldade == 'glith':
                    dificuldade = 'insano'
                if dificuldade == 'glith2':
                    dificuldade = 'glith'
                if dificuldade == 'glith3':
                    dificuldade = 'glith2'
                if dificuldade == 'third_infernal':
                    dificuldade = 'glith3'
                if dificuldade == "second_infernal":
                    dificuldade = "third_infernal"

fase_third_infernal = 0
    
fase1_boss_third_infernal_som = 'sons/fase1_boss_third_infernal.wav'
dificuldade_third_acima = 'sons/dificuldade_third_e_acima_Dela.wav'

def tocar(som):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(som)
    pygame.mixer.music.play()

while True:  
    mensagem3 = f'dificulade:{dificuldade}'
    texto_formatado3 = fonte2.render(mensagem3, True, (255,255,255))
    ret_texto2 = texto_formatado3.get_rect()
    mensagem = f'pontos: {pontos}'#a mensagem q sera exibida
    texto_formatado = fonte.render(mensagem, True, (255, 255 ,255))
    mensagem4 = f'vidas: {vidas}'#a mensagem q sera exibida
    texto_formatado4 = fonte.render(mensagem4, True, (255, 255 ,255))
    relogio.tick(ticks)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            salvar_jogo()
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                ir_para_dificuldade_anterior()
                
                
            if event.key == K_d: 
                ir_para_proxima_dificudade()

              

            ticks = int(ticks)               
                
                
               

                
            if event.key == K_SPACE:
                
                if dificuldade_selecionada == 'a':
                    dificuldade_selecionada = dificuldade
                    jogo_nao_comecou = False
                    y_move_bola = 6
                    x_move_bola = 7
                    vidas = 4
                    if dificuldade_selecionada == 'hardcore':
                        vidas = 1
                    if dificuldade_selecionada == 'nightmare' or '2_players':
                        vidas = 1
                        y_move_bola = 8
                        x_move_bola = 14
                    if dificuldade_selecionada == 'insano':
                        vidas = 1
                        y_move_bola = 10
                        x_move_bola = 18
                    if dificuldade_selecionada == 'glith' or dificuldade_selecionada == 'glith2' or dificuldade_selecionada == 'glith3':
                        vidas = 1
                        y_move_bola = 11
                        x_move_bola = 19
                    if dificuldade_selecionada == 'glith3':
                        x_bola2 = largula//2
                        y_bola2 = altura//2
                        x_move_bola2 = 10
                        y_move_bola2 = 3
                    if dificuldade_selecionada == 'third_infernal':
                        vidas = 1
                        fase_third_infernal = 1
                        if fase_third_infernal == 1:
                            tocar(fase1_boss_third_infernal_som)
                            tocou = False


                    
                tela_desbloqueio_nightmare += 1
                tela_desbloqueio_insano += 1
                tela_desbloqueio_glith += 1
                tela_desbloqueio_glith2 += 1 
            
            if event.key == [K_u]:
                tela_desbloqueio_nightmare += 1
                tela_desbloqueio_insano += 1
                tela_desbloqueio_glith += 1
                tela_desbloqueio_glith2 += 1 
                    
            
        if dificuldade_selecionada == 'a':
             x_bola = largula//2
             y_bola = altura//2      
             y_player_principal =   altura//2

        x_mouse, y_mouse =  pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f'x mouse', x_mouse)
            pass
            # if celular: parte mobile

            #     if cena_desbloqueo_glith or cena_desbloqueo_glith2 or cena_desbloqueo_glith3 or cena_desbloqueo_insano or cena_desbloqueo_nightmare or cena_desbloqueo_third_infernal:
            #         tela_desbloqueio_nightmare += 1
            #         tela_desbloqueio_insano += 1
            #         tela_desbloqueio_glith += 1
            #         tela_desbloqueio_glith2 += 1 

            #     if sensor_mouse.colliderect(proxima_dificuldade):
            #         ir_para_proxima_dificludade()
            #     if sensor_mouse.colliderect(dificuldade_anterior):
            #         ir_para_dificuldade_anterior()
            #     if sensor_mouse.colliderect(selecionar_dificuldade):
            #         if dificuldade_selecionada == 'a':
            #             dificuldade_selecionada = dificuldade
            #             jogo_nao_comecou = False
            #             y_move_bola = 6
            #             x_move_bola = 7
            #             vidas = 4
            #             if dificuldade_selecionada == 'hardcore':
            #                 vidas = 1
            #             if dificuldade_selecionada == 'nightmare':
            #                 vidas = 1
            #                 y_move_bola = 8
            #                 x_move_bola = 14
            #             if dificuldade_selecionada == 'insano':
            #                 vidas = 1
            #                 y_move_bola = 10
            #                 x_move_bola = 18
            #             if dificuldade_selecionada == 'glith' or dificuldade_selecionada == 'glith2' or dificuldade_selecionada == 'glith3':
            #                 vidas = 1
            #                 y_move_bola = 11
            #                 x_move_bola = 19
            #             if dificuldade_selecionada == 'glith3':
            #                 x_bola2 = largula//2
            #                 y_bola2 = altura//2
            #                 x_move_bola2 = 10
            #                 y_move_bola2 = 3
            #             if dificuldade_selecionada == 'third_infernal':
            #                 vidas = 1

    
                    
    
    if celular:
        y_player_principal = y_mouse-50
                    

    if pygame.key.get_pressed()[K_w]:
        y_player_principal -= 60
    if pygame.key.get_pressed()[K_s]:
        y_player_principal += 60
    # if pygame.key.get_pressed()[K_]:
    #     if dificuldade_selecionada == '2_players':
    #         y_player2 += 60
    if not jogo_nao_comecou:
        y_bola += y_move_bola
        x_bola += x_move_bola
    if vidas <= 0:
        jogo_nao_comecou = True
        ja_fez = False
        dificuldade_selecionada = 'a'
        if recorde < pontos:
            recorde = pontos
        pontos = 0
        super_especial_glith3 = False
        x_bola3 = 310
        y_bola3 = 240
        x_move_bola3 = 0
        y_move_bola3 = 0

        x_bola4 = 310
        y_bola4 = 240
        x_move_bola4 = 0
        y_move_bola4 = 0

        x_bola5 = 310
        y_bola5 = 240
        x_move_bola5 = 0
        y_move_bola5 = 0
        contador = 1
        contador2 = 1
        bola3_morreu = False
        bola4_morreu = False
        bola5_morreu = False
        ja_fez = False
        super_especial_glith3_fase = 1

    cor_inimigoglit3 = (uniform(0,255),0,0)
         

    bot = pygame.draw.rect(tela, (255, 0 ,0), (x_bot, y_bola - 100, 50 , 300) )
    linha_do_meio = pygame.draw.line(tela, (255,255,0), (largula//2, 0), (largula//2, altura), 5)
    player_principal = pygame.draw.rect(tela, (255, 0 ,0), (x_player_principal, y_player_principal, 81 , 250) )

    if dificuldade_selecionada == 'nightmare':
         bot = pygame.draw.rect(tela, (255, 0 ,0), (x_bot, y_bola - 100, 50 , 300) )
         
    if dificuldade_selecionada == 'glith' or dificuldade_selecionada == 'insano' or dificuldade_selecionada == 'glith2':
         bot = pygame.draw.rect(tela, (255, 0 ,0), (x_bot, y_bola - 130, 80 , 300) )
    if dificuldade_selecionada == 'glith3':
        bot = pygame.draw.rect(tela, cor_inimigoglit3, (x_bot, y_bola - 130, 80 , 450) )
    if dificuldade_selecionada == 'third_infernal':
        bot = pygame.draw.rect(tela, (255,22,1), (x_bot, y_bola - 135, 80 , 450) )
    

    sensor_mouse = pygame.draw.rect(tela,(255,255,255), (x_mouse,y_mouse, 2,2) )

    




    ponto_especial = 10
    bola = pygame.draw.circle(tela, (242,190,100), (x_bola, y_bola), 15)
    #spectro_bola = pygame.draw.circle(tela, (2,190,100), (x_bola + x_move_bola, y_bola + y_move_bola), 15)
    if dificuldade_selecionada == 'glith3':
        bola2 = pygame.draw.circle(tela, (255,0,0), (x_bola2, y_bola2), 15)
        x_bola2 += x_move_bola2
        y_bola2 += y_move_bola2
    if super_especial_glith3:
        bola3 = pygame.draw.circle(tela, (100,0,100), (x_bola3, y_bola3), 15)
        bola4 = pygame.draw.circle(tela, (255,0,255), (x_bola5, y_bola4), 15)
        bola5 = pygame.draw.circle(tela, (255,200,0), (x_bola2, y_bola5), 15)

    
    
  
    if bola.colliderect(bot):
        if dificuldade_selecionada == "second_infernal":
            print("passou")
            pass
        print(f'vel_x =',x_move_bola)
        print(f'vel_y =',y_move_bola)
        rebateu = False
        if dificuldade_selecionada == 'glith3':
            if uniform(0,100) < 11:
                super_especial_glith3 = True
                print('ATIVADO')
        
        if not dificuldade_selecionada == 'third_infernal':
            y_move_bola = y_move_bola * -1
            x_move_bola = x_move_bola * -1
        elif dificuldade_selecionada == 'nightmare':
            y_move_bola *= -1.001
            x_move_bola *= -1.001
        elif dificuldade_selecionada == 'insano':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
            
        elif dificuldade_selecionada == 'glith':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
        elif dificuldade_selecionada == 'glith2':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
        elif dificuldade_selecionada == 'glith3':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
        if dificuldade_selecionada == 'third_infernal':
            x_move_bola *= -1
            y_move_bola *= -1
            if fase_third_infernal == 1:
                ticks *= 1.0070
                print(ticks)
            elif fase_third_infernal == 2:
                ticks *= 1.00140
                print(ticks)
            if pontos >= 12:
                x_move_bola = x_move_bola//1.5
                y_move_bola = y_move_bola//1.5
                fase_third_infernal = 2
                ticks -= 4
                pontos = 0
                if ticks < 15:
                    ticks = 14
                    if ticks_falso == 16:
                        ticks_falso = 15
                        print('falso')
                if ticks_falso <= 15:
                    ticks_falso -= 3
                    print(f'falso', ticks_falso)

                
            
        

        
        


        

                   
        if x_move_bola < 0:      #se dificuldade for = a normal o dificil
            x_move_bola -= uniform(0,2)
        else:
                x_move_bola += uniform(0,2)
        if y_move_bola < 0:
            y_move_bola -= uniform(0,2)
        else:
            y_move_bola += uniform(0,2)
        if dificuldade_selecionada == 'hardcore':
            if x_move_bola < 0:
                x_move_bola -= uniform(0,3)
            else:
                x_move_bola += uniform(0,3)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,3)
            else:
                y_move_bola += uniform(0,3)
        if dificuldade_selecionada == 'nightmare' or '2_players':
            if x_move_bola < 0:
                x_move_bola -= uniform(0, 4)
            else:
                x_move_bola += uniform(0,4)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,4)
            else:
                y_move_bola += uniform(0,4) 
        if dificuldade_selecionada == 'insano':
            if x_move_bola < 0:
                x_move_bola -= uniform(0, 5)
            else:
                x_move_bola += uniform(0,5)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,5)
            else:
                y_move_bola += uniform(0,5)
        if dificuldade_selecionada == 'glith':
            if x_move_bola < 0:
                x_move_bola -= uniform(0, 5)
            else:
                x_move_bola += uniform(0,5)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,5)
            else:
                y_move_bola += uniform(0,5)
        if dificuldade_selecionada == 'glith2':
            if x_move_bola < 0:
                x_move_bola -= uniform(0, 5)
            else:
                x_move_bola += uniform(0,5)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,5)
            else:
                y_move_bola += uniform(0,5)
        if dificuldade_selecionada == 'glith3':
            if x_move_bola < 0:
                x_move_bola -= uniform(0, 5)
            else:
                x_move_bola += uniform(0,5)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,5)
            else:
                y_move_bola += uniform(0,5)
    if dificuldade_selecionada == 'glith3':
        if bola2.colliderect(bot):
            x_move_bola2 *= -1.002
            y_move_bola2 *= -1.002
            x_bola2 = 540
    if dificuldade_selecionada == 'third_infernal':
        if bola.colliderect(bot):
            if x_move_bola < 0:
                x_move_bola -= uniform(0,0.9)
            else:
                x_move_bola += uniform(0,0.9)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,0.9)
            else:
                y_move_bola += uniform(0,0.9)
    if bola.colliderect(player_principal):
        rebateu = True
        if dificuldade_selecionada == 'normal' or 'dificil' or 'hardcore':
            y_move_bola = y_move_bola * -1
            x_move_bola = x_move_bola * -1

        elif dificuldade_selecionada == 'nightmare':
            y_move_bola = y_move_bola * -1.001
            x_move_bola = x_move_bola * -1.001
        elif dificuldade_selecionada == 'insano':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
        elif dificuldade_selecionada == 'glith':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
        elif dificuldade_selecionada == 'glith2':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
        elif dificuldade_selecionada == 'glith3':
            y_move_bola = y_move_bola * -1.002
            x_move_bola = x_move_bola * -1.002
        elif dificuldade_selecionada == 'third_infernal':
            y_move_bola = y_move_bola * -1
            x_move_bola = x_move_bola * -1
        if dificuldade_selecionada == 'third_infernal':
            if fase_third_infernal == 1:
                ticks *= 1.0070
                print(ticks)
            elif fase_third_infernal == 2:
                ticks *= 1.0140
                print(ticks)



        pontos += 1
        if dificuldade_selecionada == 'hardcore':
            if x_move_bola < 0:
                x_move_bola -= uniform(0,2)
            else:
                x_move_bola += uniform(0,2)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,2)
            else:
                y_move_bola += uniform(0,2)
        if dificuldade_selecionada == 'normal':
            if x_move_bola < 0:
                x_move_bola += 2
            else:
                x_move_bola -= 2
            if y_move_bola < 0:
                y_move_bola += 2
            else:
                y_move_bola -= 2
        if dificuldade_selecionada == 'dificil':
            if x_move_bola < 0:
                x_move_bola += 1
            else:
                x_move_bola -= 1
            if y_move_bola < 0:
                y_move_bola += 1
            else:
                y_move_bola -= 1
        if dificuldade_selecionada == 'nightmare' or '2_players':
            if x_move_bola < 0:
                x_move_bola -= uniform(0,3)
            else:
                x_move_bola += uniform(0,3)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,3)
            else:
                y_move_bola += uniform(0,3)
        if dificuldade_selecionada == 'insano':
            if x_move_bola < 0:
                x_move_bola -= uniform(0,3)
            else:
                x_move_bola += uniform(0,3)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,3)
            else:
                y_move_bola += uniform(0,3) 
        if dificuldade_selecionada == 'glith':
            if x_move_bola < 0:
                x_move_bola -= uniform(0,3)
            else:
                x_move_bola += uniform(0,3)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,3)
            else:
                y_move_bola += uniform(0,3)  
        if dificuldade_selecionada == 'glith2':
            if x_move_bola < 0:
                x_move_bola -= uniform(0,3)
            else:
                x_move_bola += uniform(0,3)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,3)
            else:
                y_move_bola += uniform(0,3)
        if dificuldade_selecionada == 'glith3':
            if x_move_bola < 0:
                x_move_bola -= uniform(0,3)
            else:
                x_move_bola += uniform(0,3)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,3)
            else:
                y_move_bola += uniform(0,3) 
    if dificuldade_selecionada == 'glith3':
        if bola2.colliderect(player_principal):
            x_move_bola2 *= -1.002
            y_move_bola2 *= -1.002 
            x_bola2 = 160
            pontos += 1
            rebateu2 = True
    if ticks >= 19:
        ticks_falso = 16

    if super_especial_glith3_fase >= 2:
        if bola3.colliderect(player_principal):
            x_move_bola3 *= -1.002
            y_move_bola3 *= -1.002 
            x_bola3 = 170
            pontos += 1
            bola3_morreu = True
        if bola4.colliderect(player_principal):
            x_move_bola4 *= -1.002
            y_move_bola4 *= -1.002 
            x_bola4 = 170
            pontos += 1
            bola4_morreu = True
        if bola5.colliderect(player_principal):
            x_move_bola5 *= -1.002
            y_move_bola5 *= -1.002 
            x_bola5 = 170
            pontos += 1
            bola5_morreu = True
    if x_bola3 >= largula:
            vidas -= 1
    if x_bola4 >= largula:
            vidas -= 1
    if x_bola5 >= largula:
            vidas -= 1
    if dificuldade_selecionada == 'third_infernal':
        if bola.colliderect(player_principal):
            if x_move_bola < 0:
                x_move_bola -= uniform(0,0.9)
            else:
                x_move_bola += uniform(0,0.9)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,0.9)
            else:
                y_move_bola += uniform(0,1) 
        if x_bola >= largula:
            bola_morreu = True
            x_bola = largula//2
            x_move_bola *= -1
            fase_third_infernal = 2
            ticks -=4
            print(f'perdeu, tick:', ticks)
            x_move_bola = x_move_bola//1.5
            y_move_bola = y_move_bola//1.5
            if ticks < 15:
                ticks = 14
                if ticks_falso == 16:
                    ticks_falso = 15
                    print('falso')
                if ticks_falso <= 15:
                    ticks_falso -= 4
                    print(f'falso', ticks_falso)
                tick = 14
    if ticks_falso <=0:
        second_infernal_desbloqueado = True
        salvar_jogo()
        time.sleep(1.5)
        pygame.quit()
        mostrar_erro()


        contador += 1
        print(contador)

        if contador >= 100:
            print("fduf")
    






                   
    if bola3_morreu and bola4_morreu and bola5_morreu:
        if dificuldade_selecionada =='glith3':
            super_especial_glith3 = False
            pontos += 100
            bola3_morreu = False
            bola4_morreu = False
            bola5_morreu = False
        



    if y_bola >= altura:
        y_move_bola *= -1
        if dificuldade_selecionada == 'insano':
            if y_move_bola < 0:
                y_move_bola -= uniform(0,2)
            else:
                y_move_bola += uniform(0,2)
            if y_move_bola < 0:
                y_move_bola -= uniform(0,2)
            else:
                y_move_bola += uniform(0,2) 
        
        
    if x_bola <= 0:
            vidas -= 1
            x_bola = largula//2
            y_bola = altura//2


    if y_bola <=2:
        y_move_bola = y_move_bola*-1


    if dificuldade_selecionada == 'glith':
        if y_bola < 0:
            x_bola = largula//2
            y_bola = altura//2
            x_move_bola *= -1
            y_move_bola *= -1
    
    if dificuldade_selecionada == 'glith2' or dificuldade_selecionada == 'glith3':
        if y_bola < 0:
            x_bola = largula//2
            y_bola = altura//2
            x_move_bola *= -1
            y_move_bola *= -0.9
        if y_bola > altura:
            x_bola = largula//2
            y_bola = altura//2
            x_move_bola *= -1
            y_move_bola *= -0.9
    if dificuldade_selecionada == 'glith3':
        if y_bola2 < 0:
            x_bola2 = largula//2
            y_bola2 = altura//2
            x_move_bola2 *= -1
            y_move_bola2 *= -1
        if y_bola2 > altura:
            x_bola2 = largula//2
            y_bola2 = altura//2
            x_move_bola2 *= -1
            y_move_bola2 *= -1
         

                    


    
    tela.blit(texto_formatado,(400,40))
    tela.blit(texto_formatado4,(100,40))
    if jogo_nao_comecou:
        # if not dificuldade_selecionada == 'third_infernal':
        #     pygame.mixer.music.stop()
        #     tela.fill((0,0,0))
        ticks = 19
        tela.fill((0,0,0))
        mensagem3 = f'Recorde:{recorde}'
        texto_formatado5 = fonte.render(mensagem3, True, (255,255,255))
        if dificuldade == 'third_infernal':
            tela.fill((255,0,0))

            if dificuldade == 'third_infernal':
                if tocou:
                    pass
                else:
                    tocar(dificuldade_third_acima)
                    print('tocou')
                    tocou = True
        else:
            pygame.mixer.music.stop()
            tocou = False
                



        tela.blit(texto_formatado5,(300,400))
        ret_texto.center = (largula//2, altura//2)
        tela.blit(texto_formatado2, ret_texto)
        ret_texto2.center = (largula//2, 220)
        tela.blit(texto_formatado3, ret_texto2)

        if celular == True:
            dificuldade_anterior = pygame.draw.rect(tela,(255,255,255), (100,100, 50,30))
            proxima_dificuldade = pygame.draw.rect(tela,(255,255,255), (500,100, 50,30))
            selecionar_dificuldade = pygame.draw.rect(tela,(0,255,255), (300,100, 90,40))




        pygame.display.flip


        pygame.display.update()


    if dificuldade_selecionada == 'glith3':
        if pontos > 17:
            third_infernal_desbloqueado = True

            print('njnjnj')
            salvar_jogo()
            pygame.quit()
            exit()

    if x_bola >= largula:
        if not nightmare_desbloqueado:
            if not cena_desbloqueo_nightmare:
                tela_desbloqueio_nightmare = 1
                cena_desbloqueo_nightmare = True
        if dificuldade_selecionada == 'nightmare':
            if not cena_desbloqueo_insano:
                cena_desbloqueo_insano = True
                tela_desbloqueio_insano = 1
        if dificuldade_selecionada == 'glith':
            cena_desbloqueo_glith2 = True
            tela_desbloqueio_glith2 = 1
        if dificuldade_selecionada == 'glith2':
            glith3_desbloqueado = True
        if dificuldade_selecionada == 'glith3':
            third_infernal_desbloqueado = True
            print('efefgg')
            salvar_jogo()
            pygame.quit()
            exit()
        if dificuldade_selecionada == 'insano':
            if not cena_desbloqueo_glith:
                cena_desbloqueo_glith = True
                tela_desbloqueio_glith = 1
        
    fonte3 = pygame.font.SysFont('arial', 58, True, True)
    mensagem5 = 'como voce conseguiu'
    texto_formatado6 = fonte3.render(mensagem5, True, (0,0,0))
    ret_texto3 = texto_formatado6.get_rect()
    mensagem6 = 'precione U para continuar'
    texto_formatado7 = fonte2.render(mensagem6, True, (0,0,0))
        
    mensagem7 = 'como'
    fonte4 = pygame.font.SysFont('arial', 150, True, True)
    texto_formatado8 = fonte4.render(mensagem7, True, (255,0,0))

    mensagem8 = 'pesadelo desbloqueado'
    fonte5 = pygame.font.SysFont('arial', 55, True, True)
    texto_formatado9 = fonte5.render(mensagem8, True, (255,0,0))
    #glith
    mensagem9 = 'glith desbloqueado'
    texto_formatado10 = fonte5.render(mensagem9, True, (255,0,0))
        
    mensageminsano = 'insano desbloqueado'
    texto_formatadoinsano = fonte5.render(mensagem9, True, (255,0,0))

    mensagemglith2 = 'glith2 desbloqueado'
    texto_formatadoglith2 = fonte5.render(mensagemglith2, True, (255,0,0))                  


         

         

    if cena_desbloqueo_nightmare:
    
        if tela_desbloqueio_nightmare == 1:
            tela.fill((255,255,255))
            tela.blit(texto_formatado6, ret_texto)
            tela.blit(texto_formatado7,(largula//2, 400))
            pygame.display.update()
        if tela_desbloqueio_nightmare == 2:
            tela.fill((255,255,255))
            tela.blit(texto_formatado8, (0, altura//2))
            pygame.display.update()
        if tela_desbloqueio_nightmare == 3:
             tela.fill((0,0,0))
             tela.blit(texto_formatado9,(0, altura//2))
             nightmare_desbloqueado = True
        if tela_desbloqueio_nightmare == 4:
            jogo_nao_comecou = True
            cena_desbloqueo_nightmare = False
            dificuldade_selecionada = 'a'
            if recorde < pontos:
                recorde = pontos
            pontos = 0
            dificuldade = 'nightmare'


    
    if cena_desbloqueo_insano == True:
        if tela_desbloqueio_insano == 1:
            tela.fill((255,255,255))
            tela.blit(texto_formatado6, ret_texto)
        if tela_desbloqueio_insano == 2 :
            tela.fill((0,0,0))
            tela.blit(texto_formatadoinsano,(0, altura//2))
            glith_desbloqueado_desbloqueado = True
        if tela_desbloqueio_insano == 3 :
            jogo_nao_comecou = True
            cena_desbloqueo_insano = False
            dificuldade_selecionada = 'a'
            if recorde < pontos:
                recorde = pontos
            pontos = 0
            insano_desbloqueado = True
            dificuldade = 'insano'

    

    if cena_desbloqueo_glith == True:
        if tela_desbloqueio_glith == 1:
            tela.fill((255,255,255))
            tela.blit(texto_formatado6, ret_texto)
        if tela_desbloqueio_glith == 2 :
            tela.fill((0,0,0))
            tela.blit(texto_formatado10,(0, altura//2))
            glith_desbloqueado_desbloqueado = True
        if tela_desbloqueio_glith == 3 :
            jogo_nao_comecou = True
            cena_desbloqueo_glith = False
            dificuldade_selecionada = 'a'
            if recorde < pontos:
                recorde = pontos
            pontos = 0
            glith_desbloqueado = True
            dificuldade = 'glith'

    if cena_desbloqueo_glith2 == True:
        if tela_desbloqueio_glith2 == 1:
            tela.fill((255,255,255))
            tela.blit(texto_formatado6, ret_texto)
        if tela_desbloqueio_glith2 == 2 :
            tela.fill((0,0,0))
            tela.blit(texto_formatadoglith2,(0, altura//2))
            glith_desbloqueado_desbloqueado = True
        if tela_desbloqueio_glith2 == 3 :
            jogo_nao_comecou = True
            cena_desbloqueo_glith2 = False
            dificuldade_selecionada = 'a'
            if recorde < pontos:
                recorde = pontos
            pontos = 0
            glith2_desbloqueado = True
            dificuldade = 'glith2'

    if not super_especial_glith3:
        if dificuldade == 'glith':
            if pontos%2 == 0 and pontos > 0 :
                if not rebateu:
                    y_bola = uniform(80,400)
        if dificuldade == 'glith2'or dificuldade_selecionada == 'glith3':
                if not rebateu:
                    y_bola = uniform(80,400)
        if dificuldade_selecionada == 'glith3':
            if not rebateu2:
                    y_bola2 = uniform(80,400)


    if super_especial_glith3:
        if super_especial_glith3_fase == 1:
            x_move_bola2 = 0
            y_move_bola2 = 0
            x_move_bola = 0
            y_move_bola = 0
            x_bola = 550
            y_bola = 240
            x_bola2 = 550
            y_bola2 = 210
            x_bola3 = 550
            y_bola3 = 180
            x_bola4 = 550
            y_bola4 = 150
            x_bola5 = 550
            y_bola5 = 120
            contador2 += 1
            if contador2 >- 100:
                super_especial_glith3_fase = 2

        #     super_especial_glith3_fase = 2
        if super_especial_glith3_fase >= 2:
            y_bola = uniform(1,479)
            y_bola2 = uniform(1,479)
            y_bola3 = uniform(1,479)
            y_bola4 = uniform(1,479)
            y_bola5 = uniform(1,479)
            x_bola3 += x_move_bola3
            x_bola4 += x_move_bola4
            x_bola5 += x_move_bola5

            contador += 1
            if contador >= 150:
                if not ja_fez:
                    x_move_bola = -100
                    x_move_bola2 = -100
                    x_move_bola3 = -1000
                    x_move_bola4 = -100
                    x_move_bola5 = -100
                    ja_fez = True


            
    pygame.display.flip()




