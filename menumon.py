# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:13:26 2024

@author: BAO KHANH
"""

print("    ========== MENU ==========="
      "\n\t1. Hu tieu"
      "\n\t2. Chao long"
      "\n\t3. Banh canh"
      "\n\t4. Bun rieu"
      "\n\t5. Pho bo"
"\n\t==========================="
      "\n\tMoi nhap lua chon: "
"\n\t===========================")
menu=float(input("mời bạn chọn "))
if menu == 1:
    print("Hủ tiếu nha")
if menu == 2:
    print("Cháo lòng nha")
if menu == 3:  
    print("Bánh canh nhanh")
if menu == 4:  
    print("Bún riêu nha")
if menu == 5:
    print("Phở bò nha")
else:
    print("Không có món")