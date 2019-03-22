from socket import * # import functions from socket module
from threading import Thread # import Thread from threading module
# import the functions from the files
from getServerName import *
from getStats import *
from AddOrganization import *
from removeOrganization import *


activenames = []
# Create the class for multithreading
class clientHandler(Thread):
    def __init__(self,connectionSocket):
        Thread.__init__(self)
        self.__connectionSocket = connectionSocket

    def run(self):
        username = self.__connectionSocket.recv(1024).decode("utf-8")  # take the username from the client
        password = self.__connectionSocket.recv(1024).decode("utf-8")  # take the password from the client
        userLogin = [username, password]
        statUser = login(userLogin)
        self.__connectionSocket.send(statUser.encode("utf-8"))

        check = self.__connectionSocket.receive(1024).decode("utf-8")

        if check == "correct":
            choice = 0
            while choice != '5': # check if the choice is in the range from 1 to 4
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
                    removeOrgRecieved = self.__connectionSocket.recv(1024).decode("utf-8") # recieving the name of the organization
                    for i in orgInfo:
                        if removeOrgRecieved == i[0]:
                            orgInfo = removeOrganization(removeOrgRecieved, orgInfo)
                            messageToSend = "Successfully Removed!"
                        else:
                            messageToSend = "Organization not found"

                    self.__connectionSocket.send(messageToSend.encode("utf-8"))


                elif choice == '5':
                    break
                else:
                    print("invalid input!!!!!")
        else:
            incorect = "incorrect"
            self.__connectionSocket.send(incorect.decode("utf-8"))

        print("closing connection")
        self.__connectionSocket.close() # close connections

    def login(userLogin):
         
        usersPass = openUserFile()  # take the user from the list        

        if (userLogin in usersPass) and (userLogin[0] not in activenames):
            activenames.append(userLogin[0])
            activate = "True"
            return activate
        elif userLogin[0] in activenames:
            activate = "already"
            return activate
            
        else:
            activate = "False"
            return activate

def main():

   

    while True:
        connectionSocket, clientAddress = serConnection()

        user = clientHandler(connectionSocket)  # call the class clientHandler
        user.start()


def serConnection():
    
    serverName = gethostname()
    serverPort = 5000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(5)
    print("Server is ready for connection.")
    connectionSocket, clientAddress = serverSocket.accept()
    print('Client address:', clientAddress)
    return connectionSocket, clientAddress

# Open the organization file and create the list
def openFiles():
    openFile = open("organizations.txt" , 'r')
    orgInfo = []
    for j in openFile:
        newOrg = j.rstrip().split()
        orgInfo.append(newOrg)

    return orgInfo

# Open the organization file and create the list
def openUserFile():
    userFile = open('users.txt', 'r')
    orgUser = []
    for i in userFile:
        newUser = i.rstrip().split()
        orgUser.append(newUser)

    return orgUser


def appendFile():
    appendFile = open("organizations.txt" , 'a')
    
# create a function with the menu for the max, min, median, mean
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


