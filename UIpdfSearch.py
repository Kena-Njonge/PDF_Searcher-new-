#import packages
from email import message
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import LogicpdfSearch


def select_files():
    filetypes = (('PDF files', '.pdf'),)
    

    global message1 
    message1 = fd.askopenfilenames(
        title='Select file',
        initialdir='/',
        filetypes=filetypes)

    
    showinfo(
        title='Selected Files',
        message=message1
        )

def select_folder():
    global message2
    message2 = fd.askdirectory()

    showinfo(
        title='Selected Directory',
        message=message2
        )


def main():
    window.mainloop()

def fetchEntry():
    #fetch input, call pdf search and close window
    entry = entry_box1.get()
    input_path = message1[0]
    print(input_path)
    chosen_name = entry_box3.get()
    output_path = message2
    print(output_path)
    global Targetlist
    Targetlist = entry.split()
    LogicpdfSearch.textSearch(input_path, Targetlist, chosen_name, output_path)
    window.destroy()

#create window
window = Tk()
window.title("Pdf searcher")
#include icon
window.iconbitmap()
#add window elements and open window
label1=tk.Label (text= "Insert target words seperated by a blank space")
label2=tk.Label (text= "Select file")
label3=tk.Label (text= "Insert output file name")
label4=tk.Label (text= "Select output directory and press OK")
open_button1 = Button(
    window,
    text='Open Files',
    command=select_files
)
open_button2 = Button(
    window,
    text='Open Folder',
    command=select_folder
)
global entry_box1
global entry_box3
entry_box1 = tk.Entry()

entry_box3 = tk.Entry()
label1.pack()
entry_box1.pack()
label2.pack()
open_button1.pack(expand=True)
label3.pack()
entry_box3.pack()
label4.pack()
open_button2.pack(expand=True)
B = Button(text="OK", command=fetchEntry)
B.pack()
B1 = Button(text="Quit", command=window.destroy)
B1.pack()
main()


