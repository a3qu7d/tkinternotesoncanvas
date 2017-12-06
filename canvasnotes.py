#!/usr/bin/env python3
### Imports
import time
import tkinter as tk
from tkinter import N, E, W, S
from tkinter import ttk as ttk
import os
import tkinter.font
import re
#import sys
print("Hello, today's date is %s" % time.ctime())


### First steps
WIN_WIDTH = 1025
WIN_HEIGHT = 615
CURRENT_TEXTAREA = ""
CANVAS_5_NOTES_FOLDER_NAME = ".Canvas5Notes"
GAP = 16

def update_current_text_area(current_tagname):
    print("update_current_text_area called with value %s" % current_tagname)
    global CURRENT_TEXTAREA
    CURRENT_TEXTAREA = current_tagname
    print("CURRENT_TEXTAREA now has value %s" % current_tagname)
    statusvariable.set(CURRENT_TEXTAREA)

### files setup
#databasepath = "~" +  "/" + DATABASE_FOLDER_NAME + "/" + DATABASE_FILE_NAME
USER_HOME_DIR = os.path.expanduser('~')
file_path_p = USER_HOME_DIR +  "/" + CANVAS_5_NOTES_FOLDER_NAME + "/" + "p.txt"
file_path_o = USER_HOME_DIR +  "/" + CANVAS_5_NOTES_FOLDER_NAME + "/" + "o.txt"
file_path_i = USER_HOME_DIR +  "/" + CANVAS_5_NOTES_FOLDER_NAME + "/" + "i.txt"
file_path_u = USER_HOME_DIR +  "/" + CANVAS_5_NOTES_FOLDER_NAME + "/" + "u.txt"
#file_path_y = USER_HOME_DIR +  "/" + CANVAS_5_NOTES_FOLDER_NAME + "/" + "y.txt"

### gooey GUI setup
class customTextareaWidget(tk.Frame):
    def triggerupdate(self, event):
        self.bgFrame.configure(background="green", padx=2, pady=2)
        update_current_text_area(self.givenTagname)
    def focusoutupdate(self,event):
        self.bgFrame.configure(background="white")
    def setfont_ml(self,event):
        print("setfont_ml called")
        self.textarea.configure(font=self.font_ml, spacing1=2,spacing2=2,spacing3=2)
    def setfont_mh(self,event):
        print("setfont_mh called")
        self.textarea.configure(font=self.font_mh, spacing1=2,spacing2=2,spacing3=2)
    def returnsbreak_o(self, event):
        self.raise_and_fullscreen_focus_o
        return "break"

    def returnsbreak(self, event):
        return "break"

    def saveTextareaContent(self,event=None):
        print("Saving contents of %s" % self.givenTagname)
        data = self.textarea.get('1.0', tk.END+'-1c')
        if self.givenTagname == "p":
            outfile_p = open(file_path_p, "w")
            outfile_p.write(data)
            outfile_p.close()
            print("%s saved" % self.givenTagname )
        elif self.givenTagname == "o":
            outfile_o = open(file_path_o, "w")
            outfile_o.write(data)
            outfile_o.close()
            print("%s saved" % self.givenTagname )
        elif self.givenTagname == "i":
            outfile_i = open(file_path_i, "w")
            outfile_i.write(data)
            outfile_i.close()
            print("%s saved" % self.givenTagname )
        elif self.givenTagname == "u":
            outfile_u = open(file_path_u, "w")
            outfile_u.write(data)
            outfile_u.close()
            print("%s saved" % self.givenTagname )
        #elif self.givenTagname == "y":
        #    outfile_y = open(file_path_y, "w")
        #    outfile_y.write(data)
        #    outfile_y.close()
        #    print("%s saved" % self.givenTagname )

    def __init__(self, parent, providedTagname, providedcontent):
        tk.Frame.__init__(self, parent)
        self.configure(background='#fff', padx=1, pady=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.bgFrame = tk.Frame(self)
        self.bgFrame.configure(background="white", padx=1, pady=1)

        self.bgFrame.grid_rowconfigure(0, weight=1)
        self.bgFrame.grid_columnconfigure(0, weight=20)

        self.bgFrame.grid(row=0, column=0, sticky=N+E+W+S)

        self.givenTagname = providedTagname
        self.initialTextContent = providedcontent
        self.textarea = tk.Text(self.bgFrame, wrap=tk.WORD, padx=16, pady=16)
        self.textarea.grid(row=0, column = 0, sticky=N+E+W+S)
        self.textarea.insert(1.0, self.initialTextContent)

        self.vsb = tk.Scrollbar(self.bgFrame, orient="vertical", background='white', relief='flat', activebackground = 'green', activerelief='flat', troughcolor='white',  command=self.textarea.yview)

        self.vsb.grid(row=0, column=1, sticky=N+S)
        self.textarea.configure(yscrollcommand=self.vsb.set,
                            font=tkinter.font.Font(family="Bitstream Vera Sans Mono for Powerline", size=10),
                            spacing1=1,spacing2=1,spacing3=1,
                            bg='white',
                            borderwidth=0,
                            relief='flat'
                            )
        # textarea bind
        self.textarea.bind('<FocusIn>', self.triggerupdate)
        self.textarea.bind('<FocusOut>', self.focusoutupdate)
        self.textarea.bind('<Control-s>', self.saveTextareaContent)
        self.textarea.bind('<Alt-l>', self.setfont_ml)
        self.textarea.bind('<Alt-h>', self.setfont_mh)
        self.textarea.bind('<Control-o>', self.returnsbreak_o)
        self.textarea.bind('<Control-y>', self.returnsbreak)

        self.font_ml = tkinter.font.Font(family="Bitstream Vera Sans Mono for Powerline", size=8)
        self.font_mh = tkinter.font.Font(family="Bitstream Vera Sans Mono for Powerline", size=12)

class ShowNotes(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.configure(background="#fff", padx=12, pady=12)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.showNotesCanvas = tk.Canvas(self)
        self.showNotesCanvas.config(background="#00ee00")
        self.showNotesToolbar = tk.Frame(self)
        self.showNotesToolbar.config(background="#ace")
        #self.showNotesCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.showNotesCanvas.grid(row=0, column=0, sticky= N+S+E+W)

        self.showNotesToolbar.grid(row=1, column=0, sticky= E+W)
        self.simplelabel = tk.Label(self.showNotesToolbar, text="Toolbar : ", anchor=tk.NW, justify = tk.LEFT, background="#ace")
        self.simplelabel.config(font=("Merriweather", 12))
        self.simplelabel.grid(row=0, column=0, sticky=N+E+S+W)
        self.showNotesCanvas.bind("<Configure>", self.resize_shownotescanv)

    def rearrangeshownotescanv(self, event=None):
        print("Rearranging notes in canvas")
        currentheight = self.winfo_height()
        currentwidth = self.winfo_width()
        print("width : %s , height : %s" % ( currentwidth, currentheight))

    def resize_shownotescanv(self, e):
        self.rearrangeshownotescanv()

class Canvas5Notes(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background="#fff")

        self.canvasbgFrame = tk.Frame(self)
        self.canvasbgFrame.configure(background="#ace", padx=1, pady=1)
        self.canvasbgFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvasbgFrame.focus()

        self.mainBgFrameCanvas = tk.Canvas(self.canvasbgFrame)
        self.mainBgFrameCanvas.config(background="#fff")
        self.mainBgFrameCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #self.mainBgFrameCanvas.grid(row=0, column=0, sticky= N+S+E+W)
        self.mainBgFrameCanvas.bind("<Configure>", self.resize_canv)

        input_of_p_file = open(file_path_p, "r")
        text_of_p_file = input_of_p_file.read()
        input_of_p_file.close()
        self.widget_file_p = customTextareaWidget(self.mainBgFrameCanvas, "p", text_of_p_file )
        self.object_p = self.mainBgFrameCanvas.create_window(5,5, anchor=tk.NW, window=self.widget_file_p, width = 700, height = 200)

        input_of_o_file = open(file_path_o, "r")
        text_of_o_file = input_of_o_file.read()
        input_of_o_file.close()
        self.widget_file_o = customTextareaWidget(self.mainBgFrameCanvas, "o", text_of_o_file)
        self.object_o = self.mainBgFrameCanvas.create_window(5,215, anchor=tk.NW, window=self.widget_file_o, width = 700, height = 200)

        input_of_i_file = open(file_path_i, "r")
        text_of_i_file = input_of_i_file.read()
        input_of_i_file.close()
        self.widget_file_i = customTextareaWidget(self.mainBgFrameCanvas, "i", text_of_i_file)
        self.object_i = self.mainBgFrameCanvas.create_window(5,425, anchor=tk.NW, window=self.widget_file_i, width = 700, height = 200)

        input_of_u_file = open(file_path_u, "r")
        text_of_u_file = input_of_u_file.read()
        input_of_u_file.close()
        self.widget_file_u = customTextareaWidget(self.mainBgFrameCanvas, "u", text_of_u_file)
        self.object_u = self.mainBgFrameCanvas.create_window(5,425, anchor=tk.NW, window=self.widget_file_u, width = 700, height = 200)

        #input_of_y_file = open(file_path_y, "r")
        #text_of_y_file = input_of_y_file.read()
        #input_of_y_file.close()
        #self.widget_file_y = customTextareaWidget(self.mainBgFrameCanvas, "y", text_of_y_file)
        #self.object_y = self.mainBgFrameCanvas.create_window(5,425, anchor=tk.NW, window=self.widget_file_y, width = 700, height = 200)

    def rearrangeWindowsSimple(self,event=None):
        self.mainBgFrameCanvas.itemconfigure(self.object_p, state="normal")
        self.mainBgFrameCanvas.itemconfigure(self.object_o, state="normal")
        self.mainBgFrameCanvas.itemconfigure(self.object_u, state="normal")
        self.mainBgFrameCanvas.itemconfigure(self.object_i, state="normal")
        #self.mainBgFrameCanvas.itemconfigure(self.object_y, state="normal")
        print("Rearranging windows in Simple Layout")
        currentheight = self.winfo_height()
        currentwidth = self.winfo_width()
        print("width : %s , height : %s" % ( currentwidth, currentheight))
        widget_height = ( currentheight - ( 4 * GAP ) ) /  3
        widget_width = ( currentwidth - ( 3 * GAP ) ) / 2
        print("width : %s , height : %s" % ( widget_width, widget_height))
        self.mainBgFrameCanvas.itemconfig(self.object_p, width = widget_width, height = widget_height)
        self.mainBgFrameCanvas.coords(self.object_p, GAP, GAP)
        self.mainBgFrameCanvas.itemconfig(self.object_o, width = widget_width, height = widget_height)
        self.mainBgFrameCanvas.coords(self.object_o, GAP, (2 * GAP) + widget_height)
        self.mainBgFrameCanvas.itemconfig(self.object_i, width = widget_width, height = widget_height)
        self.mainBgFrameCanvas.coords(self.object_i, GAP, (3 * GAP) + ( 2 * widget_height))
        self.mainBgFrameCanvas.itemconfig(self.object_u, width = widget_width, height = (currentheight - (2 * GAP)))
        self.mainBgFrameCanvas.coords(self.object_u, ((2 * GAP) + widget_width), GAP )

    def resize_canv(self, e):
        self.rearrangeWindowsSimple()

    def raise_and_focus_p(self, e):
        self.widget_file_p.textarea.focus()
        print("Raise and focus p called.")

    def raise_and_fullscreen_focus_p(self, e):
        currentheight = self.winfo_height()
        currentwidth = self.winfo_width()
        print("width : %s , height : %s" % ( currentwidth, currentheight))
        self.mainBgFrameCanvas.itemconfigure(self.object_p, state="normal")
        self.mainBgFrameCanvas.tag_raise(self.object_p)
        self.mainBgFrameCanvas.itemconfigure(self.object_o, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_u, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_i, state="hidden")
        #self.mainBgFrameCanvas.itemconfigure(self.object_y, state="hidden")
        self.mainBgFrameCanvas.itemconfig(self.object_p, width = (currentwidth - ( 2 *  GAP)), height = currentheight - ( 2 * GAP))
        self.mainBgFrameCanvas.coords(self.object_p, GAP, GAP)
        self.widget_file_p.textarea.focus()
        print("Raise and fullscreen focus p called.")

    def raise_and_focus_o(self, e):
        self.widget_file_o.textarea.focus()
        print("Raise and focus o called.")

    def raise_and_fullscreen_focus_o(self, e):
        currentheight = self.winfo_height()
        currentwidth = self.winfo_width()
        print("width : %s , height : %s" % ( currentwidth, currentheight))
        self.mainBgFrameCanvas.itemconfigure(self.object_o, state="normal")
        self.mainBgFrameCanvas.tag_raise(self.object_o)
        self.mainBgFrameCanvas.itemconfigure(self.object_p, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_u, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_i, state="hidden")
        #self.mainBgFrameCanvas.itemconfigure(self.object_y, state="hidden")
        self.mainBgFrameCanvas.itemconfig(self.object_o, width = (currentwidth - ( 2 *  GAP)), height = currentheight - ( 2 * GAP))
        self.mainBgFrameCanvas.coords(self.object_o, GAP, GAP)
        self.widget_file_o.textarea.focus()
        print("Raise and fullscreen focus o called.")

    def raise_and_focus_i(self, e):
        self.widget_file_i.textarea.focus()
        print("Raise and focus i called.")

    def raise_and_fullscreen_focus_i(self, e):
        currentheight = self.winfo_height()
        currentwidth = self.winfo_width()
        print("width : %s , height : %s" % ( currentwidth, currentheight))
        self.mainBgFrameCanvas.itemconfigure(self.object_i, state="normal")
        self.mainBgFrameCanvas.tag_raise(self.object_i)
        self.mainBgFrameCanvas.itemconfigure(self.object_p, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_o, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_u, state="hidden")
        #self.mainBgFrameCanvas.itemconfigure(self.object_y, state="hidden")
        self.mainBgFrameCanvas.itemconfig(self.object_i, width = (currentwidth - ( 2 *  GAP)), height = currentheight - ( 2 * GAP))
        self.mainBgFrameCanvas.coords(self.object_i, GAP, GAP)
        self.widget_file_i.textarea.focus()
        print("Raise and fullscreen focus i called.")

    def raise_and_focus_u(self, e):
        self.widget_file_u.textarea.focus()
        print("Raise and focus u called.")

    def raise_and_fullscreen_focus_u(self, e):
        currentheight = self.winfo_height()
        currentwidth = self.winfo_width()
        print("width : %s , height : %s" % ( currentwidth, currentheight))
        self.mainBgFrameCanvas.itemconfigure(self.object_u, state="normal")
        self.mainBgFrameCanvas.tag_raise(self.object_u)
        self.mainBgFrameCanvas.itemconfigure(self.object_p, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_o, state="hidden")
        self.mainBgFrameCanvas.itemconfigure(self.object_i, state="hidden")
        #self.mainBgFrameCanvas.itemconfigure(self.object_y, state="hidden")
        self.mainBgFrameCanvas.itemconfig(self.object_u, width = (currentwidth - ( 2 *  GAP)), height = currentheight - ( 2 * GAP))
        self.mainBgFrameCanvas.coords(self.object_u, GAP, GAP)
        self.widget_file_u.textarea.focus()
        print("Raise and fullscreen focus u called.")

    #def raise_and_focus_y(self, e):
    #    self.widget_file_y.textarea.focus()
    #    print("Raise and focus y called.")

    #def raise_and_fullscreen_focus_y(self, e):
    #    currentheight = self.winfo_height()
    #    currentwidth = self.winfo_width()
    #    print("width : %s , height : %s" % ( currentwidth, currentheight))
    #    self.mainBgFrameCanvas.itemconfigure(self.object_y, state="normal")
    #    self.mainBgFrameCanvas.tag_raise(self.object_y)
    #    self.mainBgFrameCanvas.itemconfigure(self.object_p, state="hidden")
    #    self.mainBgFrameCanvas.itemconfigure(self.object_o, state="hidden")
    #    self.mainBgFrameCanvas.itemconfigure(self.object_i, state="hidden")
    #    self.mainBgFrameCanvas.itemconfigure(self.object_u, state="hidden")
    #    self.mainBgFrameCanvas.itemconfig(self.object_y, width = (currentwidth - ( 2 *  GAP)), height = currentheight - ( 2 * GAP))
    #    self.mainBgFrameCanvas.coords(self.object_y, GAP, GAP)
    #    self.widget_file_y.textarea.focus()
    #    print("Raise and fullscreen focus y called.")

class myStatusBar(tk.Frame):
    global statusvariable
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ace')
        self.simplelabel = tk.Label(self, text="Current : ", anchor=tk.NW, justify = tk.LEFT, background="#ace")
        self.simplelabel.config(font=("Merriweather", 12))
        self.simplelabel.grid(row=0, column=0, sticky=N+E+S+W)
        self.showCurrentRecord = tk.Label(self, textvariable=statusvariable, anchor=tk.NW, justify=tk.LEFT, wraplength=200)
        self.showCurrentRecord.config(font=("Merriweather", 12))
        self.showCurrentRecord.configure(background='#ace')
        self.showCurrentRecord.grid(row=0, column=1, sticky=N+E+S+W)


if __name__ == "__main__":
    #root = tk.Tk(className=sys.argv[0])
    root = tk.Tk(className="Canvas5Notes")
    root.geometry('1025x615')
    root.configure(background="#fff", padx=12, pady=12)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    statusvariable = tk.StringVar()
    statusvariable.set("Begin")
    mexa = Canvas5Notes(root)
    mexa.grid(row=0, column=0, sticky= N+S+E+W)
    mystb = myStatusBar(root)
    mystb.grid(row=1, column=0, sticky=E+W)
    #meviewer = ShowNotes(tab2frame)
    #meviewer.grid(row=0, column=0, sticky= N+S+E+W)
    root.bind('<Control-a>', mexa.rearrangeWindowsSimple)
    #root.bind('<Control-space>', mexa.getInputFromUser)
    root.bind('<Control-p>', mexa.raise_and_fullscreen_focus_p)
    root.bind('<Control-o>', mexa.raise_and_fullscreen_focus_o)
    root.bind('<Control-i>', mexa.raise_and_fullscreen_focus_i)
    root.bind('<Control-u>', mexa.raise_and_fullscreen_focus_u)
    #root.bind('<Control-Alt-y>', mexa.raise_and_fullscreen_focus_y)
    root.bind('<Alt-p>', mexa.raise_and_focus_p)
    root.bind('<Alt-o>', mexa.raise_and_focus_o)
    root.bind('<Alt-i>', mexa.raise_and_focus_i)
    root.bind('<Alt-u>', mexa.raise_and_focus_u)
    #root.bind('<Alt-y>', mexa.raise_and_focus_y)
    #root.bind('<Control-q>', mexa.saveAllReadyToQuit)
    #root.bind('<Control-q>', root.destroy)
    root.mainloop()
