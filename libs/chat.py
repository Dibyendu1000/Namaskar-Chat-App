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
        
        send=Button(self.root,command=lambda: self.sent(name,src),text="Send",width=20,height=2,relief=FLAT,font=("berlin sans fb",10,"bold"),bg="aqua")
        send.place(x=315,y=350)
        self.receive(name,src)
    def sent(self,name,src):
        self.receive(name,src)
        data={}
        source={}
        now = datetime.now()
        text=self.chatbox.get("1.0",END)
        print("it works")
        t_string = now.strftime("%H:%M")
        source[src+"("+t_string+")"]=text
        data[name]=source
        result=firebase.post("/chat-data-c2e74/",data)
        self.receive(name,src)
        #firebase.post()
    def receive(self,name,src):
        chatlog=firebase.get("/chat-data-c2e74/",'')
        if(bool(chatlog)):
            for i in chatlog.keys():
                recv_for=list(chatlog[i].keys())[0]
                recv_from=list(chatlog[i][recv_for].keys())[0]
                print(recv_for,'=',name)
                print(recv_from,'=',src)
                print('outside')
                #===========This Part of the code causes the error (It displays Nothing)===========               
                if(recv_for==name and recv_from[:-7]==src):                    
                    msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                    self.msg.insert(END,msg)
                    #self.msg.itemconfig(j, {'bg':'red'})
                    print('inside')
                elif(recv_for==src and recv_from[:-7]==name):
                    msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                    self.msg.insert(END,msg)
                    #self.msg.itemconfig(j, {'bg':'red'})
                    print('inside')
                #====================================================================================
                #The code works if the code is written as:
                '''if(recv_for==name):                    
                    msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                    self.msg.insert(END,msg)
                    #self.msg.itemconfig(j, {'bg':'red'})
                    print(src)'''
                #But that would be problem as if the if statement only verifies recv_for, then if other
                #users send message to receive for those messages will be received as well also this code
                #doesnot display messages from the other user and only displays my messages

                #Chatlog is of the form
                '''chatlog={'M9lF4JqHjKBZzaOzhfW':{'Subrata':{'Dibyendu Das(10:44)': "1234\n"}}
                         'M9lLQB4cQws0I_Y-mvM':{'Dibyendu Das':{'Subrata(11:12)':"hi\n"}}
                         }'''
            
    def snd_rcv(self,name,src):
        chatlog=firebase.get("/chat-data-c2e74/",'')
        if(bool(chatlog)):
            j=1
            for i in chatlog.keys():
                recv_for=list(chatlog[i].keys())[0]                
                if(recv_for==name):
                    recv_from=list(chatlog[i][recv_for].keys())[0]
                    msg=recv_from+':'+list(chatlog[i][recv_for].values())[0]
                    self.msg.insert(END,msg)
                    #self.msg.itemconfig(j, {'bg':'red'})
                    j+=1
    

def message(name,src):
    
    root=Tk()
    obj=Chat_system(root,name,src)
    root.mainloop()
