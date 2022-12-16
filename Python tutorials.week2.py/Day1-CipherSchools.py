#infinite loop
#stop infinite loop using ctrl + C
 i = 0
 while i<=10:
    print("hello sexy")

# OR while loop
while True:
    print("hello")    

#for loop with range function:
for i in range(10):   #( i = 0 to 9)
    print(f"hello  world : {i}")    #no need to use i+=1, runs in defined range

# sum from 1 to 10
total = 0
for i in range (1,11):
    total += i
    
print(f"{total} is the sum of numbers defined in range")    

#sum of numbers till n(number entered by user)
num = int(input("please enter a number: "))
total = 0
for i in range(1,num+1):
    total += i
print(f"{total} is the sum of numbers from 1 to {num}")    

#logic:  
# num = "1256" length = 4
# int(num[0]) = 1
# int(num[1]) = 2
# int(num[2]) = 5
# int(num[3]) = 6
# i ---> 0 to 3
n = input("please enter a number: ")
sum = 0
l = len(n)
for i in range(0, l):
    sum += int(n[i])
print(f"sum of digits of number entered is {sum}")    

# break keyword
for i in range (1,11):
    if i == 5:
        break
    print(i)

# continue keyword
for i in range(1,11):
    if i == 5:
        continue
    print(i)


#Exercise 6   
#MODIFY GUESSING GAME
import random
winning_number = int(random.randint(1,100))
guess = 1
num = int(input("Enter your number: "))
game_over = False

while not game_over :   #while True:
    if num == winning_number:
        print(f"you win guessing the number {guess} times")
        game_over = True    #break
    else:
        if num < winning_number:
            print("too low")
            
        else:
            print("too high")   
        guess += 1                                # DRY PRINCIPLE = don't repeat yourself
        num = int(input("guess again: "))

#step argument
for i in range(1,11,2):
print(i)

for i in range(-10,0,1):
    print(i)

# for_loop_strings method used commonly for all programming languages
name = "Ayushi"
for i in range(len(name)):
    print(name[i])

# for_loop_strings used in particular for python    
name = "ayushi"
for i in name:
    print(i)

# easy method    
num = input("enter your number: ")
sum = 0
for i in num:
    sum += int(i)
  
print(sum)