def max(org):
    # we set the statup value of the maximum connections of the organization
    maxOrg = int(org[0][3])
    hostName = 0

    # use for loop to check all the minutes to the organization file
    for i in org:
        # we check every time if the new value of the connection is bigger than
        # the older and if it is we change the maxOrg with the new one
        # .Otherwhise is keeping the old value.
        if int(i[3]) > maxOrg:
            maxOrg = int(i[3])
            hostName = i[1]
            displayReturn = "Hostname: " + str(hostName) + "\nNo of Org: " + str(maxOrg)

    return displayReturn

def min(org):
    # we set the statup value of the minimum connections of the organization
    minOrg = int(org[0][3])
    hostName = 0

    # use for loop to check all the minutes to the organization file
    for i in org:
        # we check every time if the new value of the connection is lower than
        # the older and if it is we change the maxOrg with the new one
        # .Otherwhise is keeping the old value.
        if int(i[3]) < minOrg:
            minOrg = int(i[3])
            hostName = i[1]
            displayReturn = "Hostname: " + str(hostName) + "\nNo of Org: " + str(minOrg)

    return displayReturn

def mean(org):

    # we set a value to find the mean of the minutes in the organization file
    minutesOrg = 0

    # we use the for loop to count all the minutes in the file
    for j in org:
        minutesOrg += int(j[3])

    mednOrg = minutesOrg / len(org)

    return str(mednOrg)

def median(org):
    # we creat the new list where we are going to put all the minutes so after
    # that we can sort the list and find the median of the the minutes

    minutArray = []
    # we use the for loop to append all the minutes in one array
    for i in org:
        newValue = int(i[3])
        minutArray.append(newValue)


    sortArray = sorted(minutArray) # Sort the created list with time of timeArray
    lengthArray = len(minutArray)  # put to the value the length of the timeArray array
    devLength = lengthArray // 2

    # chech if the length of the array is odd or even
    if lengthArray % 2 == 0:
        num1 = devLength
        num2 = devLength - 1

        averNum = (sortArray[num1] + sortArray[num2] ) / 2

        meanOrg = averNum

    else:
        num = devLength - 1

        meanOrg = sortArray[num]

    return str(meanOrg)
