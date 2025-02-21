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
### 10. Scope && BigO
### 11. List
### 12. Unpacking, Tuple, Map, Filter
### 13. Sort
### 14. Set, Dictionary, Counter
### 15. Matrix
### 16. String (str)
### 17. OOP
### 18. File


   
    

    
    