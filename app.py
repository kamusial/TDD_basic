from functions import *

x = int(input('Do ilu gramy w FizzBuzz?  '))
for i in range(1, x+1):
    print(i, ' -> ', fizzbuzz(i))
