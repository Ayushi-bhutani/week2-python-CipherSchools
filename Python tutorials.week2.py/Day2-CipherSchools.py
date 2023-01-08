#user defined functions
def add(a,b):
    return a + b    #not necessary to write print instead you can write print but return is preferrable
total = add(2,3)    
print(f"addition od two numbers is {total}") 

#Functions practice
def last_char(name):
    return name[-1]
print(last_char("ayushi")) 

def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"   
num = int(input("enter number: "))        
print(odd_or_even(num))   

def is_even(num):  #num  is a parameter
    if num % 2 == 0:
        return True
    return False
num1 = int(input("enter: "))    
print(is_even(num1))       #here num1 is an argument

#greatest function in python
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c        
      
print(greatest(1,6,3))

#another method for finding greatest number
def greater(a,b):
    if a>b :
        return a
    else:
        return b    
       
def greatest(a,b,c):
    bigger = greater(a,b) 
    return greater(bigger,c)
print(greatest(1,2,3))

#fibonacci series
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    if n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")

fib(20)

#variable scope
def func():
    global x
    x=7
    return x
print(func())
x=5
def func2(x):
    print(x)
func2()
