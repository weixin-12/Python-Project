# Data Analysis process by Weixin Liu(04100842)
# CST2101- Liu00529@algonquinlive.com

from tkinter.filedialog import askopenfilename
import os
import tkinter.messagebox
import re
from tkinter import *
from collections import Counter
import tkinter as tk

class Analysis():
     # ask the user input the filename
    def readtextfile(self):
        self.fpath = askopenfilename()
        self.fname = os.path.basename(self.fpath)
        self.ftype = os.path.splitext(self.fname)[1]
        print("get file name "+ self.fname)
        print("file type "+ self.ftype)
    
    # read from input file
    def readfile(self):
        with open(self.fpath,"r") as f:
            self.text = f.read()
        
    # Doing the analysis
    def counting(self):
        # count the blank
        self.countb = self.text.count(" ")
        print("Total blank character count:", self.countb)
        
        # count total character
        self.countc = 0
        for i in self.text:
            if i != " ":
                self.countc += 1
        print("Total Non-blank character:", self.countc)
        
        # Percentage of blank
        self.percent = float(self.countb/(self.countb+self.countc)*100)
        print('Percentage of blank characters:' + '%.2f' % self.percent + "%")
        
        # fingding the total words
        Replace = re.sub(r'\W', " ",self.text)
        Words = Replace.split(" ")
        self.countw = Counter(Words)
        del self.countw[" "]
        print("Total number of Words:", len(self.countw))
        print("dictionary:", self.countw)
    
    
    # get output file
    def Output(self):
        self.nfname = self.fname+"Analysis.txt"
        self.nfile = open(self.nfname, "w+")
        self.nfilepath = os.getcwd()
        self.nfile.write("Name of text: " + str(self.fname) + '\n')
        self.nfile.write("Total blank character count:" + str(self.countb)+'\n')
        self.nfile.write("Total Non-blank character:" + str(self.countc)+'\n')
        self.nfile.write("Percentage of blank characters:" + str('%.2f' % self.percent + "%")+'\n')
        self.nfile.write("Total number of Words:"+ str(len(self.countw)) + '\n')
        self.nfile.write("Dictionary: "+ '\n')
        for i in self.countw:
                    self.nfile.write(i + "---" + str(self.countw[i]) + '\n')
        self.nfile.close()
# Create interface


class Interface():
    def __init__ (self,window):
        
        #connect with class Analysis
        self.an = Analysis()
        self.an.fileName = ""
        
        # Design three labels and three button
        self.Label = Label(window, text="Data Analysis")
        self.Label.grid(row=0,column=1,sticky="n")
        self.Fname =Label(window, text="")
        self.Fname.grid(row=2,column=1)
        button1 = Button(window,text="Input", command = self.openfile)
        button1.grid(row=1,column=0,sticky="w")
        button2 = Button(window,text = "Output",command = self.start)
        button2.grid(row=3,column=3)
        self.Nflocation = Label(window,text = "Output file location:")
        self.Nflocation.grid(row=4,column=1,sticky="w")
        quit = Button(window,text="Exit",command = window.destroy)
        quit.grid(row=5,column=5)
    
        
    # Command for Input button 
    def openfile(self):
        self.an.readtextfile()
        self.Fname.config(text = self.an.fname)
        if self.an.ftype != ".txt":
            tk.messagebox.showinfo("warning","Please input the txt file!")
    # Command for Output button
    def start(self):
        self.an.readfile()
        self.an.counting()
        self.an.Output()
        self.Nflocation.config(text = self.an.nfilepath)
        tk.messagebox.showinfo("congratudation","Analysis is complete!")

        
# Display the interface when open the file

root =  Tk()
root.title("Data Analysis")
Project = Interface(root)
root.mainloop()


