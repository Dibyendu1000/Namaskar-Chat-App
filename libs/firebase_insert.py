from firebase import firebase
import re
#import bcrypt

firebase=firebase.FirebaseApplication("https://chat-app-login.firebaseio.com/", None)
import re
#regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
regex='[^@]+@[^@]+\.[^@]+'
def check(email):
    if(re.search(regex,email)):  
        return 0           
    else:  
        return 1

def push(u,e,p):
        try:
            #salt=bcrypt.gensalt()
            #hashedpass=bcrypt.hashpw(p.encode(),salt)
            #hashedpass=hashedpass.decode()
            data={
            'Name':u,
            'Email':e,
            'Password':p
            }
            stored=firebase.get("/chat-app-login/User",'')
            if(not bool(stored)):
                result=firebase.post("/chat-app-login/User",data)
                return 1
            if(check(e)):
                return 2
            for i in stored:
                if(stored[i]['Email']==e):
                    return 0
                else:
                    result=firebase.post("/chat-app-login/User",data)
                    return 1
        except Exception as E:
            #print(E)
            return -1


#result=firebase.post("/chat-app-login/User",data)
#print(result)