import pyautogui
import os
import time
from tkinter import *
def window():
    root = Tk()
    root.title("Warning")
    w=Label(root, text=" The computer will shutdown after 5 seconds! \n Shit you can do about it")
    w.pack()
    button = Button(root, text='OK', width=25, command=root.destroy)
    button.pack()
    w = 250
    h = 100
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry('%dx%d+%d+%d' %(w,h,x,y))
    root.mainloop()

def accept():
    root =Tk()
    root.title("Success")
    w=Label(root, text="Congratulations!\nYou are authorized")
    w.pack()
    w = 250
    h = 100
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry('%dx%d+%d+%d' %(w,h,x,y))
    button = Button(root, text='OK', width=25, command=root.destroy)
    button.pack()
    root.mainloop
start_time=time.time()
a, b=pyautogui.size()
count=0
try:
    while True:
        if (time.time()-start_time < 15):
            x, y = pyautogui.position()
            if x>=0 and x<=5 and y>=0 and y<=5 and count==0:
                count+=1
            if x>=a-6 and x<=a-1 and y>=0 and y<=5 and count==1:
                count+=1
            if x>=a-6 and x<=a-1 and y>=b-6 and y<=b-1 and count==2:
                count+=1
            if x>=0 and x<=5 and y>=b-6 and y<=b-1 and count==3:
                accept()
                break
        else:
            window()
            break
except KeyboardInterrupt:
    print('\n')
