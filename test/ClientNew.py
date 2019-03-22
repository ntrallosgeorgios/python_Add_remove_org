from socket import *  # import functions from socket module

def main():
    

    clientSocket = clientConnection()

    username = input("Enter User Name: ")
    clientSocket.send(username.encode("utf-8")) # send the username in the server
    password = input("Enter password: ")
    clientSocket.send(username.encode("utf-8"))  # send the username in the server
    
    checkUser = clientSocket.recv(1024).decode("utf-8")


    if checkUser == "True":
        correct = "correct"
        clientSocket.send(correct.encode("utf-8")
                          
        choice = ''
        while choice != '5': # check if the choice is not 5 and continue to exec the while
            
            menu() # call the function menu
            choice = input('Enter relevent number:')
            messageToSend = choice # take the choice from the user
            print("Sending choice to server...")
            clientSocket.send(messageToSend.encode("utf-8")) # send the choice to the server

            if choice == '1':
                displayRecieved = clientSocket.recv(1024).decode("utf-8")
                print("message recieved from server")
                        
                messageToSend = input(displayRecieved)
                clientSocket.send(messageToSend.encode("utf-8"))
                messageRecieved = clientSocket.recv(1024).decode("utf-8")
                print(messageRecieved)

            elif choice == '2':
                submenu()
                subChoice = ''
                subChoice = input("What stat you want? ")
                clientSocket.send(subChoice.encode("utf-8"))
                print(clientSocket.recv(1024).decode("utf-8"))

            elif choice == '3':
                addOrgNew = str(addOrgInput())
                clientSocket.send(addOrgNew.encode("utf-8"))
                print(addOrgNew + "\n Above record was successfully added!")

            
            elif choice == '4':
                removeOrg = input("Enter name of the Organization to remove: ")
                clientSocket.send(removeOrg.encode("utf-8"))
                print(clientSocket.recv(1024).decode("utf-8"))
            else:
                print("Invalid input!!!")

            messageToSend = choice
            print("Closing Connection!")
            clientSocket.send(messageToSend.encode("utf-8"))
    elif checkUser == "already":
        print("Already logged in.")
    else:
        print("Not valid user!!!")


    clientSocket.close() # close the connection

            

    #print("connected to " + serverName + "at" + gethostname(serverName))
        
    #messageToSend = input("Enter Message to send: ")
        #print("Sending Message")
        #clientSocket.send(messageToSend.encode("utf-8"))
        #messageRecieved = clientSocket.recv(1024)
        #print("Message came back from the server")
        #print(messageRecieved.decode("utf-8"))
        #if messageToSend == 'exit':
            #print("Closing connection")
            #print("Connection Closed")


# a function to create the connection with the server
def clientConnection():
    serverName = gethostname()
    serverPort = 5000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

def menu():
    print("1.Get server name and IP")
    print("2.Get Ststistics")
    print("3.Add new organization")
    print("4.Remove organization")
    print("5.Quit program.")

def submenu():
    print("1.Max")
    print("2.Min")
    print("3.Median")
    print("4.Mean")
    
def addOrgInput():
    orgName = input("Enter Organization Name:")
    orgDomain = input("Enter Organization Domain Name:")
    orgIp = input("Enter Enter Ip Adress:")
    orgTime = input("Enter connection time:")

    orgInput = (orgName + '\t' + orgDomain +'\t'+ orgIp +'\t'+ orgTime)

    return orgInput


main()
