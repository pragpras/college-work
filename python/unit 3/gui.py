from tkinter import *
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def add():
    f_n=e.get()
    global f_num
    global math 
    math="addition"
    f_num=eval(f_n)
    e.delete(0,END)
def sub():
    f_n=e.get()
    global f_num
    global math 
    math="subtraction"
    f_num=eval(f_n)
    e.delete(0,END)
def multi():
    f_n=e.get()
    global f_num
    global math 
    math="multiplication"
    f_num=eval(f_n)
    e.delete(0,END)
def div():
     f_n=e.get()
     global f_num
     global math 
     math="division"
     f_num=eval(f_n)
     e.delete(0,END)
def equal():
    s_num=eval(e.get())
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+s_num)
    if math=="subtraction":
        e.insert(0,f_num-s_num)
    if math=="multiplication":
        e.insert(0,f_num*s_num)
    if math=="division":
        e.insert(0,f_num/s_num)
bt1=Button(root,text="1",padx=40,pady=20,command=lambda:click(1)) #callback
bt2=Button(root,text="2",padx=40,pady=20,command=lambda:click(2))
bt3=Button(root,text="3",padx=40,pady=20,command=lambda:click(3))
bt4=Button(root,text="4",padx=40,pady=20,command=lambda:click(4))
bt5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5))
bt6=Button(root,text="6",padx=40,pady=20,command=lambda:click(6))
bt7=Button(root,text="7",padx=40,pady=20,command=lambda:click(7))
bt8=Button(root,text="8",padx=40,pady=20,command=lambda:click(8))
bt9=Button(root,text="9",padx=40,pady=20,command=lambda:click(9))
bt0=Button(root,text="0",padx=40,pady=20,command=lambda:click(0))
btadd=Button(root,text='+',padx=40,pady=20,command=add)
btsub=Button(root,text='-',padx=40,pady=20,command=sub)
btmul=Button(root,text='*',padx=40,pady=20,command=multi)
btdiv=Button(root,text='/',padx=40,pady=20,command=div)
bteq=Button(root,text='=',padx=140,pady=20,command=equal)
btcl=Button(root,text='AC',padx=80,pady=20,command=clear)
bt1.grid(row=1,column=0)
bt2.grid(row=1,column=1)
bt3.grid(row=1,column=2)
bt4.grid(row=2,column=0)
bt5.grid(row=2,column=1)
bt6.grid(row=2,column=2)
bt7.grid(row=3,column=0)
bt8.grid(row=3,column=1)
bt9.grid(row=3,column=2)
bt0.grid(row=4,column=0)
btcl.grid(row=4,column=1,columnspan=2)
bteq.grid(row=5,column=0,columnspan=4)
btadd.grid(row=1,column=3)
btsub.grid(row=2,column=3)
btmul.grid(row=3,column=3)
btdiv.grid(row=4,column=3)
root.mainloop()