#!/usr/bin/env python3

name=input("Thong tin tap tin: ")
print("=======================")
try:
	words=0
	chars=0

	with open(name,'r',encoding='UTF8') as f:
		data=f.readlines()
	lines=len(data)

	for i in data:
		words += len(i.split())
		chars += len(i.replace(" ", "").strip())
	print("So luong dong: ", lines, " dong\n")
	print("So luong tu: ", words, " tu\n")
	print("So ky tu: ", chars, " ky tu\n")
	print("===============================================")
	n=int(input())
	if n <= lines:
		print(n, "dong dau tien cua file ",name)
		for i in range(n):
			print(data[i])
	else:
		print("So dong vuot qua so dong hien tai cua ", name)
except FileNotFoundError:
	print("Tep khong ton tai")
