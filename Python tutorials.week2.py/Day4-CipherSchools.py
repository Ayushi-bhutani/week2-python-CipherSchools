#more about lists
# num =list(range(1,11))
# print(num)
num = [1,2,3,4,5,6,7,8,9,10]
# num.pop(2)
# print(num)
# print(num.index(1,3))

def neg(l):
    negative =[]
    for i in l:
        negative.append(-1)
    return negative

print(neg(num))

#Exercise
def square_list(l):
    square =[]
    for i in l:
        square.append(i**2)
    return square
numbers=list(range(1,11))

print(square_list(numbers))