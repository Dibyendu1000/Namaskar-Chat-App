from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from libs import firebase_insert
from libs import firebase_verify
from libs import home
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("500x400+0+0")
        self.root.iconbitmap("Chat App//images//namaste.ico")
        tabControl = ttk.Notebook(root) 
  
        tab1 = ttk.Frame(tabControl) 
        tab2 = ttk.Frame(tabControl) 
  
        tabControl.add(tab1, text ='Login') 
        tabControl.add(tab2, text ='Sign Up') 
        tabControl.pack(expand = 1, fill ="both")

        self.uname=StringVar()
        self.pass1_=StringVar()
        self.email1=StringVar()
        self.pass2_=StringVar()
        self.email2=StringVar()
        #=======Login Tab==========================================================
        title=ttk.Label(tab1,text="Login",font=("Berlin Sans FB",20,"bold"))
        title.place(x=220,y=0,relwidth=1)
        #L1=Label(self.root,bg="white",height=20,width=68)
        #L1.place(x=10,y=50)
        L2=Label(tab1,text="E-mail Id",font=("Berlin Sans FB",10,"bold"))
        L2.place(x=20,y=100)
        L2=Label(tab1,text="Password",font=("Berlin Sans FB",10,"bold"))
        L2.place(x=20,y=150)
        E1=Entry(tab1,width=50,textvariable=self.email1,relief=FLAT)
        E1.place(x=100,y=100)
        E2=Entry(tab1,show="*",width=50,textvariable=self.pass1_,relief=FLAT)
        E2.place(x=100,y=150)
        B1=Button(tab1,command=lambda: login(self.email1.get(),self.pass1_.get()),text="Login",width=20,height=2,relief=FLAT,font=("berlin sans fb",10,"bold"),bg="aqua")
        B1.place(x=170,y=200)
        #========Sign Up Tab========================================================
        title=ttk.Label(tab2,text="Sign Up",font=("Berlin Sans FB",20,"bold"))
        title.place(x=200,y=0,relwidth=1)
        #L1=Label(self.root,bg="white",height=20,width=68)
        #L1.place(x=10,y=50)
        L3=Label(tab2,text="User Name",font=("Berlin Sans FB",10,"bold"))
        L3.place(x=20,y=100)
        L4=Label(tab2,text="E-Mail Id",font=("Berlin Sans FB",10,"bold"))
        L4.place(x=20,y=150)
        L5=Label(tab2,text="Password",font=("Berlin Sans FB",10,"bold"))
        L5.place(x=20,y=200)
        E3=Entry(tab2,width=50,textvariable=self.uname,relief=FLAT)
        E3.place(x=100,y=100)
        E4=Entry(tab2,width=50,textvariable=self.email2,relief=FLAT)
        E4.place(x=100,y=150)
        E5=Entry(tab2,show="*",width=50,textvariable=self.pass2_,relief=FLAT)
        E5.place(x=100,y=200)
        B1=Button(tab2,command=lambda: signup(self.uname.get(),self.pass2_.get(),self.email2.get()),text="Sign Up",width=20,height=2,relief=FLAT,font=("berlin sans fb",10,"bold"),bg="aqua")
        B1.place(x=170,y=250)


def login(e,p):
    if(e=="" or p==""):
        messagebox.showerror("Error", "All Fields are necessary !!")
    else:
        res=firebase_verify.check(e,p)
        if(res[1]==0):
            messagebox.showerror("Error", "Invalid Email Id or Password !!")
        elif(res[1]==-1):
            messagebox.showerror("Error", "Internet might be disconnected !!")
        else:
            res=firebase_verify.check(e,p)
            if(res[-1]==0):
                messagebox.showerror("Error", "Invalid Email Id or Password !!")
            elif(res[-1]==-1):
                messagebox.showerror("Error", "Internet might be disconnected !!")
            else:
                root.destroy()
                home.profile(res[-2])
def signup(u,p,e):
    if(e=="" or u=="" or p==""):
        messagebox.showerror("Error", "All Fields are necessary !!")
    else:
        res=firebase_insert.push(u,e,p)
        if(res==0):
            messagebox.showerror("Error", "Email Id already exists try logging in !!")
        elif(res==-1):
            messagebox.showerror("Error", "Internet might be disconnected !!")
        elif(res==2):
            messagebox.showerror("Error", "Invalid Email Id  !!")
        else:
            messagebox.showinfo("Success","You have been successfully signed up, login to access !")
        

root=Tk()
obj=Login_System(root)
root.mainloop()