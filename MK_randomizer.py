#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
import os, random, time

#TODO: Create directory if it does not exist
#TODO: Show list of exclusively txt/csv files in combobox
#TODO: Give option to import text files to copy to directory
#TODO: Deploy program

def play():
    '''Function to play item box jingle after button is clicked'''
    # Exit function if no input
    if combo.get() == '':
        return

    mixer.music.load('MK_item_box.wav')
    mixer.music.play()

def printRandomValue():
    '''Function to print randomly-selected lines until stopping at one at the
    end of the item box jingle.'''
    # Exit function if no input
    if combo.get() == '':
        return

    listfile = '{}/{}'.format(list_dir, combo.get())
    timeout = time.time() + 3
    while time.time() < timeout:
        root.update_idletasks()
        time.sleep(0.10)
        rand_line = random.choice(list(open(listfile)))
        #print(rand_line)
        rline['text'] = rand_line

# Create tkinter window
root = tk.Tk()
root.title('Item Box')
root.geometry('300x300')

# Initialize pygame
mixer.init()

# Create photoimage object to use item box image
photo = Image.open('item_box.png').resize((125,125))
photo = ImageTk.PhotoImage(photo)

# Set icon to photo
root.iconphoto(False, photo)

# List for option menu
list_dir = 'Text Files'
options = os.listdir(list_dir)

# Label widget in root window
tk.Label(
    root,
    text='Pick a list you want to randomize.',
).pack(side=tk.TOP, pady=10)

# Combobox to show list of options to select
selected_file = tk.StringVar()
combo = ttk.Combobox(root, values=options, textvariable=selected_file)
#combo.set('Pick an option.')
combo.pack(padx=10, pady=5)

# Button with photo
tk.Button(
    root,
    image=photo,
    bd=0,
    #command=lambda:[play, printRandomValue]
    #command=play
    command=lambda:[play(), printRandomValue()]
).pack(side=tk.TOP, pady=25)

# Label for output
rline = tk.Label(root)
rline.pack()

root.mainloop()