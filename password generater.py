import string

import random
user= input('enter your password : ')
pwd_len=8
num=string.digits
char=string.punctuation
upper_letter=string.ascii_uppercase
letter=string.ascii_letters
def user_input():
    if user in char:
        if user in num:
            if len(user)>=4:
                print('next page')
    else:
        print(' type  a strong password it should consis atleast one number')
    user2=input('do u want the computer to recommnd y/n')
    if user2 =='y':
        return password_generator()
    elif user=='n':
        return user_input


def password_generator():
    password=upper_letter+num+char+letter
    pwd=''
    for i in range (pwd_len):
        pwd+=''.join(random.choice (password))
    print(pwd)
password_generator()