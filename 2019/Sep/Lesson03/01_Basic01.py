#encoding: utf-8

# n = 0
# m = 1
# while n <= 8:
#     n = n + 1
#     m = 1
#     while m <= n:
#         print(str(m) + '*' + str(n) + '=' + str(m*n) + ' ',end='')
#         m = m + 1
#     print('')

import random

guess = random.randint(0,100)
count = 0
print('Answer: ' + str(guess))
while True:
    g = input('Plz input a number: ')
    g = int(g)
    count += 1
    if guess == g:
        print('Write! You guess number is :' + str(g))
        break
    elif guess > g:
        print('Wrong! You guess number is greater than ' + str(g))
    elif guess < g:
        print('Wrong! You guess number is smaller than ' + str(g))
    if count >= 5:
        break
    