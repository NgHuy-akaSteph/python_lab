# Python
## Day 1:
### 1. Comment
    # : chú thích trên 1 dòng
    """ """ : chú thích tren nhieu dong
### 2. Method print()
Syntax : printf ( object , sep = separator, end = end)
+ object : doi tuong trong python can in
+ separator : dau phan cach giua cac doi tuong, mac dinh la 1 space
+ end : ki tu duoc in cuoi cua dong, mac dinh la enter
### 3. Variable and types
#### 3.1 Variable 
- Dynamic typing : bien duoc tao va xac dinh kieu du lieu dong
- De biet kieu du lieu co the dung ham type()
- Ten bien khong duoc chua dau cach, ki tu dac biet hoac bat dau bang so
- Ten bien phan biet chu hoa va thuong (case sensitive)
#### 3.2 Types
#1. Number : Integer, Floating-point numbers, Complex numbers
```python
        """
        Integer : khong co gioi han, co the in ra cac so o he co so 2, 8, 10, 16
        - 0b/0B : binary
        - 0o/0O : octal
        - 0x/0X : hexadecimal
        """
        a = 0b1101
        print(a) # 13
        b = 0o123
        print(b) # 83
        c = 0x22A
        print(c) # 554
```
```python
        """
        Floating-point numbers (So thuc) : so am, duong kem theo phan thap phan
        - MaxVal = 1.8*10^308, cac gia tri > MaxVal coi la inf (infinity)
        - MinVal = 5.0*10^-324, cac gia tri < MinVal coi la 0
        """
        a = 1.9e308
        print(a) # inf
        b = 5.4e-325
        print(b) # 0.0
        c = 28.0419234
        print('%.2f' % c) # 28.04
        print(round(a, 2)) #28.04
        print('Gia tri cua c la: {:.2f}'.format(a)) #Gia tri cua c la: 28.04 
```
```python
      # Complex numbers = real part + imaginary part
      a = 3 + 5j
      print(a.real) # 3.0
      print(a.imag) # 5.0
```
#2. Kieu bool :
+ True : xau khac rong, so khac 0
+ False

#3. Kieu xau ki tu str:
- Noi dung duoc dat trong dau nhay don hoac nhay kep
- Xau co nhieu dong thi dat giua 3 nhay kep
```python
    s = 'abc'
    s1 = "abc"
    t = """
    python abc
    egf
    """
```
#4. Casting
```python
    a = int('123') # a = 123
    b = int(123.123) # b = 123
    c = float('50.22') # c = 50.22
    d = str(1234) # d = '1234'
```
### 4. Operator
```python
    # Toan tu gan
    a, b, c = 100, 200, 'abc'
    print(a, b, c) # 100 200 abc
    # Hoan vi gia tri cua 2 bien
    x, y = 1, 2
    y, x = x, y # x = 2, y = 1
    
```
```python
# Toan tu toan hoc
    a, b = 300, 200
    print(a/b) # 1.5
    print(a//b) # 1
    print(a%b) # 100
    x, y = 2, 3
    print(x * y) # 6
    print(x ** y) # 8
# Toan tu so sanh : tuong tu C++
# Toan tu logic : and, or, not
# Toan tu nhan dang
    a = [1,2,3]
    b = [1,2,3]
    print(a == b) # True
    print(a is b) # False : id(a) != id(b)
    print(a is not b) # True
# Toan tu thanh vien    
    s = 'abcdef'
    print('a' in s) # true
    print('k' in s) # false
```
### 5. Nhap input
```python
n = input('Nhap vao gia tri cua n: ') # 123
print(type(n)) # <class 'str'>
print(n) # 123

# Tach du lieu nhap vao
a, b, c = map(int, input('Nhap 3 so nguyen: ').split()) # 1 2 3
# a = 1, b = 2, c = 3
```

### 6. sqrt, pow, floor, factorial, gcd, sum
```python
    from math import *
    print(help(math)) # in huong dan ve cac ham trong thu vien
    # sqrt : square root 
    print(sqrt(4)) # 2.0
    print(isqrt(4)) # 2
    # pow : power
    print(pow(2, 4)) # 16.0
    print(pow(8, 1/3)) # 2.0
    # ceil : tra ve so nguyen gan nhat lon hon input
    print(ceil(2.2)) # 3
    # floor : tra ve so nguyen gan nhat nho hon input
    print(floor(2.8)) # 2
    # factorial : giai thua
    print(factorial(3)) # 6
    # gcd : greatest common divisor
    print(gcd(100, 350)) # 50
    # comb(n, k) : to hop chap k cua n
    print(comb(5, 3)) # 10
    #perm(n, k) : chinh hop chap k cua n
    print(perm(5, 3)) # 60
    
    #buil-in function: abs(), round(), min(), max(), sum(), length()
```

### 7. Condition Structure
```python
    if condition1 and condition2 :
        #code

    if condition:
        #code
    else: 
        #code

    if condition:
        #code
    elif condition1:
        #code
    else:
        #code
    
    a, b = 100, 200
    res = '28tech' if a < b else 'python' # in ra 28tech
```
### 8. Loop 
```python
    #for loop
    # range (start, stop, step) 
    # start : gia tri bat dau (mac dinh la 0)
    # stop: gia tri cuoi cung cua day so (can nay khong lay duoc)
    # step: Buoc nhay cua day so (mac dinh la 1)
    for i in range(0, 5, 1):
        print(i, end=' ')
    else:
        print("End loop") # cau lenh neu vong lap ko duoc thuc hien tiep
    #output : 0 1 2 3 4
    
    #while loop
    while condition :
        #code
    else:
        #code
    
    #break : lap tuc thoat khoi vong lap va thuc hien khoi code tiep theo
    #continue: bo qua phan con lai cua vong lap va tiep tuc vong lap tiep theo
    
```
### 9. Method & Recursion
```python
    #Method
    # def function_name(param1, param2, ...):
    #     #code
    #     return value
    # #goi ham
    # function_name(param1, param2, ...)
    # Mac dinh tra ve None neu khong co return
    #Ex:
    def add(a, b):
        return a + b
    print(add(2, 3)) 
    #output: 5
    
    def add(*args):
        return sum(args)
    print(add(1, 2, 3, 4, 5)) 
    #output:  15
    
    def show_info(*kwargs):
        print(kwargs)
    show_info(name='28tech', age=20) 
    #output:  {'name': '28tech', 'age': 20}
        

    #Recursion
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)
```
### 10. Scope
#### 10.1 Local
- Bien duoc khai bao trong pham vi cua 1 ham.
- Bien nay chi ton tai va co gia tri trong ham do.
```python
    def show():
        a = 100
        print(a)
    show() # 100
    print(a) # NameError: name 'a' is not defined
```
#### 10.2 Global
- Bien duoc khai bao ngoai cac ham
- Bien nay co pham vi truy cap trong toan bo file ma nguon
- De thay doi gia tri cua bien toan cuc trong ham con, su dung tu khoa _**global**_.
Neu khong Python se  tao 1 bien _**local**_ co cung ten vs bien _**global**_ 
va nhung thay doi o bien nay khong anh huong den bien _**global**_
```python
    a = 100
    def show():
        global a
        a = 200
        print(a)
    show() # 200
    print(a) # 200
```
#### 10.3 Enclosed
- Trong nested function, khi khai bao 2 bien co cung ten o trong 2 ham nay thi 2 bien co pham vi khac nhau
- Bien o ham ben ngoai goi la bien _**enclosed**_
```python
    def outer():
        a = 100
        def inner():
            a = 200
            print(a)
        inner() # 200
        print(a) # 100
    outer()
```
- Su dung keyword _**nonlocal**_ de thay doi gia tri cua bien **_enclosed_**
```python
    def outer():
        a = 100
        def inner():
            nonlocal a
            a = 200
            print(a)
        inner() # 200
        print(a) # 200
    outer()
```
### 11. List, List Slicing, List Comprehension, Lamda
#### 11.1 List
- _**List**_ tuong tu cau truc **_Array_** trong C++
- Tinh chat:
    + List are ordered : cac phan tu trong list la co thu tu
    + Accessed by index : truy cap vao phan tu bang chi so
    + Lists can contain any arbitrary objects : co the chua bat ky doi tuong nao
    + List are mutable : co the thay doi noi dung cua list
```python
    #Khai bao list
    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c']
    c = [1, 'a', 2.5]
    d = []
    e = list()
    print(type(a)) # <class 'list'>
    print(type(e)) # <class 'list'>
    
    # len(list) : tra ve so phan tu trong list
    print(len(a)) # 5
    
    # Truy cap theo chi so, 
    # Co ho tro chi so am. Chi so am se duoc tinh tu cuoi list
    print(a[0]) # 1
    print(a[-1]) # 5
    
    # Duyet list
    # for in range
    for i in range(len(a)):
        print(a[i], end=' ')
    # for each
    for i in a:
        print(i, end=' ')
    
    # Thay doi gia tri cua phan tu
    # Thay doi gia tri cua phan tu thong qua chi so: a[index] = value
    a[0] = 100 # a = [100, 2, 3, 4, 5]
    
    # Them phan tu vao list
    # append(value) : them phan tu vao cuoi list
    a.append(6) # a = [100, 2, 3, 4, 5, 6]
    # insert(index, value) : them phan tu vao vi tri index
    a.insert(1, 200) # a = [100, 200, 2, 3, 4, 5, 6]
    # extend(list) : them list vao list
    a.extend([7, 8, 9]) # a = [100, 200, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Xoa phan tu khoi list
    # remove(value) : xoa phan tu dau tien co gia tri value
    a.remove(200) # a = [100, 2, 3, 4, 5, 6, 7, 8, 9]
    # pop(index) : xoa phan tu tai vi tri index
    a.pop(0) # a = [2, 3, 4, 5, 6, 7, 8, 9]
    # clear() : xoa toan bo phan tu trong list
    a.clear() # a = []
    
    # Nhan ban list
    f = a * 2 # f = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    e = [0] * 10 # -> tao list co 10 phan tu 0
    
    # Tim kiem phan tu trong list
    # index(value) : tra ve chi so cua phan tu dau tien co gia tri value
    print(a.index(3)) # 1
    # count(value) : dem so lan xuat hien cua value trong list
    print(a.count(3)) # 1
    # in/not in : kiem tra phan tu co trong list hay khong
    print(3 in a) # True
    print(3 not in a) # False
    
    # Sap xep list
    # sort() : sap xep list tang dan
    a.sort() # a = [2, 3, 4, 5, 6, 7, 8, 9]
    # reverse() : dao nguoc list
    a.reverse() # a = [9, 8, 7, 6, 5, 4, 3, 2]
    
    # Mot so ham khac
    # copy() : sao chep list
    b = a.copy() # b = [9, 8, 7, 6, 5, 4, 3, 2]
    # list() : chuyen doi tu tuple, set, dictionary sang list
    c = list((1, 2, 3)) # c = [1, 2, 3]
    # max(), min(), sum()
    print(max(a)) # 9
    print(min(a)) # 2
    print(sum(a)) # 44
    # all() : tra ve True neu tat ca phan tu trong list la True
    # any() : tra ve True neu co it nhat 1 phan tu la True
    
    

```
#### 11.2 List Slicing
- Python list slicing la mot ky thuat giup ban co the truy cap vao mot khoang phan tu trong list thong qua toan tu
- Cu phap : List[start:stop:step]
  - start : chi so bat dau : neu < 0 thi start bat dau tu vi tri cuoi cung cua list
  - stop : chi so ket thuc : neu > len(list) thi stop = len(list)
  - step : buoc nhay : neu < 0 thi dao nguoc list
  - Neu start & stop deu am thi step cung phai am neu khong se tra ve list rong

```python
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a[0:5]) # [1, 2, 3, 4, 5]
    print(a[:5]) # [1, 2, 3, 4, 5]
    print(a[5:]) # [6, 7, 8, 9]
    print(a[0:9:2]) # [1, 3, 5, 7, 9]
    print(a[::2]) # [1, 3, 5, 7, 9]
    print(a[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(a[-1:-5:-1])  # [9, 8, 7, 6]
    print(a[-1:-5:1]) # []

    # Thay doi gia tri cua list thong qua slicing
    a[1:3] = [10, 11] # a = [1, 10, 11, 4, 5, 6, 7, 8, 9]
    a[1:3] = [10, 11, 12] # a = [1, 10, 11, 12, 4, 5, 6, 7, 8, 9]
    a[1:3] = [] # a = [1, 12, 4, 5, 6, 7, 8, 9]
    
    # Shallowing copy
    b = a[:] # b = [1, 12, 4, 5, 6, 7, 8, 9]
    print(b) # [1, 12, 4, 5, 6, 7, 8, 9]
    print(b is a) # False
    print(b == a) # True
```
#### 11.4 Lamda
- Lamda function la mot ham khong ten, khong can dung tu khoa def (anonymous function)
- IIFE (Immediately Invoked Function Expression) : ham duoc goi ngay sau khi duoc dinh nghia
- Cu phap : lambda arguments : expression (arguments : danh sach cac doi so, expression : bieu thuc)
```python
    #Ex:
    add = lambda a, b : a + b
    print(add(2, 3)) # 5
    # Lamda function co the co nhieu doi so va IIFE
    print((lambda x, y, z : x + y - z)(5, 6, 7)) # 4
    # Lamda function co the su dung trong ham khac
    def my_func(n):
        return lambda a : a * n
    double = my_func(2)
    print(double(5)) # 10

    # Su dung lamda function trong sorted(), filter(), map()
    a = [1, 2, 3, 4, 5]
    b = sorted(a, key = lambda x : x % 2) # b = [2, 4, 1, 3, 5]
    c = filter(lambda x : x % 2 == 0, a) # c = [2, 4]
    d = map(lambda x : x ** 2, a) # d = [1, 4, 9, 16, 25]
```
#### 11.3 List Comprehension
- List comprehension la mot cach tao list moi tu list cu bang cach su dung cu phap nhanh chong va de hieu
- Cu phap : [expression for item in iterable if condition]
```python
    #Ex:
    a = [1, 2, 3, 4, 5]
    # Tao list moi chua cac phan tu la binh phuong cua cac phan tu trong list a
    b = [i ** 2 for i in a] # b = [1, 4, 9, 16, 25]
    # Tao list moi chua cac phan tu chan trong list a
    c = [i for i in a if i % 2 == 0] # c = [2, 4]
    # Tao list moi chua cac phan tu chan va binh phuong cua cac phan tu le trong list a
    d = [i if i % 2 == 0 else i ** 2 for i in a] # d = [1, 2, 9, 4, 25]
```
### 12. Unpacking, Tuple, Map, Filter, Reduce
#### 12.1 Unpacking
- Unpacking la mot ky thuat giup ban co the chia nho cac phan tu trong list, tuple, set hoac iterable ra thanh cac bien rieng le
- Dung _ trong truong hop khong quan tam den gia tri cua phan tu do
```python
    #Ex:
    a = [1, 2, 3]
    x, y, z = a
    print(x, y, z) # 1 2 3
    
    s = 'abc'
    x, y, z = s
    print(x, y, z) # a b c
    
    b = [1, 2, 3, 4, 5]
    x, y, *z = b
    print(x, y, z) # 1 2 [3, 4, 5]
```
```python
    # Unpacking trong for loop
    a = [(1, 2), (3, 4), (5, 6)]
    for x, y in a:
        print(x, y)
    
    # Unpacking trong function
    def show(a, b, c):
        print(a, b, c)
    show(*a) # 1 2 3
```

#### 12.2 Tuple
- Tuple la mot collection co thu tu trong python
- Cac tinh chat cua tuple:
    - Tuple are ordered : cac phan tu trong tuple la co thu tu
    - Accessed by index : truy cap vao phan tu bang chi so
    - Tuple can contain any arbitrary objects : co the chua bat ky doi tuong nao
    - Tuple are immutable : khong the thay doi noi dung cua tuple 
  nhung neu item trong tuple la object co the thay doi duoc thi van co the thay doi cac item do
```python
a = (1, 2, 3, 4, 5)
print(type(a)) # <class 'tuple'>
print(a[0]) # 1
print(a[-1]) # 5
print(a[1:3]) # (2, 3)
print(a[::-1]) # (5, 4, 3, 2, 1)

s = 'abcdef'
b = tuple(s) # b = ('a', 'b', 'c', 'd', 'e', 'f')

# Sorting tuple : sorted() -> list
c = (3, 2, 1, 4, 5)
d = sorted(c) # d = [1, 2, 3, 4, 5]
c = tuple(d) # c = (1, 2, 3, 4, 5)
```
#### 12.3 Map, Filter, Reduce
- Map : ap dung mot ham len tat ca cac phan tu cua 1 iterable
```python
    a = [1, 2, 3, 4, 5]
    b = map(lambda x : x ** 2, a) # b = [1, 4, 9, 16, 25]
```
- Filter : loc cac phan tu cua 1 iterable
```python
    a = [1, 2, 3, 4, 5]
    b = filter(lambda x : x % 2 == 0, a) # b = [2, 4]
```
- Reduce : ap dung mot ham len tat ca cac phan tu cua 1 iterable de tinh toan ra 1 gia tri duy nhat
```python
    from functools import reduce
    a = [1, 2, 3, 4, 5]
    b = reduce(lambda x, y : x + y, a) # b = 15
```
### 13. Sort
### 14. Set, Dictionary, Counter
### 15. Matrix
### 16. String (str)
### 17. OOP
### 18. File


   
    

    
    