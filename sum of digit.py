#lex_auth_012693749623193600122

def find_sum_of_digits(number):
    
    strr = str(number)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
    

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                          