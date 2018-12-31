#!/usr/bin/python
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from backend import *
import datetime

gui = Tk()
gui.geometry("800x500")
gui.title("Sibyl")

def getWeather(param, cityName, backgroundLocation):
    now = datetime.datetime.now()
    name = now.strftime("%Y-%m-%d")
    where = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",initialfile = (name),filetypes = (("png files","*.png"),("all files","*.*")))
    print(where)
    makeImage(param,where,cityName, backgroundLocation)
def changeBackground():
def main():
    a = Label(gui ,text="City:").grid(row=0,column = 0)
    #b = Label(gui ,text="Image name:").grid(row=0,column = 1)
    #c = Label(gui ,text="File location:").grid(row=0,column = 2)
    #d = Label(gui ,text="File extension:").grid(row=0,column = 3)
    #weather = Label(gui)
    #weather.grid(row=6,column=1)



    param = Entry(gui)
    param.grid(row=1,column=0)

    name = Entry(gui,text="assets/background.png")
    name.insert(END,"assets/background.png")
    name.grid(row=1,column=1)

    #where = Entry(gui)
    #where.grid(row=1,column=2)

    #extVar = StringVar()
    #extension = ttk.Combobox(gui,textvariable=extVar)
    #extension['values']=(".png",".jpeg",".tiff")
    #extension.grid(row=1,column=3)
    change = Button(gui, text="Change Background", command=lambda : )
    getter = Button(gui, text="Get Weather",command=lambda : getWeather(makeCurrent(param.get()),param.get(),name.get()))
    getter.grid(row=5,column=0)

main()
gui.mainloop()
