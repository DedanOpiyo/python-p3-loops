#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    year = 10
    while year > 0:
        print(year)
        year -= 1
    print("Happy New Year!")
    # pass

def square_integers(int_list):
    # code goes here!
    new_intList = list()
    for int in int_list:
        new_intList.append(int * int)
    return new_intList
    # pass
    # Alternatively: using List comprehensions...
    new_intList = [int ** 2 for int in int_list]
    return new_intList

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif not num % 5:
            print("Buzz")
        else:
            print(num)
    # pass

# Test calls
print(happy_new_year()) 
print(square_integers([1,2,3,4,5]))
print(fizzbuzz())