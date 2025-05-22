import tkinter as tk
from tkinter import *

win = Tk()
win.title('Calculator')

center_frame = Frame(win,bg='light gray',width=300,height=300)
center_frame.pack(expand=True)
center_frame.pack_propagate(False)

num=1
for i in range(3):
	for j in range(3):
		frame = Frame(center_frame,relief=FLAT)
		frame.grid(row=i,column=j,padx=4,pady=4)
		frame.grid_propagate(False)
		B1 = Button(frame,relief=RAISED,bg='black',text=f"{num}",fg='white',height=1,width=3)
		B1.pack(padx=5,pady=5,expand=True)
		num = num+1

B2 = Button(center_frame,text="ENTER",bg='red')
B2.pack(padx=2,pady=2)
B2.grid(row=2,column=3)




win.mainloop()