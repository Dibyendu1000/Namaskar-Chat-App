from firebase import firebase


firebase=firebase.FirebaseApplication("https://chat-app-login.firebaseio.com/", None)

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