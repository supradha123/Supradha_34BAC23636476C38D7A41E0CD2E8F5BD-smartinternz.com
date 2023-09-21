import random

def input_num(min, max):
    num = int(input())

    if num > max or num < min:
        print("Enter valid choice")
        return input_num(min, max)
    else: