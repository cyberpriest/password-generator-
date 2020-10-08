import random
from string import  *
from pyinputplus import inputStr,inputInt
ask = 'y'
print (" <PasswordGenerator>  ".center(30,'*'))
print ("created by ----[joshua.A.timi]---- ")
def main():
    global ask 
    while ask == 'y' or ask == 'y'.upper() or ask == 'yes':
        print()
        length = inputInt(" specify password length ",blank = True,timeout=14,default=" TimeOut re-run the program again")
        my_S = f"{ascii_letters}{punctuation}{digits}"
        #print (my_S)
        get_pwd(my_S,length)
        print()
        ask = inputStr(" do you wanna generate again type(yes) type no to quit ")   
def get_pwd(my_S,L):
    c = random.choices(my_S,k=L)
    print ()
    print (" password generated : ".upper(),"".join(c))  
main()
