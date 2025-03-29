#Function to check whether a number is even or odd
def even_odd(number):
    if number%2==0:
        print("The number is Even")
        
    else:
        print("The number is Odd")
        
even_odd(26)

#Function to add two variable
def add(a,b):
    sum=a+b
    return sum

result=add(2,5)
print(result)

#Function to Convert Celcium into Farenhite & simultaneously!

def convert_temperature(temp,unit):
   if unit=="C":
    return temp*9/5+32
   elif unit=="F":
       return (temp-32)*5/9

print(convert_temperature(23,"F"))

#Function to check whether your password is strong or not!

def pass_checker(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "@#$%&" for char in password):
        return False
    return True

print(pass_checker("Anu9140@1"))
print(pass_checker("RANdom12345678@+?"))

#Function to check whether a string is palindrome or not!
def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("ANUrag"))

#Factorial of a number using recusrion!

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
    
# Lambda Function:It is used to solve one or 2 step problems

#P1 
addition=lambda a,b:a+b
print(addition(7,5))

#P2
even=lambda num:num%2==0
print(even(132))

#Map Function

numbers=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x*x,numbers)))

#Function to Calculate area of rectangle!

def sq_area(length,breadth):
    area=length*breadth
    print(area)
sq_area(12,12)






     
       
       
