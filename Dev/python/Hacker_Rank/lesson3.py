#!/bin/python3

import math
import os
import random
import re
import sys

def func(value):
    if value % 2 !=0:
        print("Weird")
    elif 2 <= value and 5 >= value:
        print("Not Weird")
    elif 6 <= value and 20 >= value:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    func(n)
