#!/usr/bin/env python3
""" 
Write a method `happy_new_year` that outputs numbers starting at 10 and
counting down to 1. After reaching 1, print out "Happy New Year!" """
def happy_new_year():
    # code goes here!
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print ("Happy New Year!")


""" 
Write a function `square_integers()` that takes one argument, a list of
integers and returns the list of squared elements.
"""
def square_integers(int_list):
    # code goes here!
    int_list = [num * num for num in int_list]
    return int_list

"""   
Write a method `fizzbuzz_printer` that prints the numbers from 1 to 100. For
multiples of three, print "Fizz" instead of the number and for the multiples
of five print "Buzz". For numbers which are multiples of both three and five,
print "FizzBuzz".
 """
def fizzbuzz():
    # code goes here!
    num = 1
    while num <= 100:
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
            num += 1
        elif (num % 3 == 0):
            print("Fizz")
            num += 1
        elif (num % 5 == 0):
            print("Buzz")
            num += 1
        else:
            print(num)
            num += 1
