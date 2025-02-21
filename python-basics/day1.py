#from math import *
# n = input("Nhap vao gia tri cua n: ")
# print("Gia tri cua n la: {}".format(n))
# print("Kieu du lieu cua n la: {}".format(type(n)))

# a = int(input("Nhap vao 1 so nguyen : "))
# print(type(a))

# a, b = 50, 200
# if a > 50 and b >= 100 :
#     print("Hello World")
# elif a < 50 :
#     print("Hello")
# else :
#     print("Else")
#
# c, d = 100, 200
# if c < d : print(c,'less than', d)
# for i in range(0, 5, 1):
#         print(i,end=' ')
# else:
#     print('End loop')

# def add(a, b):
#     return a + b
#
# def hello():
#     print("Hello World")

def add(*args):
    return sum(args)

def show_info(*kwargs):
    print(kwargs)



if __name__ == '__main__':
    print(add(50, 60, 70, 80))
    show_info(name='28tech', job='Dev')

