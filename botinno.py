import csv
import re
import tkinter as tk
import threading
import cgi
import pyttsx3


   

a={}
with open(r"C:\Users\sravanti\Desktop\pakodi\cgi-bin/ab.csv") as filea:
    dean=csv.reader(filea,delimiter=',')
    next(dean)
    for row in dean:
        a[row[1]]=row[2]





root=tk.Tk()
root.configure(bg="Dark Violet")
root.state('zoomed')
def acha2():
    root.destroy()
                

timer1=threading.Timer(180.0,acha2)
timer1.start()
        

w1=tk.Label(root,text="Text with our AbcBot. Ask your query",font=("French Script MT" ,50),fg="Linen" ,bg="Dark Violet")
w1.pack()
w10=tk.Label(root,text=" ",bg="Dark Violet")
w10.pack()
w2=tk.Entry(root,font=40,bg="Linen")
w2.pack()
w10=tk.Label(root,text=" ",bg="Dark Violet").pack()




def hat():
    global w31
    global sr
    
    while True:
        
        msg1=w2.get()
        timer2=threading.Timer(30.0,acha1)
        timer2.start()
        
        
        
    
        msg=msg1 + ".*"
        for x in a.keys():
            match=re.search(msg,x,re.IGNORECASE)
            if(match):
                sr="BOT:"+a[x]
                break
                
        w31=tk.Label(root,text=sr,font=("Dosis",15),wraplength=250)
        w31.pack(side="top")
        engine=pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say(sr)
        engine.runAndWait()
        root.mainloop()
             
    
def acha1():
    global w2
    w31.pack_forget()
    w2.delete(0,'end')


w3=tk.Button(root,text="Send",font=40,fg="Midnight Blue", bg= "Linen",command=hat)
w3.pack()
            

        
        



