import pygame
import time
import random
import numpy as np
import winsound
from tkinter import *

bleu = [0,0,255]
rouge = [255,0,0]
vert = [0,255,0]
jaune =[255,255,0]
highscore = 0
high_mot = "_  _  _"

class carre:

    def __init__(self,color,position,freq):

        self.color = color
        self.position = position
        self.freq = freq



    def get_pressed(self,time_sound):

        winsound.Beep(self.freq,time_sound)


def game():

    global high_mot,highscore,jaune,bleu,rouge,vert

    dim_w= 400
    dim_c = int(0.35 *dim_w)
    dim_i = int( 0.1 * dim_w)
    time_ = 2000
    jouable = False

    c_b = carre(bleu,[dim_i,dim_i],150)
    c_j = carre(jaune,[dim_i, 2*dim_i + dim_c],200)
    c_v = carre(vert,[2*dim_i + dim_c, dim_i],250)
    c_r = carre(rouge, [2*dim_i + dim_c, 2* dim_i + dim_c],300)

    L_case = [c_b,c_v,c_j,c_r]
    running = True
    pygame.init()
    font = pygame.font.SysFont("comicsansms", 25)
    screen= pygame.display.set_mode((dim_w,dim_w))
    pygame.display.set_caption("")
    screen.fill((0,0,0))
    for case in L_case:
        pygame.draw.rect(screen,case.color,(case.position[0],case.position[1],dim_c,dim_c))
    pygame.display.update()
    N_tour = 1

    L_prop =[]
    L_rep = []

    while running:

        screen.fill((0,0,0))
        text = font.render(str(N_tour), True, (255,255,255))
        screen.blit(text,(int(dim_w/2) - text.get_width() // 2, 0))
        for case in L_case:
            pygame.draw.rect(screen,case.color,(case.position[0],case.position[1],dim_c,dim_c))
        pygame.display.update()


        if jouable == False:

            time_sound = int(time_ /N_tour)
            time.sleep(1)

            for case in L_rep:
                screen.fill((0,0,0))
                L_c =[c_b,c_v,c_j,c_r]
                L_c.remove(case)
                pygame.draw.rect(screen,color_bright(case.color),(case.position[0],case.position[1],dim_c,dim_c))
                for c in L_c:
                    c_nouv = color_dark(c.color)
                    pygame.draw.rect(screen,c_nouv,(c.position[0],c.position[1],dim_c,dim_c))
                pygame.display.update()
                case.get_pressed(time_sound)

            screen.fill((0,0,0))
            L_c =[c_b,c_v,c_j,c_r]
            r_c = random.sample(L_c,1)[0]
            L_rep.append(r_c)
            L_c.remove(r_c)
            r_c_col = color_bright(r_c.color)
            pygame.draw.rect(screen,r_c_col,(r_c.position[0],r_c.position[1],dim_c,dim_c))
            for c in L_c:
                c_nouv = color_dark(c.color)
                pygame.draw.rect(screen,c_nouv,(c.position[0],c.position[1],dim_c,dim_c))
            pygame.display.update()
            r_c.get_pressed(time_sound)

            jouable=True

        if jouable == True:




            event = pygame.event.get()
            for e in event:

                if e.type == pygame.MOUSEBUTTONDOWN:

                    mx,my =pygame.mouse.get_pos()

                    if mx> dim_i and mx < dim_i + dim_c and my > dim_i and my < dim_i + dim_c:

                        L_prop.append(c_b)
                        pygame.draw.rect(screen,color_bright(c_b.color),(c_b.position[0],c_b.position[1],dim_c,dim_c))

                        for case in [c_v,c_j,c_r]:

                            pygame.draw.rect(screen,color_dark(case.color),(case.position[0],case.position[1],dim_c,dim_c))
                        pygame.display.update()
                        c_b.get_pressed(time_sound)


                    if mx>dim_i and mx < dim_i + dim_c and  my > 2* dim_i + dim_c and my <  2* (dim_i + dim_c):

                        L_prop.append(c_j)
                        pygame.draw.rect(screen,color_bright(c_j.color),(c_j.position[0],c_j.position[1],dim_c,dim_c))

                        for case in [c_v,c_b,c_r]:

                            pygame.draw.rect(screen,color_dark(case.color),(case.position[0],case.position[1],dim_c,dim_c))
                        pygame.display.update()
                        c_j.get_pressed(time_sound)

                    if mx> 2*dim_i + dim_c and mx < 2* (dim_i + dim_c) and my > dim_i and my < dim_i + dim_c:

                        L_prop.append(c_v)
                        pygame.draw.rect(screen,color_bright(c_v.color),(c_v.position[0],c_v.position[1],dim_c,dim_c))

                        for case in [c_b,c_j,c_r]:

                            pygame.draw.rect(screen,color_dark(case.color),(case.position[0],case.position[1],dim_c,dim_c))
                        pygame.display.update()
                        c_v.get_pressed(time_sound)

                    if mx> 2*dim_i + dim_c and mx < 2* (dim_i + dim_c) and my > 2* dim_i + dim_c and my < 2* (dim_i + dim_c):

                        L_prop.append(c_r)
                        pygame.draw.rect(screen,color_bright(c_r.color),(c_r.position[0],c_r.position[1],dim_c,dim_c))

                        for case in [c_b,c_j,c_v]:

                            pygame.draw.rect(screen,color_dark(case.color),(case.position[0],case.position[1],dim_c,dim_c))
                        pygame.display.update()
                        c_r.get_pressed(time_sound)

                if e.type == pygame.QUIT:
                    if highscore < N_tour-1:
                        highscore = N_tour-1
                        high_mot = "    " +str(highscore)
                    pygame.quit()
                    running = False

            len_prop = len(L_prop)

            if len_prop != 0 and L_prop != L_rep[:len_prop]:

                if highscore < N_tour-1:
                    highscore = N_tour-1
                    high_mot = "    " +str(highscore)
                winsound.Beep(75,500)
                running = False
                pygame.quit()

            if L_prop == L_rep:
                time_ += time_*0.1
                N_tour +=1
                jouable=False
                L_prop =[]



            time.sleep(0.1)

def color_bright(color):
    col = ((255-color[0])/2,(255-color[1])/2,(255-color[2])/2)
    nouv_col = (col[0]+ color[0],col[1]+ color[1],col[2]+ color[2])
    return nouv_col


def color_dark(color):
    nouv_col = (color[0]/2, color[1]/2,color[2]/2)
    return nouv_col

def run_game(fenetre):

    fenetre.destroy()
    game()
    run()

def run():

    Menu=Tk()
    Menu.title('Menu')
    Menu.geometry('300x300')
    Menu['bg']='white'
    Play=Button(Menu,text='Jouer',bg='white', fg = 'black',font=("comicsansms", 40) , borderwidth = 0, command = lambda : run_game(Menu) )
    High=Label ( Menu , text = "Highscore = " + str(high_mot) , bg = 'white' , fg = 'black', font=("comicsansms", 20) )
    Play.place(x=25, y =140, width = 250, height = 100)
    High.place(x=30,y=40)
    Menu.mainloop()

if __name__ == '__main__':
    run()