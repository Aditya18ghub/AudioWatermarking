# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:43:21 2023

@author: ADITYA VENKATA
"""

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import *

from Audio_wm_lsb import LSB_Audiowm

root = Tk()



class Window(Frame):

    def __init__(self, master=None):
       
        Frame.__init__(self, master)
       
        self.master = master
      
     
        self.init_window()

 
    def init_window(self):
       
        self.master.title("Audio Watermarking using the LSB Encoding Technique")

       
        self.pack(fill=BOTH, expand=1)
        self.drawEnocoding()
        self.drawDecoding()

    def drawEnocoding(self):
      
        self.encodeVar = StringVar()
        self.encodelabel = Label(root, textvariable=self.encodeVar)
        self.encodelabel.place(x=10, y=10)
        self.encodeVar.set("ENCODING.")
       
        
        self.selectFileButton = Button(self, text="Select File  To Encode", command=self.selectFile)
        self.selectFileButton.place(x=10, y=100)

        self.var = StringVar()
        self.label = Label(root, textvariable=self.var, relief=RAISED)
        self.label.place(x=10, y=130)
      
        self.entryText = Entry(root)
        self.entryText.place(x=10, y=180)
        self.entryText.insert(0, "Enter the data to be encoded ")
       
        self.encodeButton = Button(self, text="Encode", command=self.encode)
      

        self.encodeButton.place(x=10, y=220)
     

      
        self.enocdedLocation = StringVar()
        self.locationOfEncodeFile = Label(root, textvariable=self.enocdedLocation)
        self.locationOfEncodeFile.place(x=10, y=280)

    def drawDecoding(self):
       
        self.decodeVar = StringVar()
        self.decodelabel = Label(root, textvariable=self.decodeVar)
        self.decodelabel.place(x=500, y=10)
        self.decodeVar.set("DECODING")

       
        self.selectFileDecodeButton = Button(self, text="Select  File To Decode ", command=self.selectFileDecode)
        self.selectFileDecodeButton.place(x=500, y=100)
       
        self.decodeFileVar = StringVar()
        self.decodeFileLabel = Label(root, textvariable=self.decodeFileVar, relief=RAISED)
        self.decodeFileLabel.place(x=500, y=140)

        self.decodeButton = Button(self, text="Decode", command=self.decode)
        self.decodeButton.place(x=500, y=200)
      
        self.decodedString = StringVar()
        self.decodedStringlabel = Label(root, textvariable=self.decodedString, font=(None, 40))
        self.decodedStringlabel.place(x=500, y=350)

    def client_exit(self):
        exit()

    def selectFile(self):
       
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select the file",
                                                   filetypes=(("WAV files", "*.wav"), ("all files", "*.*")))
        self.fileSelected = root.filename
        self.var.set(root.filename)

    def selectFileDecode(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select the file",
                                                   filetypes=(("WAV files", "*.wav"), ("all files", "*.*")))
        self.fileSelcetedForDecode = root.filename
        self.decodeFileVar.set(root.filename)

    def encode(self):
     
            perform = LSB_Audiowm()
      
            result = perform.enc_Audio(self.fileSelected, self.entryText.get())

            self.enocdedLocation.set(result)

    def decode(self):

            perform = LSB_Audiowm()

            result = perform.dec_Audio(self.fileSelcetedForDecode)
            self.decodedString.set(result)
            
            



root.geometry("1200x700")

app = Window(root)


root.mainloop()