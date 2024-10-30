import pygame
import random

pygame.init()
pygame.display.set_caption("game of life")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

while True:
    clock.tick(60)
    event = pygame.event.get()


    for i in range(16):
        for j in range(16):
            counter=0
            if i <15 and map[i+1][j] == 1:
                counter+=1
            if j <15 and map[i][j+1] == 1:
                counter+=1
            if i <15 and j<15 and map[i+1][j+1] == 1:
                counter+=1
            if i <15 and j<15 and map[i+1][j-1] == 1:
                counter+=1
            if i <15 and map[i-1][j] == 1:
                counter+=1
            if i <15 and map[i][j-1] == 1:
                counter+=1
            if i <15 and j<15 and map[i-1][j+1] == 1:
                counter+=1
            if i <15 and j<15 and map[i-1][j-1] == 1:
                counter+=1
            if map[i][j] == 1 and counter<=1:
                map[i][j] = 0
                print("i died from lonliness")
            if map[i][j] == 1 and counter>=4:
                map[i][j] = 0
                print("i died from overpopulation")
            if map[i][j] == 0 and counter>1 and counter<4:
                map[i][j] = 1
                print("i am born!")

    


    for event in pygame.event.get():
        break

    

    pygame.time.wait(2000)

    screen.fill((0,0,0))
    for i in range(16):
        for j in range(16):
            if map[i][j]==0:
                pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                pygame.draw.rect(screen, (255,255,255), (j*50, i*50, 50, 50), 1)
            if map[i][j]==1:
                pygame.draw.rect(screen, (0,200,200), (j*50, i*50, 50, 50))
            

    pygame.display.flip()

pygame.quit()
