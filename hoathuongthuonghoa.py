# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:15:27 2024

@author: BAO KHANH
"""

chu= input("Nhập chữ cái: ")
if chu.islower():
    print("Kết quả: ", chu.upper())
elif chu.isupper():
    print("Kết quả: ",chu.lower())
else:
    print("Không phải chữ cái")