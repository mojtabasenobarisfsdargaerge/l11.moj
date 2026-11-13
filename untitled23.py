n ="ali","12345","ali@gmail.com","active"
k ="sara","abc789","sara@gmail.com","active"
b ="reza","45678","reza@gmail.com","blocked"
    
with open("users.txt","w")as ml:
    ml.write(n +  "\n")
    ml.write(k +  "\n")
    ml.write(b +  "\n")
class user:
    def __init__(self,username,password,email,status):
        self.username =username
        self.password =password
        self.email =email
        self.status =status
    def to_format(self,matn):
        with open(matn, "w")as i:
            i.write(self.username + "\n")
            i.write(self.password + "\n")
            i.write(self.email + "\n")
            i.write(self.status + "\n")
    def 	__str__(self):
        print(self.username)
        print(self.password)
        print(self.email)
        print(self.status)
class FileManager:
    def __init__(self,maser):
        self.maser =maser
    def find_user(self,username):
        if username in self.maser:
            return True
        else:
            return False
    def read_users(self):
        print(self.maser)
    def add_user(self,u,p,e,s):
        z =username =u, password=p, email =e, status=s + "\n"
        with open(self.maser,"w")as e:
            e.write(z + "\n")
    def delete_user(self,username):
        with open(self.maser, "w") as e:
            e.writelines(username)
    def update_status(self,username, status):
        username[status] =status
    def login(self,username, password):
        if username and password in self.maser:
            return True
        else:
            return False
        def generate_report(self):
            with open(self.maser, "r", encoding="utf-8") as f:
                statuses = [line.strip().split("|")[3] for line in f if line.strip()]
            
    
    
    
    
    
    
    
    
    
    
    
    
    