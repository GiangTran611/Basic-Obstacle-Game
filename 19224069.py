#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 00:22:12 2022

@author: trangiang
"""

import pygame
pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption('The Jumping Cooky')
blue = (0,191,255)
pink = (199, 21, 133)
red = (255,0,0)
background_x = 0
background_y = 0
Cooky_x = 0
Cooky_y = 190
Tata_x = 550
Tata_y = 185
RJ_x = 1100
RJ_y = 180
velocity_x = 5
velocity_y = 7
font1 = pygame.font.SysFont('san', 20)
font2 = pygame.font.SysFont('san', 40)

background = pygame.image.load('background.jpg')
Cooky = pygame.image.load('Cooky.png')
Tata = pygame.image.load('Tata.png')
RJ = pygame.image.load('RJ.png')
clock = pygame.time.Clock()
score = 0
jump = False
pausing = False
running = True
while running:
    clock.tick(60)
    screen.fill(blue)
    background1_rect = screen.blit(background, (background_x, background_y))
    background2_rect=screen.blit(background, (background_x+600, background_y))
    Cooky_rect = screen.blit(Cooky, (Cooky_x, Cooky_y))
    Tata_rect = screen.blit(Tata, (Tata_x, Tata_y))
    RJ_rect = screen.blit(RJ, (RJ_x, RJ_y))
    score_txt = font1.render("Score:" + str(score), True, pink)
    screen.blit(score_txt,(10,10))
    background_x -= velocity_x
    if background_x+600 <= 0:
        background_x = 0
        

    #running Tata    
    Tata_x -= velocity_x
    if Tata_x <= -600:
        Tata_x = 550 
        
    
    #running RJ
    RJ_x -= velocity_x
    if RJ_x <=-1200:
        RJ_x = 1100
        
        
   
    #When Cooky is jumping 
    if 190 >= Cooky_y>=0:
        if jump == True:
            Cooky_y -= velocity_y
            
    else:
        jump = False
    if Cooky_y < 190:
        if jump == False:
            Cooky_y += velocity_y

    
   #Cooky meets Tata
    if Cooky_rect.colliderect(Tata_rect):
        pausing = True
        gameover_txt = font2.render("GAME OVER", True, red)
        screen.blit(gameover_txt,(200, 100))
        result_txt = font1.render("Score: "+ str(score), True, red)
        screen.blit(result_txt, (255, 140))
        velocity_x = 0
        y_velocity = 0
        
    #Cooky meets RJ
    if Cooky_rect.colliderect(RJ_rect):
        pausing = True
        gameover_txt = font2.render("GAME OVER", True, red)
        screen.blit(gameover_txt,(200,100))
        result_txt = font1.render("Score: "+ str(score), True, red)
        screen.blit(result_txt, (255, 140))
        velocity_x = 0
        velocity_y = 0
    
    #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if Cooky_y == 190:
                    jump = True
                    score += 1
                if pausing:
                    background_x = 0
                    background_y = 0
                    Cooky_x = 0
                    Cooky_y = 190
                    Tata_x = 550
                    Tata_y = 185
                    RJ_x = 1100
                    RJ_y = 180
                    velocity_x = 5
                    velocity_y = 7
                    score = 0
                    pausing = False
                    
        
            
    pygame.display.flip()
pygame.quit()
      