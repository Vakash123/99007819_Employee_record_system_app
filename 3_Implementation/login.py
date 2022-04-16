from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("File base Record System BY rb")
        self.root.geometry("1350x700+0+0")
        #-----------define Frame1
        F1=Frame(self.root,bd=10,relief=GROOVE)
        F1.place(x=450,y=150,height=350)
        #-------------defining variable
        self.user=StringVar()
        self.password=StringVar()
        #--------------defining title

        title=Label(F1, text="Login System", font=("times new roman",30,"bold")).grid(row=0,columnspan=2,pady=20)

        lblusername=Label(F1, text="Username",font=("times new roman",25,"bold")).grid(row=1,column=0,padx=10,pady=10)
        txtuser=Entry(F1,bd=7,relief=GROOVE,textvariable=self.user,width=25,font="arial 15 bold").grid(row=1,column=1,pady=10,padx=10)

        lblpass=Label(F1, text="Password",font=("times new roman",25,"bold")).grid(row=2,column=0,padx=10,pady=10)
        txtpass=Entry(F1,bd=7,relief=GROOVE,show="*",textvariable=self.password,width=25,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        #--------------creating button
        btnlog=Button(F1,text="Login",bd=7,width=10,command=self.logfun,font="arial 15 bold").place(x=10,y=250)
        btnreset=Button(F1,text="Reset",bd=7,width=10,command=self.reset,font="arial 15 bold").place(x=170,y=250)
        btnexit=Button(F1,text="Exit", bd=7, width=10, command= self.exit_fun,font="arial 15 bold").place(x=320,y=250)


    def logfun(self):
        if self.user.get()=="akash" and self.password.get()=="akash":
           self.root.destroy()
           import software
           software.File_T()
        else:
            messagebox.showerror("Error", "Invaid user name or password")

    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit_fun(self):
        option=messagebox.askyesno("Exit","Do you really want to exit ?")
        if option>0:
            self.root.destroy()
        else:
            return
    

root=Tk()
ob=Login(root)
root.mainloop()

    
    
