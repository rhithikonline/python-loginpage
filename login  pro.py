from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("login")
root.geometry("400x200")

def login_ckeck():
    try:
        name =  entry1.get()
        password = entry2.get()
        if name == "rhithik" and password == "2006":
            #messagebox
            respones=messagebox.showinfo("message","login sucssessfull...!!")
            
        else:
            configlabel.config(text="'Your password ,usermane or both are wrong...!'")
    except ValueError:
        print("by")
#entry1 username
entry1 = Entry(bg="white",width=25)
entry1.place(x=130,y=20)
#label1
label1 = Label(root,text="username :",fg="blue")
label1.place(x=30,y=25)


#entry2 password
entry2 = Entry(bg="white",width=25)
entry2.place(x=130,y=60)
#label2
label2 = Label(root,text="password :",fg="blue")
label2.place(x=30,y=60)

#login button
login = Button(root,text="login" ,width=35 , command=login_ckeck)
login.place(x=30,y=100)

#label
configlabel = Label(root,fg="red",text="")
configlabel.place(x=30,y=140)


#mainloop
root.mainloop()
