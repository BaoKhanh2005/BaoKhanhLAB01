# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:19:38 2024

@author: BAO KHANH
"""

gio = float(input("Nhập giờ: "))
phut = float(input("Nhập phút: "))
giay = float(input("Nhập giây: "))
if gio<24 and gio>=0 and phut<60 and phut>=0 and giay<60 and giay>=0:
    print("Giờ, phút, giây hợp lệ")
else:
    print("Giờ, phút, giây không hợp lệ")