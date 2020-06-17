import socket
from firebase import firebase
from tkinter import *
from datetime import datetime
#import json
#f=open(r'E:/Workplace/Chat App/data/chatlog.json','a')
firebase=firebase.FirebaseApplication("https://chat-data-c2e74.firebaseio.com/", None)
#stored=firebase.get("/chat-app-login/User",'',)
class Chat_system:
    def __init__(self,root,name,src):
        self.root=root
        self.root.title(name)
        self.root.geometry("500x400+0+0")
        self.root.iconbitmap("Chat App//images//namaste.ico")
        self.frame=Frame(self.root,height=15)
        self.frame.place(x=0,y=20,relwidth=1)
        self.msg=Listbox(self.frame,height=15, width=100,font=("Comic Sans MS",10,"bold"))
        #self.msg.place(x=0,y=20,relwidth=1)
        self.msg.pack(fill="both")
        scrollbar = Scrollbar(self.frame, orient="vertical")
        scrollbar.config(command=self.msg.yview)
        scrollbar.pack(side="right", fill="y")
        self.text=StringVar()
        self.chatbox=Text(self.root,width=47,height=40,relief=FLAT)
        self.chatbox.place(x=20,y=350)
        self.prev={}
        send=Button(self.root,command=lambda: self.sent(name,src),text="Send",width=20,height=2,relief=FLAT,font=("berlin sans fb",10,"bold"),bg="aqua")
        send.place(x=315,y=350)
        self.receive(name,src)
    def sent(self,name,src):
        self.snd_rcv(name,src)
        data={}
        source={}
        now = datetime.now()
        text=self.chatbox.get("1.0",END)
        t_string = now.strftime("%H:%M")
        source[src+"("+t_string+")"]=text
        data[name]=source
        result=firebase.post("/chat-data-c2e74/",data)
        self.snd_rcv(name,src)
        #firebase.post()
    def receive(self,name,src):
        chatlog=firebase.get("/chat-data-c2e74/",'')
        if(bool(chatlog)):
            for i in chatlog.keys():
                recv_for=list(chatlog[i].keys())[0]
                recv_from=list(chatlog[i][recv_for].keys())[0]
                               
                if(recv_for==name and recv_from[:-7]==src):                    
                    msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                    self.msg.insert(END,msg)
                    self.msg.itemconfig(END-1, {'fg':'red'})
                elif(recv_for==src and recv_from[:-7]==name):
                    msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                    self.msg.insert(END,msg)
            self.prev=chatlog
            
    def snd_rcv(self,name,src):
        chatlog=firebase.get("/chat-data-c2e74/",'')
        if(bool(chatlog)):
            for i in chatlog.keys():
                try:
                    if(chatlog[i]==self.prev[i]):
                        pass
                except KeyError:
                    recv_for=list(chatlog[i].keys())[0]
                    recv_from=list(chatlog[i][recv_for].keys())[0]
                    #print(recv_for,'=',name)
                    #print(recv_from,'=',src)
                    #print('outside')
                               
                    if(recv_for==name and recv_from[:-7]==src):                   
                        msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                        self.msg.insert(END,msg)
                        #self.msg.itemconfig(j, {'bg':'red'})
                        #print('inside')
                    elif(recv_for==src and recv_from[:-7]==name):
                        msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                        self.msg.insert(END,msg)
                        #self.msg.itemconfig(j, {'bg':'red'})
                        #print('inside')
            self.prev=chatlog
    

def message(name,src):
    
    root=Tk()
    obj=Chat_system(root,name,src)
    root.mainloop()