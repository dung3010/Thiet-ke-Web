#!/usr/bin/env python3

str1="Tri tue nhan tao ngay nay co the thay the con nguoi trong mot so cong viec nhat dinh"
str2="con nguoi ngay nay"

rmstr=str2.split()
data=str1.split()

print(rmstr)
for i in rmstr:
	for j in data:
		if i==j:
			str1=str1.replace(j,"",1)
str1=" ".join(str1.split())

with open('a.txt','w') as f:
	f.write(str1)

