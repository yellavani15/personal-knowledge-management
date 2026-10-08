class PKM:
    def __init__(self):
        self.users=[]
        self.notes={}
        self.current_user=None
    def login(self):
        username=input("Enter the valid Username :")
        
        if not any(not i.isalnum() for i in username):
            print("Username should  contain special characters")
            return
        password=input("Enter the Password :")
        if len(password) < 8:
            print("Password should contain at least 8 characters")
            return
        self.user=self.users.append(username)
        self.current_user=username
        print("Login Successful")

    def add_note(self):
        
        if self.current_user is None:
            print("Please Login First")
            return
        
        Topic=input("Enter the Topic name :")
        Content=input("Write your notes :")
        
        self.notes[Topic] = Content
        print("Note added Successfully")

    def access_note(self):
        
        if self.current_user is None:
            print("Please Login First")
            return
            
        topic=input("Enter the topic name :")
        if topic in self.notes:
            print("Topic:",topic)
            print("Content:",self.notes[topic])
            
        else:
            print("Topic not found")
    def modify_note(self):
        if self.current_user is None:
            print("Please Login First")
            return

        topic=input("Enter the topic :")
        if topic in self.notes:
            content=input("Enter the content :")
            self.notes[topic]=content
            print("Note Modified Successfully")
        else:
            print("Topic not found")

    def logout(self):
        if self.current_user is not None:
            self.current_user = None
            print("Logout Successful")
        else:
            print("No User Logged in")
V=PKM()
while True:
    print("Personal Knowledge Management system".upper().center(80,'='))
    print("1.Login")
    print("2.Add Note")
    print("3.Access Note")
    print("4.Modify Note")
    print("5.Logout")
    choice=input("Enter your Choice :")
    if choice=="1":
        V.login()
    elif choice=="2":
        V.add_note()
    elif choice=="3":
        V.access_note()
    elif choice=="4":
        V.modify_note()
    elif choice=="5":
        V.logout()
    else:
        print("Invalid choice")
    