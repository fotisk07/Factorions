import math

def digits(number):
    a=str(number)
    digitas = []
    for i in range(0,len(a)):
        digitas.append((number//10**i)%10)

    return digitas

if __name__ == "__main__":
    upper_bound = 50000
    




    for number in range(0,upper_bound):
        digits_fact_sum =0
        digits_num = digits(number)
        
        
        for digit in digits_num:
            digits_fact_sum =digits_fact_sum+ math.factorial(digit)
            
            
        

        if digits_fact_sum == number:
            print(number)

    print("The end")
    


    
