#!/bin/bash

data_folder="$HOME/Documents/Data"

if [ ! -d $data_folder ]
then
	echo "Thu muc $data_folder khong ton tai. Moi kiem tra lai."
	exit 1
fi

echo "Nhap ten thu muc Backup:"
read name

desktop_folder="$HOME/Desktop/$name"

if [ ! -d $desktop_folder ]
then
	echo "Thu muc $desktop_folder chua ton tai. Tien hanh tao thu muc."
	mkdir $desktop_folder
else
	echo "Thu muc $desktop_folder da ton tai"
fi


time=$(date +%T)
backup_name="Backup_$time.tar"

tar -cvf "$desktop_folder/$backup_name" -C "$HOME/Documents" Data

echo "Sao luu thanh cong!"
