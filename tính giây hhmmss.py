# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:00:01 2024

@author: BAO KHANH
"""

thoigian = input("Nhập thời gian: ")
hh,mm,ss =map(int,thoigian.split(':'))
print("Thời gian sau khi đổi ra giây: ", hh*60*60 + mm*60 +ss)