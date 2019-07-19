#enconding: utf-8

print( 1+1 )

a_int = 1
b_float = 1.14
c_ = +10
d_minus = -10 

print("int: ", a_int, " float: ", b_float, " int: ", c_ , " minus: ", d_minus)


name = 'abc'
age = 17

#desc = 'my name is ' + name + ', and I am ' + age + ' old.'
desc = 'my name is ' + name + ', and I am ' + str(age) + ' old.'

print(type(name), type(age))

print(desc)

# 加+ 减- 乘* 除/ 整除// 余% 幂 **
# python 2.7 整数除于整数得整数(导入 __future__import division修改行为与python3.5一致)

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
