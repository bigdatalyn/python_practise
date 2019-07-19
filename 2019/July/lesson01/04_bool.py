#enconding: utf-8

'''
>= 90 => A
>= 80 => B
>= 70 => C
>= 60 => D
<60   => E
'''


is_boy = True
is_girl = False
print(is_boy, is_girl)


prompt = input('you have a son?(Y/N)')
many = 2

if prompt == 'Y':
    print('how many?')
    print(many)


print(bool(1))

print(bool(0))

print(bool(1.1))

'''

bool => int (True -> 1 False -> 0)
bool => float ( 1.0 / 0.0 )
bool => str ('True' / 'False')

str => bool

'' => False


>>> print(int(bool(False)))
0
>>> print(float(bool(False)))
0.0
>>> print(float(bool(True)))
1.0
>>> print(float(bool(False)))
0.0
>>> bool('')
False
>>> bool('False')
True
>>> bool('True')
True
>>>


'''
