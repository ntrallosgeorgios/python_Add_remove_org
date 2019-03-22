def main():
    users = []
    activenames = []
    x=0

    infile = open("users.txt" ,"r")

     

    for line in infile:
        subLine = (line.rstrip()).split()
        users.append(subLine)


    while True:
        username = input("Enter User Name: ")
        password = input("Enter Password: ")
       

        output = authentication(username,password,users,activenames)
        print(output)
       
        
        
                            
     
      
        
def authentication(username,password,users,activenames):
    userPass = [username , password]
    
    if userPass in users:
        if username in activenames:
            return "Already logged in."
        activenames.append(username)
        return "Success!"
        
    else:
        return "Username or password Invalid!"
            


main()    
