#!/usr/bin/env python3

import csv

data=[
	['MaNV','Hoten','Namsinh','DiaDiem'],
	['NV01','Nguyen Van Tam','2000','HCM'],
	['NV02','Dao Thi Tuyen','2001','HN'],
	['NV03','Le Thanh Trung','2004','DN']
	]

#Tao file .txt
with open('nhanvien.txt','w',encoding='UTF8',newline='') as f:
	w=csv.writer(f,delimiter='\t')
	w.writerows(data)

#Tao file .csv
with open('nhanvien.txt','r',encoding='UTF8',newline='') as f:
	data=csv.reader(f,delimiter='\t')
	with open('nhanvien.csv','w',encoding='UTF8',newline='') as f_csv:
		w=csv.writer(f_csv)
		w.writerows(data)

with open('nhanvien.csv','r',encoding='UTF8',newline='') as f:
	lines=f.readlines()
	print(lines[0])

with open('nhanvien.txt','r',encoding='UTF8',newline='') as f:
	print(f.read())
