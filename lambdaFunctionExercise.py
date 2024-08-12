# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument
addFifteen = lambda num : num + 15
print(addFifteen(10))

# 2 . create a lambda function that multiplies argument x with argument y and prints the result.
getSum = lambda x, y : x + y
print(getSum(1, 5))

#3 . Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number
def multipl(num):
    return lambda x : x * num

res = multipl(2)
print(res(15))

res = multipl(3)
print(res(15))

res = multipl(4)
print(res(15))

#4 Write a Python program to sort a list of tuples using Lambda.
inp = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
inp.sort(key = lambda x : x[1])
print(inp)

#5 Write a Python program to sort a list of dictionaries using Lambda.
lst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
lst.sort(key=lambda x : int(x.get('model')))
print(lst)

#6  Write a Python program to filter a list of integers using Lambda.
orgLst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNum = list(filter(lambda x : x % 2 == 0, orgLst))
oddNum = list(filter(lambda x : x % 2 != 0, orgLst))
print(evenNum)
print(oddNum)

#7  Write a Python program to square and cube every number in a given list of integers using Lambda.
squareOfAllNum = list(map(lambda x : x ** 2, orgLst))
cubeOfAllNum = list(map(lambda x : x ** 3, orgLst))
print(squareOfAllNum)
print(cubeOfAllNum)

#8 Write a Python program to find if a given string starts with a given character using Lambda.
x = lambda i : True if i[0] == ('a' or 'A') else False
print(x('Aditya'))
print(x('aditya'))
print(x('Lisa'))

#9 Write a Python program to extract year, month, date and time using Lambda.
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x : x.year
month = lambda x : x.month
date = lambda x : x.day
time = lambda x : x.time()

print(year(now))
print(month(now))
print(date(now))
print(time(now))

#10 Write a Python program to check whether a given string is a number or not using Lambda.
result = lambda x : True if type(x) == int else False
print(result(10))
print(result(10))
print(result('adi'))
print(result(True))

#11 Write a Python program to find the intersection of two given arrays using Lambda.
lstOne = [1, 2, 3, 5, 7, 8, 9, 10]
lstTwo = [1, 2, 4, 8, 9]

result = list(filter(lambda x : x in lstTwo, lstOne))
print(result)
