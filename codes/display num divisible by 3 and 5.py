def display(num):
    message=""
    if (num%3==0 and num%5==0):
        message=("zoom")
    elif (num%5==0):
        message=("zap")
    elif(num%3==0):
        message=("zip")
    else:
        message=("invalid")
    return message

#Provide different values for num and test your program
message=display(9)
print(message)