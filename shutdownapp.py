from tkinter import * 
import os 

def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")   

stapp=Tk() #create a instance or object of tkinter
stapp.title("Shut Down App")
stapp.geometry("2000x2000")
stapp.config(bg="Black")

r_buttton = Button(stapp,text="Restart",font=("Time New Roman",30,"bold"),command=shutdown,relief=RAISED,cursor="plus")
r_buttton.place(x=500,y=180,height=50,width=250)

st_buttton = Button(stapp,text="Shut Down",font=("Time New Roman",30,"bold"),command=restart,
relief=RAISED,cursor="plus")
st_buttton.place(x=500,y=100,height=50,width=250)
stapp.mainloop()
