#!/bin/bash

i="r"
while [ $i = "r" ]
do
read file_name
read path
full_path=$path/$file_name
touch $full_path && chmod +x $full_path
echo "Restart: "
read i
done
