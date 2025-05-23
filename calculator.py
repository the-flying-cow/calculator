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
		frame = Frame(center_frame,relief=FLAT,bg='white')
		frame.grid(row=i,column=j,padx=5,pady=5)
		frame.grid_propagate(False)
		B1 = Button(frame,relief=RAISED,bg='black',text=f"{num}",fg='white',height=1,width=3)
		B1.pack(padx=2,pady=2,expand=True)
		num = num+1

B2 = Button(center_frame,text="ENTER",bg='gray')
B2.pack(padx=2,pady=2)
B2.grid(row=2,column=3)

B_add = Button(center_frame,text="+",bg='light gray')
B_add.pack(padx=3,pady=3)
B_add.grid(row=4,column=0)

B_sub = Button(center_frame,text="-",bg='light gray')
B_sub.pack(padx=3,pady=3)
B_sub.grid(row=4,column=1)

B_mul = Button(center_frame,text="*",bg='light gray')
B_mul.pack(padx=3,pady=3)
B_mul.grid(row=4,column=2)

B_div= Button(center_frame,text="/",bg='light gray')
B_div.pack(padx=3,pady=3)
B_div.grid(row=4,column=3)

result_frame= Frame(win,bg='red',width=175,height=50)
result_frame.pack(expand=True)
result_frame.pack_propagate(False)
result_frame.place(x=680,y=250)

result_screen = Entry(result_frame,fg='white',bg='black',bd=10)
result_screen.pack(expand=True,fill='none')


win.mainloop()