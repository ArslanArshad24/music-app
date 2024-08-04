from tkinter import *
import pygame
import os

window=Tk()
window.geometry("800x400")
window.config(padx=70,pady=50,bg='yellow')

pygame.mixer.init()
n=0
def start_stop():
	global n
	n=n+1
	if n==1:
		song_name=songs_listbox.get()
		pygame.mixer.music.load(song_name)
		pygame.mixer.music.play(0)
		print("music started ")
	elif (n%2)==0:
 		pygame.mixer.music.pause()
 		print("paused ")
	elif (n%2)!=0:
		pygame.mixer.music.unpause()
		print("unPaused")

l1=Label(window,text="MUSIC PLAYER",font="times 20",fg='red')
l1.grid(row=0,column=0,pady=10,columnspan=2)

b2=Button(window,text='Start/Paused',width=20,command=start_stop,fg='green',bg='orange')
b2.grid(row=4,column=0,pady=10,padx=40)

songs_list=os.listdir()
songs_listbox=StringVar(window)
songs_listbox.set("Select Song",)
menu=OptionMenu(window,songs_listbox,*songs_list)
menu.grid(row=4,column=3,pady=10)

window.mainloop()