#-*- coding:utf-8 -*-
'''
Created on 2019年5月24日

@author: 宛洛
'''
import pygame, sys,json
from pygame.locals import *
pygame.init()

def window():
    screen = pygame.display.set_mode(size=(500, 500))
    font = pygame.font.Font(None, 100)
    blue = 255, 255, 255
    txt = font.render("1", True, blue)
    x, y = 0, 0
    move=1
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT :
                sys.exit()
        screen.blit(txt, (x, y))
        x, y = move + x, y+2*move
        if x > 100 or x < 0 or y < 0 or y > 50:
            move = -move
        clock.tick(60)
        pygame.time.delay(1000)
        pygame.display.update()
import os
from ctypes.test.test_pickling import name

def readlines(dir=os.path.abspath('txt')):
    f=open(dir,"r",encoding="utf-8")
    data=f.readlines()
    for line in data:
        dict = json.loads(line)
        print(dict["html"])
    print('readlines(return list):'+dir)
    f.close
    return data
    
def story1():
    print('蛋疼小故事    \n')  
    name1 = input('what\'s your name ')  
    story = 'you are namenamename name na name,lalalla\n' + "dawd"
    story = story.replace('name', name1)
    print(story)
    
    
def write(txt,dir=os.path.abspath('txt')):
    with open(dir,'a',encoding="utf-8") as f:
        f.writelines(txt)
    print('writelines(list):'+dir)
    
def read(dir=os.path.abspath('txt')):
    f=open(dir,"r",encoding="utf-8")
    data=f.read()
    if data.startswith(u'\ufeff'):
        data = data.encode('utf8')[3:].decode('utf8')
    data=data.split('}')
    for lines in data:
        lines+='}'
        dict = json.loads(lines)
        print(dict["html"])
    print(dict["html"])
    print('readlines(return list):'+dir)
    f.close
    return data
    
read(r'C:\Users\onelor\AppData\Local\Programs\Python\Python37\myscrapy\img.txt')