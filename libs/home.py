import socket
from firebase import firebase
from tkinter import *
firebase=firebase.FirebaseApplication("https://chat-app-login.firebaseio.com/", None)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
try:
    stored=firebase.get("/chat-app-login/User",'')
except:
    print("Internet disconnected!")
class Home_System:
    def __init__(self,root,name):
        self.root=root
        self.root.title("Namaskar- Chat App")
        self.root.geometry("300x400+0+0")
        self.root.iconbitmap("Chat App//images//namaste.ico")
        title=Label(self.root,text="Welcome "+name.split()[0],font=("Berlin Sans FB",20,"bold"))
        title.place(x=10,y=0)
        head=Label(self.root,text="Contacts:",font=("Berlin Sans FB",15,"bold italic"))
        head.place(x=10,y=50)
        contacts=Listbox(self.root,font=("Comic Sans MS",10,"bold"))
        contacts.place(x=10,y=75)
        for i in stored:
            if(stored[i]['Name']==name):
                break
        del[stored[i]]
        j=1
        for i in stored:
            contacts.insert(j,stored[i]['Name'])
            j+=1
        chat=Button(self.root,command=None,text="Message...",width=20,height=2,relief=FLAT,font=("berlin sans fb",10,"bold"),bg="aqua")
        chat.place(x=120,y=350)

def Chat()

def profile(name):
    root=Tk()
    obj=Home_System(root,name)
    root.mainloop()
    