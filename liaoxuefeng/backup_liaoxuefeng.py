## generator生成器
def triangles():
	lt = [1]
	while True:
		lt = [0] + lt + [0]
		yield lt[1:-1]
		lt = [lt[i] + lt[i+1] for i in range(len(lt) - 1)]

n = 0
for i in triangles():    
    print(i)
    n = n + 1
    if n == 10:
        break


## map函数
def normalize(name):
	return list(map(lambda s: s.title(), name))

name = ['adam', 'LISA', 'barT']
lt = normalize(name)
print(lt)


## reduce函数
from functools import reduce

def prod(L):
    return reduce(lambda x, y: x * y, L)

l = [1, 2, 3, 4]
print(prod(l))    


## 字符串转整数
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def fn(x, y):
#     return x * 10 + y

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]

# print(reduce(fn, map(char2num, '12424')))



# def str2int(ss):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    
#     def fn(x, y):
#         return x * 10 + y

#     def char2num(s):
#         return digits[s]
    
#     return reduce(fn, map(char2num, ss))

# string = '565787'
# print(str2int(string))



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
        return DIGITS[s]

def str2int(ss):
    reduce(lambda x, y: 10 * x + y, map(char2num, ss))


## 字符串转浮点型
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(ss):
    # dot_index = ss.index('.')
    # ss_first = ss[:dot_index]
    # ss_last = ss[dot_index + 1:]

    # r1 =  reduce(lambda x, y: 10 * x + y, map(char2num, ss_first))
    # r2 =  reduce(lambda x, y: 10 * x + y, map(char2num, ss_last))
    # return r1 + r2 / pow(10, len(ss[dot_index + 1:]))

def str2int(ss):
    ss = ss.split('.')

    r1 =  reduce(lambda x, y: 10 * x + y, map(char2num, ss[0]))
    r2 =  reduce(lambda x, y: 10 * x + y, map(char2num, ss[1]))
    return r1 + r2 / pow(10, len(ss[1]))


string = '565.7087'
print(str2int(string))


## 装饰器
import functools
import time

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.perf_counter()
        excute = func(*args, **kw)
        end_time = time.perf_counter()
        print("%s executed in %s ms" % (func.__name__, end_time - start_time))
        return excute
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.012)
    return x + y

print(fast(10, 4))


## 将类的方法转换为属性
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, vlaue):
        self._width = value


## 正则表达式
import re

'''匹配邮箱地址'''

#__author__:humin

def is_valid_email(addr):
    if re.match(r'\w+\.?\@\w+\.com$', addr):
        return print("True")
    print("地址错误")

is_valid_email('huminme@gmail.com')


re.match(r'\<?(\w+\s?)\>?\w+\@(\w+\.\w+)')

r'^\<?([\w\s]+)\>?\s*(\w*)@(\w+\.\w+)$'




    