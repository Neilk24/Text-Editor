from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

root = Tk()
root.title('Text Editor')
root.geometry('600x500')
root.rowconfigure(0, minsize=800,weight=1)
root.columnconfigure(1, minsize=800,weight=1)

def openfile():
    filepath=askopenfilename(
        filetype=[('Text File', '*.txt'), ('Python File', '*.py'), ('All Files', '*.*')])
    if not filepath:
            return
    text_edit.delete(1.0, END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
        input_file.close()
    root.title(f'Text Editor - {filepath}')

def savefile():
    filepath=asksaveasfilename(defaultextension='txt', 
        filetype=[('Text File', '*.txt'), ('Python File', '*.py'), ('All Files', '*.*')])
    if not filepath:
         return
    with open(filepath, 'w') as output_file:
        text = text_edit.get(1.0. END)
        output_file.write(text)
    root.title(f'Text Editor - {filepath}')

text_edit = Text(root)
fr_button = Frame(root, relief=RAISED, bd = 2)
button_save = Button(fr_button, text='save', command=savefile)
button_open = Button(fr_button, text='open', command=openfile)

button_open.grid(row = 0, column = 0, sticky='ew', padx = 5, pady = 5)
button_save.grid(row = 1, column = 0, sticky='ew', padx = 5, pady = 5)

fr_button.grid(row = 0, column = 0, sticky = 'ns')
text_edit.grid(row = 0, column = 1, sticky = 'nsew')

root.mainloop()