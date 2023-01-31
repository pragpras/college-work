from tkinter import *
from tkinter import messagebox as mb
root=Tk()
def answer():
    if mb.askyesno("answer","is 2020 a leap year?"):
        mb.showinfo('answer','correct')
        exit()
    else:
        mb.showinfo('answer','incorrect')
        exit()

def callback():
    if mb.askyesno('verify','really quit?'):
        mb.showinfo('quit','goodbye')
        exit()
    else:
        mb.showinfo('no','good choice')

label=Label(root,text='would you like to answer a question?')
b1=Button(root,text='answer',command=answer).pack(fill='none')
b2=Button(root,text='quit',command=callback).pack(fill='none')
root.mainloop()