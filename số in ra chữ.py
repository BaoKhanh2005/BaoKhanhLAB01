# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:39:44 2024

@author: BAO KHANH
"""

giatri = {0: "Không",1: "Một",2: "Hai",3: "Ba",4: "Bốn",5: "Năm",6: "Sáu",7: "Bảy",8: "Tám",9: "Chín"}
a = int(input("Nhập số: "))
if a >= 0 and a <= 9:
    print("Giá trị: ", giatri[a])
else:
    print("Khong đoc đuoc")