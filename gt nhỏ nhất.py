# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:33:40 2024

@author: BAO KHANH
"""

a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
d=float(input("Nhập số d: "))
if a < b and a < c and a < d:
    print("Giá trị nhỏ nhất là: ",a)
elif b < a and b < c and b < d:
    print("Giá trị nhỏ nhất là: ",b)
elif c < b and c < a and c < d:
    print("Giá trị nhỏ nhất là: ",c)
else:
    print("Giá trị nhỏ nhất là: ",d)