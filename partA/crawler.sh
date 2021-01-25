#!/bin/bash
#Collecting Twitter Geolocated Data
#Craw data from twitter
python twitter_streaming.py > ./res.txt
#split the raw data 'res.txt' into files of size 10M
python split3.py
#parse original data into 'parse_data1.csv' and 'parse_data1.json' file
python parse_data.py

#load 'parse_data1.csv' file into database
#Open Navicat, create a new database, then right click the 'table' and click 'import Wizard'
#get title of urls in tweet text, insert into database
#In python, first open the database, select all the urls where is not null, select the result into a list,then extract the title for the url one by one, finally insert the title back into the table
#export data from database into file 'parse_data2.csv'
#Open Navicat, create a new database, then right click the 'table' and click 'Export Wizard', then choose 'csv'

#split 'parse_data2.csv' into files of size 10M small_file_0.csv
python split2.py
#get the number of generated files
filenum=$(ls small_file_*.csv | wc -l)
#convert splited files 'small_file_*.csv' into 'small_file_*.json' format
cnt=0
while [ $cnt -lt $filenum ]
do 
  python convert.py $cnt
  cnt=$((cnt+1))
done
