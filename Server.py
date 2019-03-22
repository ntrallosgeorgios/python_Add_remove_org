from socket import * # import functions from socket module
from threading import Thread  # import Thread from threading module
# import the functions from the files
from getServerName import *
from getStats import *
from AddOrganization import *
from removeOrganization import *

# Global variable
activeNames = []


# Create the class for multithreading
class clientHandler(Thread):
    def __init__(self,connectionSocket):
        Thread.__init__(self)
        self.__connectionSocket = connectionSocket

    def run(self):
        try:
            # Check the username 3 times if the username or the password is wrong
            for x in range(0,3):
                users = [] # create an empty list which will contain the username and the password from the file

                infile = open("users.txt" ,"r") # open the file
                for line in infile: # take every line from the file and put it in a list
                    subLine = (line.rstrip()).split() 
                    users.append(subLine) # add the user and password to the list
                print("waiting for username and password..")
                
                # take from the user the username and the password
                userPassRecieved = self.__connectionSocket.recv(1024)     
                userPass = userPassRecieved.decode("utf-8").split()
                print("username recieved",userPass)

                # check if the username and password is in the list 
                if userPass in users:
                    # check if the username is in the list of the active users
                    if userPass[0] in activeNames:
                        authDisplay = "User Already active"
                        auth = "n"
                        # send this variables to the user
                        self.__connectionSocket.send(authDisplay.encode("utf-8"))
                        self.__connectionSocket.send(auth.encode("utf-8"))  

                    else:
                        # add the username to the activeNames
                        activeNames.append(userPass[0])
                        authDisplay = "Login Success"
                        auth = "y"
                        # send this variables to the user
                        self.__connectionSocket.send(authDisplay.encode("utf-8"))
                        self.__connectionSocket.send(auth.encode("utf-8"))
                        break

                else:
                    authDisplay = "Login Unsuccessful."
                    auth = "n"
                    self.__connectionSocket.send(authDisplay.encode("utf-8"))
                    self.__connectionSocket.send(auth.encode("utf-8"))
            
            choice = '1'
            # check if the choice is in the range from 1 to 4
            while choice != '5' and auth == "y":
                orgInfo = openFiles()
                choiceRecieved = self.__connectionSocket.recv(1024)
                choice = choiceRecieved.decode("utf-8").rstrip()
                print('choice recieved: ', choice)
            
                if choice == '1':
                    displayMessage = "Enter the Server Name: " #Message to send to Client
                    self.__connectionSocket.send(displayMessage.encode("utf-8"))
                    searchServer = self.__connectionSocket.recv(1024).decode("utf-8") # receive from the client the name
                    retName = getServerName(searchServer, orgInfo) 
                    self.__connectionSocket.send(retName.encode("utf-8")) # send back the answer 

                elif choice == '2':
                    subChoiceRecieved = self.__connectionSocket.recv(1024).decode("utf-8").rstrip() #recieving sub choice
                    retMessage = statChoices(subChoiceRecieved, orgInfo) #Calling the subchoice handling function and getting the stat
                    self.__connectionSocket.send(retMessage.encode("utf-8")) #send back the answer
                    
                elif choice == '3':
                    newOrgRecieved = self.__connectionSocket.recv(1024).decode("utf-8") # recieving the name of the organization
                    addOrganization(newOrgRecieved, orgInfo) 
            
                elif choice == '4':
                    removeOrgRecieved = self.__connectionSocket.recv(1024).decode("utf-8")  # recieving the name of the organization
                    # take every time 1 organization from the file
                    for i in orgInfo:
                        # check if the name of the organization is equal with the first element of the list
                        if removeOrgRecieved == i[0]:
                            # user the function to remove the organization of the 
                            orgInfo = removeOrganization(removeOrgRecieved, orgInfo)
                            messageToSend = "Successfully Removed!"
                        else:
                            messageToSend = "Organization not found"

                    # send the message to the user
                    self.__connectionSocket.send(messageToSend.encode("utf-8"))
                            
            
                elif choice == '5':
                    # remove the user from the activeNames list
                    activeNames.remove(userPass[0])
                    break
                else:
                    print("invalid input!!!!!")

            print("closing connection")
            self.__connectionSocket.close() # close connections
    
        except IOError:
            print('cannot open user file \n')
        except:
            print("Some problem occur!!! \n")

        

def main():

    while True:
  
        connectionSocket, clientAddress = serConnection()
        user = clientHandler(connectionSocket)  # call the class clientHandler
        user.start()


def serConnection():
    
    try:
        serverName = gethostname()
        serverPort = 5000
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((serverName, serverPort))
        serverSocket.listen(5)
        print("Server is ready for connection.")
        connectionSocket, clientAddress = serverSocket.accept()
        print('Client address:', clientAddress)
        return connectionSocket, clientAddress
    except IOError:
        print("Something happend with the connection with the server")

# Open the organization file and create the list
def openFiles():
    try:
        openFile = open("organizations.txt" , 'r')
        orgInfo = []
        for j in openFile:
            newOrg = j.rstrip().split()
            orgInfo.append(newOrg)

        return orgInfo
    except IOError:
        print("The file organization don't exist")

# Open the organization and add 
def appendFile():
    try:
        appendFile = open("organizations.txt" , 'a')
    except socket.error:
        print("The file organization don't exist \n")
    
# is the main choice menu
def statChoices(choice,orgInfo):
    if choice == '1':
        maxOut = max(orgInfo)
        return maxOut
    elif choice == '2':
        minout = min(orgInfo)
        return minout
    elif choice == '3':
        medout = median(orgInfo)
        return medout
    elif choice == '4':
        meanout = mean(orgInfo)
        return meanout
    else:
        return "Invalid Input!"
       

main()


