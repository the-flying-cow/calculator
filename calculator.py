import tkinter as tk
from tkinter import *

win = Tk()
win.title('Calculator')

center_frame = Frame(win,bg='light gray',width=300,height=300)
center_frame.pack(expand=True)
center_frame.pack_propagate(False)

result_frame= Frame(win,bg='red',width=175,height=50)
result_frame.pack(expand=True)
result_frame.pack_propagate(False)
result_frame.place(x=680,y=250)

result_screen = Entry(result_frame,fg='white',bg='black',bd=10)
result_screen.pack(expand=True,fill='none')


def button_press(symbol):
	current  = result_screen.get()
	result_screen.delete(0,END)
	result_screen.insert(0,current+symbol)

def evaluate():
	value = result_screen.get()
	result = eval(value)
	result_screen.delete(0,END)
	result_screen.insert(0,result)

num=1
for i in range(3):
	for j in range(3):
		frame = Frame(center_frame,relief=FLAT,bg='white')
		frame.grid(row=i,column=j,padx=5,pady=5)
		frame.grid_propagate(False)
		num_str = str(num)
		B1 = Button(frame,relief=RAISED,bg='black',text=f"{num}",fg='white',height=1,width=3,command=lambda n=num_str:button_press(n))
		B1.pack(padx=2,pady=2,expand=True)
		num = num+1


B2 = Button(center_frame,text="=",bg='orange',command=lambda: evaluate())
B2.grid(row=2,column=3)

B3 = Button(center_frame,text="CLR",bg='sky blue',command=lambda: result_screen.delete(0,END))
B3.grid(row=0,column=3)

B_add = Button(center_frame,text="+",bg='light gray',command=lambda: button_press("+"))
B_add.grid(row=4,column=0)

B_sub = Button(center_frame,text="-",bg='light gray',command=lambda: button_press("-"))
B_sub.grid(row=4,column=1)

B_mul = Button(center_frame,text="*",bg='light gray',command=lambda: button_press("*"))
B_mul.grid(row=4,column=2)

B_div= Button(center_frame,text="/",bg='light gray',command=lambda: button_press("/"))
B_div.grid(row=4,column=3)

B_dec= Button(center_frame,text=".",bg='light gray',command=lambda: button_press("."))
B_dec.grid(row=1,column=3)

win.mainloop()