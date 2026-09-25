# Function which is used to check Either the number is odd or even:
num=int(input("Enter any number:"))
def odd_even(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
odd_even(num)