#!/bin/bash

echo "Chuong trinh tim so max"
echo "======================="

if [ $# -lt 3 ] || [ $# -gt 9 ]
then
	echo "Loi!!!!"
	exit 1
fi
echo "So luong cac doi so truyen vao: $#"
max=$1
for i in $*
do
	if [ $max -lt $i ]
	then
		max=$i
	fi
done
echo $max

