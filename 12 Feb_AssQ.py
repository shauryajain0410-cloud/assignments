#q1 ---> whenever we write a code in python , somethings are not allowed to execute such that division by zero or reading a file that does not exists, these types of errors are basically known as exception. Syntax errors can be fixed but exceptions can't.
#q2 ---> when an exception is not handled , it gives an error and the whole block of code written below it will not be executed.

a = 10
b = 5/0
#ZeroDivisionError: division by zero

#q3 ---> try and except statements are used for doing so.

try:
    f = open("test43.txt","w")
    f.write("this is my msg")
except Exception as e:
    print("issue",e)

#q4 ---> 
try:
    f = open("test43.txt","w")
    f.write("this is my msg")
except Exception as e:
    print("issue",e)
else:
    f.close()
    print("successful")



try:
    f = open("test333.txt","r")
    f.write("yo")
finally:
    print("this will always print")


class validateage(Exception):
    def __init__(self,msg):
        self.msg = msg

def validate_age(age):
    if age < 0:
        raise validateage("age should not be less than zero")
    elif age > 200:
        raise validateage("age is very high")
    else :
        print("age is valid")

try:
    age = int(input("enter ur age"))
    validate_age(age)
except validateage as e:
    print(e)

#a) try and else: when we want to try out the code for exception handling , we use try , and if that try works and the code runs , the else block executes
#b) finally: this code of block always runs whether the try is executed or not
#c) raise: if we want to make a custom exception , we use raise

#q5 ---> Custom exceptions are the exceptions not set initially but are set by us as per out requirements. Suppose we want to input age for license , so that should be greater than 18 , but python would not give us any error for any age , so we set our own exceptions by using raise 

class ageCheck(Exception):
    def __init__(self,msg):
        self.msg = msg

def validate(age):
    if age < 18:
        raise ageCheck("age should not be less than 18")
    elif age > 200:
        raise validateage("age is very high")
    else :
        print("age is valid")

try:
    age = int(input("enter ur age"))
    validate(age)
except ageCheck as e:
    print(e)

#q6 ---> done above