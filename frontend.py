#!/usr/bin/python
from tkinter import *
from tkinter import ttk
from backend import *
gui = Tk()
gui.geometry("800x500")
gui.title("Sibyl")
cities = {
    "ottawa": "45.4215, -75.6972",
    "toronto": "43.6532, -79.3832"
}


def getWeather(param,name,where,extension):
    makeImage(param,name,where,extension)


a = Label(gui ,text="City:").grid(row=0,column = 0)


weather = Label(gui,text='-')
weather.grid(row=6,column=1)

param = Entry(gui) 
param.grid(row=1,column=0)

name = Entry(gui)
name.grid(row=1,column=1)

where = Entry(gui)
where.grid(row=1,column=2)

extVar = StringVar()
extension = ttk.Combobox(gui,textvariable=extVar)
extension['values']=(".png",".jpeg",".tiff")
extension.grid(row=1,column=3)

getter = Button(gui, text="Get Weather",command=lambda : getWeather(makeCurrent(),name.get(),where.get(),extension.get()).grid(row=5,column=0))
getter.grid(row=5,column=0)
gui.mainloop()
