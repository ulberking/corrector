from tkinter import *
import tkinter
from textblob import TextBlob
import textblob

def correct_word():
    obj = TextBlob(word1.get())
    corrected_word = obj.correct()
    word2.delete(0,END)
    word2.insert(10,corrected_word)

def clear_word():
    word1.delete(0,END)
    word2.delete(0,END)

if(__name__ == '__main__'):
    root = Tk()
    root.title('correcter')
    root.geometry('600x250')
    root.configure(background='lightgreen')
    header = Label(root, text='welcome to the word correcter',
                   bg='lightgreen', fg='black', font='Times 20 bold')
    header.grid(row=1, column=0)
    label1=Label(root, text='write the word',
                   bg='lightgreen', fg='black', font='Times 20 bold')
    label1.grid(row=2, column=0)
    word1=Entry()
    word1.grid(row=2,column=1)
    button1=Button(root,text='correct',bg='white',fg='black',command=correct_word)
    button1.grid(row=3,column=0)
    label2 = Label(root, text='corrected word word',
                   bg='lightgreen', fg='black', font='Times 20 bold')
    label2.grid(row=4, column=0)
    word2=Entry()
    word2.grid(row=4,column=1)
    button2=Button(root,text='clear',bg='white',fg='black',command=clear_word)
    button2.grid(row=5,column=0)
    root.mainloop()