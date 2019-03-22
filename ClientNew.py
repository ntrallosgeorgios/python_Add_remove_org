from socket import * # import functions from socket module

def main():
    

    clientSocket = clientConnection()

    # run the validation 3 times if one of them is wrong
    for x in range(0,3):
        username = input("Enter User Name: ")
        password = input("Enter Password: ")
        userPass = username + " " + password
        # send the username and the password to the server
        clientSocket.send(userPass.encode("utf-8"))
        authMessage = clientSocket.recv(1024).decode("utf-8")
        # get an answer from the user
        auth = clientSocket.recv(1024).decode("utf-8")
        print(authMessage)
        # if is correct break the loop
        if auth == "y":
            break 

    choice = ''
    while choice != '5' and auth == "y": # check if the choice is not 5 and continue to exec the while
            
        menu() # call the function menu
        choice = input('Enter relevent number:') 
        messageToSend = choice  # take the choice from the user
        print("Sending choice to server...")
        clientSocket.send(messageToSend.encode("utf-8")) # send the choice to the server

        if choice == '1':
            displayRecieved = clientSocket.recv(1024).decode("utf-8")
            print("message recieved from server")
                        
            messageToSend = input(displayRecieved)
            clientSocket.send(messageToSend.encode("utf-8"))
            print(clientSocket.recv(1024).decode("utf-8"))

        elif choice == '2':
            submenu() # call the submenu with the ither choices 
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
            
            

    messageToSend = choice
    print("Closing Connection!")
    clientSocket.send(messageToSend.encode("utf-8"))
    clientSocket.close()

# a function to create the connection with the server
def clientConnection():
    serverName = gethostname()
    serverPort = 5000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

def menu():
    print("1.Get server name and IP")
    print("2.Get Stastistics")
    print("3.Add new organization")
    print("4.Remove organization")
    print("5.Quit program.")

def submenu():
    print("1.Max")
    print("2.Min")
    print("3.Median")
    print("4.Mean")

# a function that take all the input from the client to create the new organization
def addOrgInput():
    orgName = input("Enter Organization Name:")
    orgDomain = input("Enter Organization Domain Name:")
    orgIp = input("Enter Enter Ip Adress:")
    orgTime = input("Enter connection time:")

    orgInput = (orgName + '\t' + orgDomain +'\t'+ orgIp +'\t'+ orgTime)

    return orgInput

main()
