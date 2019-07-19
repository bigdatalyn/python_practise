#enconding: utf-8

s = 'abc'
ss = "abcd"
sss = '''
abc1
abc2
abc3
'''
print(s)
print(ss)
print(sss)


s1 = 'abc\\abc'
print(s1)

s2 = 'abc\'"abc'
print(s2)


##>>> print('a\tb')
##a       b
##>>> print('a\rb')
##b
##>>> print('a\fb')
##a
##b
##>>> print('a\nb')
##a
##$$b
##>>> print('\f')
##
##>>>

print('abcde\r123')
print('abcde\r12345678')

print('a\\tb\\nc\\')

#print(int('1.5'))
print(int(1.5))

##int/str => float
##float/str => int
##int/float => str


print(type(int(1.2)))
print(type(int('1')))
print(type(float(1)))
print(type(float('1.2')))
print(type(str(1)))
print(type(str('1')))



a = input('num1:')
b = input('num2:')
total = int(a) + int(b)
print(a + ' + ' + b + ' = ' + str(total))

