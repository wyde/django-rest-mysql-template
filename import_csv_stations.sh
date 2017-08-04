#!/bin/bash
csv_file="./csv/weather_rainfallstation.csv"
if [ -f "$csv_file" ]
then
    echo " $csv_file already exists"
else
    echo " start downloading $csv_file"
    wget https://rawgit.com/yeeede/seidm-hw6-jupyter/master/RainTenMin_Cor.csv -O $csv_file
 fi

{
    echo " importing $csv_file data into mysql..." &&
    mysqlimport --ignore-lines=1 \
                --fields-terminated-by=',' \
                --lines-terminated-by='\n' \
                --local -u dbuser -p'dbuser1234' \
                demo $csv_file 
} || {
    echo "*** WARNING: please make sure mysql is running, the password is correct..."
}
