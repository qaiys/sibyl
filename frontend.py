#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from backend import *
import datetime
import os

gui = Tk()                  #some tkinter init stuff n that
gui.geometry("240x288")
gui.title("Sibyl")
gui.iconbitmap('assets/icon_qai_icon.ico') #I have that graphic design sauce 8)

def getWeather(param, cityName, backgroundLocation, error_log):
    error_log = error_log
    now = datetime.datetime.now()
    name = now.strftime("%Y-%m-%d")
    where = filedialog.asksaveasfilename(initialdir = '/',title = "Select file",initialfile = (name),filetypes = (("png files","*.png"),("all files","*.*")))

    if param != '':
        error_catcher = makeForecast(param,where,cityName, backgroundLocation)
    else:
        error_catcher = 5

    changeErrorLog(error_catcher,error_log)

def changeBackground(obj): #changes the background n that
    newBgLocation = filedialog.askopenfilename(initialdir = 'assets',title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
    obj.delete(0,END)
    obj.insert(END, newBgLocation)
    return newBgLocation

def changeErrorLog(error_number, obj): #all the possible errors (that we know of!) from the backend part.
    errors = {
        1: "Successfully saved file!",
        0: "Error: That file already exists\nRename it or delete the existing file",
        3: "Invalid API key",
        4: "Error: Nothing was saved\nCanceled before file was written",
        5: "Error: No city selected"
    }
    obj['text'] = errors.get(int(error_number))

def main(): #all the buttons n gui stuff n that

    a = Label(gui ,text="City:").grid(row=0,column=0)
    b = Label(gui ,text="Background:").grid(row=3,column=0)

    labelframe = LabelFrame(gui, text="Error Log:",width=100)
    labelframe.grid(row=8,column=0)
    e = Label(labelframe, text="", anchor='w')
    e.pack()

    param = Entry(gui)
    param.grid(row=1,column=0,)

    name = Entry(gui,text="assets/greenscreen.png")
    name.insert(END,"assets/greenscreen.png")
    name.grid(row=4,column=0)

    change = Button(gui, text="Change Background", command=lambda : changeBackground(name))
    change.grid(row=5,column=0,pady=(0,10))

    getter = Button(gui, text="Get Weather",command=lambda : getWeather(getForecast(param.get()),param.get(),name.get(),e))
    getter.grid(row=2,column=0,pady=(0,10))

main()
gui.mainloop()
