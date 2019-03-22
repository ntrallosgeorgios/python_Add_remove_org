# this function take an input name of the server from the main function and the list that is # created list of the organizations 
def removeOrganization(name,  org):
     # that is will go in the main funtion
     #shan = input("You can remove an organisation, please enter the name:")

    # Here we remove the organization from the array
    for i in org:
        if  name == i[0]:
            org.remove(i)

    # We recreate the updated organizations file
    outfile = open ("organizations.txt", 'w')
    for i in org:
        for x in i:
            outfile.write(x + "\t")
        outfile.write("\n")
            

    outfile.close()

    # Return the new org(list)
    return org
