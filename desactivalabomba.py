#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  tkinter import *
import time

root = Tk()
root.title("Desactiva la bomba")
root.geometry("490x650")

time_display = Label(root,width=58,height=4,bg="black")
time_display.place(x=11,y=33)
display = Entry(root,bg='gray70',width=10,font=('arial',19,'bold'))
display.place(x=163,y=100)

root.mainloop()
