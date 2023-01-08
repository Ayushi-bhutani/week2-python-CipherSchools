#Intro lists
num=[1,2,3,4]
print(num(1))

word = ["word1",'word2','word3']
print(word[:2])

mix=[1,2,3,4,"word1",'word2','word3']
print(mix[-1])

mix[1:]='two'

#Add in list
l=[]
n=int(input("Enter"))
for i in range(n):
    a=input("Enter list iteam")
    l.append(a)
print(l)

#add more
fr1=['mango','orange']
print(fr1)

fr2=['grapes','apple']
print(fr2)
fr1.append(fr2)
print(fr1)

#delete data
fruits = ['Mango','Apple',"banana",'pear']
fruits.pop(1)
del fruits[2]
fruits.remove('pear')
print(fruits)

#some more lists
fruits =['orange','apple','pear','banana','kiwi','guava','orange']
print(fruits.count('orange'))

num=[122,2,3,4,50,34,345,33,5]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

num.clear()
print(num)

#'is' vs 'equal'
fruits =['orange','apple','pear','banana','kiwi']
fruits2 =['orange','apple','pear','banana','kiwi']
fruits1 =['orange','apple','pear','banana','kiwi','Guava',]
print(fruits==fruits2)
print(fruits is fruits1)

#join and split
user_info = 'Ritika 18'
print(user_info.split())

name,age=input("enter name and age").split(',')
print(name)
print(age)

#list vs array
# array same data type can be stored

#list vs string
l=['word1','word2','word3']
l.pop()
print(l)
s="string is immutable"
print(s.title())

#looping in list
fruits = ['orange','apple','pear','banana','kiwi']
for i in fruits:
    print(i)

#list inside list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[2])
for sublist in matrix:
    for i in sublist:
        print(i)
print(matrix[2][1])


