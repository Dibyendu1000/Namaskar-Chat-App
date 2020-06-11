from firebase import firebase
import re


firebase=firebase.FirebaseApplication("https://chat-app-login.firebaseio.com/", None)
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):
    if(re.search(regex,email)):  
        return 0           
    else:  
        return 1

def push(u,e,p):
        try:
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
        except:
            return -1


#result=firebase.post("/chat-app-login/User",data)
#print(result)