def getServerName(search, org):
    """
    Take the name of server at the
    print it if exist

    """

    # take the list of organisations and take every time one organisation
    for i in org:

        # If the seach name is equal with the first element of the organisation
        # list then return the website of the server
        if  search == i[0]:
            new = "Server Address: " + i[1] + " \n" + "IP Address: " + i[2]
            return new

    # If we don't find the name it's return that string
    return "Not found"
