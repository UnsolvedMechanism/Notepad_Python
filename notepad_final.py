import tkinter as t
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

#setting up the window
root = t.Tk()
root.title('Notepad')
root.iconbitmap('notepad.ico')
root.geometry('800x600')
root.minsize(width = 300, height = 200)

#text area & scroll
scroll = t.Scrollbar(root)
scroll.pack(side = t.RIGHT,  fill = t.Y)
text = t.Text(root, yscrollcommand = scroll.set, bg = 'light yellow', fg = 'black', font = ('Calibri',14))
file = None
text.pack(expand = True, fill=t.BOTH)
scroll.config(command = text.yview)



#creating functions
dataS = ''
dataU = ''

def newFile() :
    global file
    root.title('Untitled notepad')
    file = None
    text.delete(1.0, t.END)

def openFile():
    global file
    file = t.filedialog.askopenfilename(defaultextension = '.txt', filetypes = [('All Files', '*.*'), ('Text documents','*.txt')])
    if file == '' :
        file = None
    else:
        root.title(os.path.basename(file)+'- Notepad')
        text.delete(1.0, t.END)
        f = open(file, 'r')
        text.insert(1.0, f.read())
        f.close()
    dataS = text.get(0.1, t.END)

def saveFile():
    global file
    
    if file == None:
        file=t.filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = '.txt', filetypes = [('All Files','*.*'),('Text Documents', '*.txt')])
        if file == '' :
            file = None
            
        else :
            f = open(file, 'w')
            f.write(text.get(1.0, t.END))
            f.close()
            root.title(os.path.basename(file) + '- Notepad')
    else :
        f = open(file, 'w')
        dataS = text.get(1.0, t.END)
        f.write(dataS)
        f.close()

    dataS = text.get(0.1, t.END)

def saveAsFile():
    global file
    file = t.filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = '.txt', filetypes = [('All Files','*.*'),('Text Documents', '*.txt')])
    f = open(file, 'w')
    f.write(text.get(1.0, t.END))
    f.close()
    root.title(os.path.basename(file) + '- Notepad')
    dataS = text.get(0.1, t.END)

def exitApp() :
    global file
    res = t.messagebox.askyesno('Notepad', 'Do you really want to exit ?')
    if res == True: 
        root.destroy()
            
def cut() :
    text.event_generate(('<<Cut>>'))

def copy() :
    text.event_generate(('<<Copy>>'))

def paste() :
    text.event_generate(('<<Paste>>'))

def about() :
    t.messagebox.showinfo('Notepad', 'Notepad by Yash Patil')

'''Creating menubar******************************************************'''
MenuBar = t.Menu(root)


#Creating File Menu
FileMenu = t.Menu(MenuBar, tearoff = 0)

FileMenu.add_command(label = 'New', command = newFile)
FileMenu.add_command(label = 'Open', command = openFile)
FileMenu.add_separator()

FileMenu.add_command(label = 'Save', command = saveFile)
FileMenu.add_command(label = 'Save As', command = saveAsFile)
FileMenu.add_separator()

FileMenu.add_command(label = 'Exit', command = exitApp)

MenuBar.add_cascade(label = 'File', menu = FileMenu)
#########################################################


#Creating Edit Menu
EditMenu = t.Menu(MenuBar, tearoff = 0)

EditMenu.add_command(label = 'Cut', command = cut)
EditMenu.add_command(label = 'Copy', command = copy)
EditMenu.add_command(label = 'Paste', command = paste)

MenuBar.add_cascade(label = 'Edit', menu = EditMenu)
#########################################################

#Creating help menu
HelpMenu = t.Menu(MenuBar, tearoff = 0)

HelpMenu.add_command(label = 'Info', command = about)

MenuBar.add_cascade(label = 'Help', menu = HelpMenu)
#########################################################
root.config(menu = MenuBar)
'''**********************************************************************'''

root.mainloop()
