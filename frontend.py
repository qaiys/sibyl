#!/usr/bin/python
from tkinter import *
from tkinter import ttk
from backend import *
gui = Tk()
gui.geometry("500x500")
gui.title("Sibyl")

def getWeather(param):
    makeImage(param)


a = Label(gui ,text="City:").grid(row=0,column = 0)


weather = Label(gui,text='-')
weather.grid(row=6,column=1)

param = Entry(gui)
param.grid(row=1,column=0)

getter = Button(gui, text="Get Weather",command=lambda : getWeather(makeCurrent()).grid(row=5,column=0))
getter.grid(row=5,column=0)
gui.mainloop()
