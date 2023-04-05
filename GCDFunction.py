def GCD(num1, num2):
    if (num2 == 0):
        print("The GCD is", num1)
    else:
        return GCD(num2, num1%num2)
    
GCD(10,1000)