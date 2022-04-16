from tkinter import *
from tkinter import ttk,messagebox
import time
import os
from tkinter import font
class File_T:
    def __init__(self):
        self.title("File Based Record System by rb")  # type: ignore
        self.geometry("1350x700+0+0")  # type: ignore


        title=Label(self.root,text="File Based Record System", bd=10, relief=GROOVE,pady=10,font=("times new roman", 35 , "bold")).pack(fill=x)  # type: ignore
        Student_Frame=Frame(self.root,bd=10,relief=GROOVE)  # type: ignore
        Student_Frame.place(x=20,y=100,height=450)

        stitle=Label(Student_Frame,text="Employee Details", font=("times new roman", 30, "bold")).grid(row=0, columnspan=4,pady=20)


        #=====all variables=============
        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()


        lblsid=Label(Student_Frame, text="User ID"), font("times new roman",20,"bold")  # type: ignore
        lblsid.grid(row=1, column=0,pady=10,padx=20,sticky="w")  # type: ignore
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.s_id,relief=GROOVE,width=22,font="arial 15 bold").grid(row=1,column=1,padx=10,pady=10)

        lblsid=Label(Student_Frame,text="Contact"),font("times new roman",20,"bold").grid(row=1, column=2,pady=10,padx=20,sticky="w")  # type: ignore
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.contact,relief=GROOVE,width=22,font="arial 15 bold").grid(row=1,column=3,padx=10,pady=10)

        lblsid=Label(Student_Frame,text="Name"),font("times new roman",20,"bold").grid(row=2, column=0,pady=10,padx=20,sticky="w")  # type: ignore
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.name,relief=GROOVE,width=22,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        lblsid=Label(Student_Frame,text="Date(dd/mm/yyyy)"),font("times new roman",20,"bold").grid(row=2, column=2,pady=10,padx=20,sticky="w")  # type: ignore
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.date,relief=GROOVE,width=22,font="arial 15 bold").grid(row=2,column=3,padx=10,pady=10)

        lblsid=Label(Student_Frame,text="Course"),font("times new roman",20,"bold").grid(row=3, column=0,pady=10,padx=20,sticky="w")  # type: ignore
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.course,relief=GROOVE,width=22,font="arial 15 bold").grid(row=3,column=1,padx=10,pady=10)

        lblsid=Label(Student_Frame,text="Address"),font("times new roman",20,"bold").grid(row=4, column=0,pady=10,padx=20,sticky="w")  # type: ignore
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.address,relief=GROOVE,width=22,font="arial 15 bold").grid(row=4,column=0,padx=10,pady=10)

        lblsid=Label(Student_Frame,text="City"),font("times new roman",20,"bold").grid(row=5, column=0,pady=10,padx=20,sticky="w")  # type: ignore
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.city,relief=GROOVE,width=22,font="arial 15 bold").grid(row=5,column=1,padx=10,pady=10)

        lbldegree=Label(Student_Frame,text="Select Degree", font=("times new roman",20,"bold")).grid(row=3,column=2,pady=10,padx=20,sticky="w")
        lbldegree=Label(Student_Frame,text= "ID Proof", font=("times new roman",20,"bold")).grid(row=4,column=2,pady=10,padx=20,sticky="w")
        lbldegree=Label(Student_Frame,text="Payment Mode", font=("times new roman",20,"bold")).grid(row=5,column=2,pady=10,padx=20,sticky="w")

        idcombo=ttk.Combobox(Student_Frame,width=20,textvariable=self.degree,state="readonly",font="arial 15 bold")
        idcombo['values']={"PAN Card", "Driving Licence", "Adharcard", "Student id card"}
        idcombo.grid(row=4,column=3,padx=10,pady=10)

        paymentcombo=ttk.combobox(Student_Frame,width=20,textvariable=self.payment,state="readonly", font="arial 15 bold")  # type: ignore
        paymentcombo['values']=("cash","check","credit card","Net Banking")
        paymentcombo.grid(row=5,column=3,padx=10,pady=10)

        btnFrame=Frame(self.root,bd=10,relief=GROOVE)  # type: ignore
        btnFrame.place(x=10,y=570)

        btnsave=Button(btnFrame,text="Save",command=self.save_data,font="arial 15 bold", bd=7, width=18).grid
        btnlog=Button(btnFrame,text="Logout",command=self.logout,font="arial 15 bold", bd=7, width = 18)  # type: ignore
        btnexit=Button(btnFrame,text="Exit",command=self.exit_fun,font="arial 15 bold", bd=7, width = 18)  # type: ignore

        File_Frame=Frame(self.root,bd=10,relief=GROOVE)  # type: ignore
        File_Frame.place(x=1030,y=100,width=300,height=450)

        ftitle=Label(File_Frame,text="All files",font="arial 20 bold",bd=5,relief=GROOVE).pack(side=RIGHT,fill=Y)

        scroll_y=Scrollbar(File_Frame,orient=VERTICAL)
        self.file_list=Listbox(File_Frame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)  # type: ignore
        self.show_files()  # type: ignore
        self.root.mainloop()  # type: ignore
        
    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("error", "student id must be required ! !")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present == "Yes":
                    ask=messagebox.askyesno("Update","File already present \nDo you want to update id")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has Updated successfully")
                        self.show_files()  # type: ignore
                    else:
                        self.save_file()
                        messagebox.showinfo("Update", "Record has updated successfully")
                        self.show_files()  # type: ignore

    def save_file(self):
        f=open("files/"+str(self.s_id.get())+".txt","w")
        f.write(
            str(self.s_id.get())+","+
            str(self.name.get())+","+
            str(self.course.get())+","+
            str(self.address.get())+","+
            str(self.city.get())+","+
            str(self.contact.get())+","+
            str(self.date.get())+","+
            str(self.degree.get())+","+
            str(self.proof.get())+","+
            str(self.payment.get())+","
                )
        f.close()  # type: ignore

    def show_files(self):
        files=os.listdir("files/")
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)

    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        #print(self.file_list.get(get_cursor))
        f1=open("files/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")

        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])
        
    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")

    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("error","student id must be required !!")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present == "yes":
                    ask=messagebox.askyesno("Delete"," Do you really want to delete?")
                    if ask>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showerror("Success", "Deleted successfully")
                        self.show_files()
                    else:
                        messagebox.showerror("Error","File not found !")

    def exit_fun(self):
        ask=messagebox.askyesno("Exit", "Do you realy want to exit")
        if ask>0:
            self.root.destroy()  # type: ignore

    def logout(self):
        self.root.destroy()  # type: ignore
        import login
            
        



