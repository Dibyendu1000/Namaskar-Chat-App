from firebase import firebase


firebase=firebase.FirebaseApplication("https://chat-app-login.firebaseio.com/", None)
def check(e,p):
        try:
            stored=firebase.get("/chat-app-login/User",'')
            if(not bool(stored)):
                result=firebase.post("/chat-app-login/User",data)
                return ('',0)
            for i in stored:
                if(stored[i]['Email']==e and stored[i]['Password']==p):
                    return (stored[i]['Name'],1)
            return ('',0)
        except:
            return ('',-1)