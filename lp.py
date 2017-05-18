#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print (100+200+300)
print ('hello,world')
print('1024*768 =',1024*768)
#name=input('please input your name:')
#print('hello,',name)
print('I\'m ok!')
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
n = 123
f = 456.789
s1 = "'Hello,world'"
s2 = "'Hello,\\'Adam\\''"
s3 = "r\'Hello,\"Bart\"\'"
s4 = "r\'\'\'Hello,\nLisa!\'\'\'"
print('n =',n)
print('f =',f)
print('s1 =',s1)
print('s2 =',s2)
print('s3 =',s3)
print('s4 =',s4)

# 20170517
print('中文字符')
aa = ord('王')
print (aa)
bb = chr(aa+1)
print (bb)
cc = chr(29580)
print (cc)
s1 = 72
s2 = 85
s3 = 85 -72
r = s3/s1*100
print('%.1f%%' % r)
#print('%s %' % r)%
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

age = 20
if age > 18:
    print('your age is',age)
    print('adult')
age = 3
if age > 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
age = 3
if age > 18:
    print('adult')
elif age >=6:
    print('teenager')
else:
    print('kid')
#s = input('birth: ')
#birth = int(s)
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')
height = 1.75
weight = 60.5
bmi = int(weight/(height*height))
print (bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28 and bmi <= 32:
    print('肥胖')
elif bmi > 25 and bmi <= 28:
    print('过重') 
elif bmi > 18.5 and bmi <= 25:
    print('正常')
elif bmi <= 18.5:
    print('过轻')
classmates = ['wang','jia','jun']
for classmate in classmates:
    print (classmate)
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
sum = 0
for x in list(range(101)):
    sum=sum+x
print(sum)
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
L = ['Bart', 'Lisa', 'Adam']
ln=len(L)
index = 0
while index < ln:
    print('Hello,',L[index],'!')
    index = index + 1
