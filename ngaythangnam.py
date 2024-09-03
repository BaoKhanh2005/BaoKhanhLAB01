# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:45:16 2024

@author: BAO KHANH
"""

ngaythangnam=input("Nhập vào ngày tháng năm: ")
dd,mm,yyyy = ngaythangnam.split(' ')
print("Ngày/Tháng/Năm:", dd,"/",mm,"/",yyyy)
print("Ngày/Tháng/Năm:", dd,"/",mm,"/",yyyy[-2:])
print("Năm/Tháng/Ngày:", yyyy,"/",mm,"/",dd)