# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:47:55 2024

@author: BAO KHANH
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
if a!=0:
    print("Phương trình có một nghiệm duy nhất: ", -b/a)
elif a==0 and b==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    print("Không có đáp án")