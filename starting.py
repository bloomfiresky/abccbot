import tkinter as tk
import os
import sqlite3


def hello1():

    root1.destroy()
def hallo():
    
    import botinno
    root1.destroy()
def hello():
    global t1
    global t2
    global t3
    t1=w2.get()
    t2=w7.get()
    t3=w6.get()
    hallo()


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "def.db")
    with sqlite3.connect(db_path) as db:
    #conn = sqlite3.connect('cse.db')
        cur = db.cursor()   
    cur.execute('SELECT name FROM users WHERE email = ?', (t2,))
    rows = cur.fetchall()   
    if len(rows) == 0:  
        cur.execute('INSERT INTO users VALUES(?, ?, ?)', (t1,t2,t3))
        db.commit()
        cur.close()
        db.close()
        hallo()

root1=tk.Tk()
root1.configure(bg="Hot Pink")
root1.state('zoomed')
w11=tk.Label(root1,text=" ",font=("Arial",30),bg="Hot Pink")
w11.pack(side="top")
w1=tk.Label(root1,text="NAME",font=("Arial",30))
w1.pack(side="top")
w2=tk.Entry(root1,bg="pink",fg="black",font=("Arial",30))
w2.pack(side="top")
w61=tk.Label(root1,text="EMAIL",font=("Arial",30))
w61.pack(side="top")
w7=tk.Entry(root1,bg="pink",fg="black",font=("Arial",30))
w7.pack(side="top")
w3=tk.Label(root1,text="PASSWORD",font=("Arial",30))
w3.pack(side="top")
w6=tk.Entry(root1,bg="pink",fg="black",font=("Arial",30),show="0")
w6.pack(side="top")
w4=tk.Button(root1,text="Submit",font=("Arial",30),command=hello)
w4.pack(side="top")
w41=tk.Label(root1,text=" ",font=("Arial",30),bg="Hot Pink")
w41.pack(side="top")
w5=tk.Button(root1,text="Close",font=("Arial",30),command=hello1)
w5.pack(side="top")
root1.mainloop()                                                                                                                                                                                                                                                                                                                   
