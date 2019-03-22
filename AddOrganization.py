# Create a function to add an Organization to the file
def addOrganization(orgInput, orgList):

    # open the file to add the new organization
    appendFile = open("organizations.txt" , 'a')

    # use append to and the organization
    orgList.append((orgInput.rstrip()).split())
    appendFile.write(str(orgInput) + '\n') # write the new organization to the file

    # close the file
    appendFile.close()
