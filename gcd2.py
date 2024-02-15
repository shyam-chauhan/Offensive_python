def gcd(num1,num2):
    if(num1 == 0 or num2 == 0):
        if(num1 == 0):
            return num2
        else:
            return num1
    else:
        temp2 = num1 % num2
        return gcd(num2,temp2)
        
x = gcd(16,2)
print("gcd is : ",x)