#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from backend import *
import datetime
import os

gui = Tk()
gui.geometry("250x200")
gui.title("Sibyl")
def getWeather(param, cityName, backgroundLocation):
    now = datetime.datetime.now()
    name = now.strftime("%Y-%m-%d")
    where = filedialog.asksaveasfilename(initialdir = str(os.getcwd),title = "Select file",initialfile = (name),filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
    print(where)
    makeImage(param,where,cityName, backgroundLocation)
def changeBackground(obj):
    newBgLocation = filedialog.askopenfilename(initialdir = str(os.getcwd),title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    obj.delete(0,END)
    obj.insert(END, newBgLocation)
    return newBgLocation


def main():
    a = Label(gui ,text="City:").grid(row=0,column=0)
    b = Label(gui ,text="Background:").grid(row=3,column=0)
    c = Label(gui ,text="Font:").grid(row=6,column=0)
    param = Entry(gui)
    param.grid(row=1,column=0,)

    name = Entry(gui,text="assets/background.png")
    name.insert(END,"assets/background.png")
    name.grid(row=4,column=0)

    fontbox = ttk.Combobox(values = getFonts())
    fontbox.grid(row=7,column=0 )
    fontbox.set("Arial")
    change = Button(gui, text="Change Background", command=lambda : changeBackground(name))
    change.grid(row=5,column=0,pady=(0,10))
    getter = Button(gui, text="Get Weather",command=lambda : getWeather(makeCurrent(param.get()),param.get(),name.get()))
    getter.grid(row=2,column=0,pady=(0,10))

main()
gui.mainloop()
