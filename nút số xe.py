# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:16:39 2024

@author: BAO KHANH
"""

a=int(input("Nhập biển số xe gồm 4 số: "))
số_đầu = a // 1000
số_hai = a // 100 % 10
số_ba = a // 10 % 10
số_cuối = a % 10
nut = số_đầu + số_hai + số_ba + số_cuối
a =nut//10
b =nut%10
c =a+b
d =c//10
e =c%10
f =d+e
print("Biển số xe của bạn được: (nút)", f)