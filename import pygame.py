import pygame
import keyboard
from tkinter import *
from tkinter import ttk

   




pygame.init()
pygame.mixer.music.load("get_lucky.mp3")




def tocar_musica():
    pygame.mixer.music.play(1)
    
    
def parar_musica():
    pygame.mixer.music.pause()               
     
     
    
def despausar_musica(): 
    pygame.mixer.music.unpause() 
    
    
 
     
while True:
    while True: 
     if keyboard.is_pressed("space"):  
      tocar_musica()   
     break
     
     
    while True:
     if keyboard.is_pressed("b"):
        parar_musica()
     break
       
    while True:
     if keyboard.is_pressed("n"):   
        despausar_musica()
     break
     
   
    


              