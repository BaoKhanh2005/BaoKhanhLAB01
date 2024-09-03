# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:55:57 2024

@author: BAO KHANH
"""

a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
a1=a**(1/3)
b1=b**(1/3)
c = (a*b)**(1/3)
print("Kết quả của biểu thức: ", (((a+b)/(a1+b1))-c) / ((a1 - b1)**2))