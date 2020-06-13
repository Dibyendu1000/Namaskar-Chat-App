from firebase import firebase
#import bcrypt

firebase=firebase.FirebaseApplication("https://chat-app-login.firebaseio.com/", None)
def check(e,p):
        try:
            stored=firebase.get("/chat-app-login/User",'')
            if(not bool(stored)):
                return ('',0)
            for i in stored:
                #hashed=stored[i]['Password'].encode()
                #p=p.encode()
                #hashed=hashed.encode()
                if(stored[i]['Email']==e and stored[i]['Password']==p):
                    return (stored[i]['Email'],stored[i]['Name'],1)
            return ('',0)
        except Exception as E:
            #print(E)
            return ('',-1)