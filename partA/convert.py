import sys
import csv
import json

csvfile = open('./small_file_'+sys.argv[1]+'.csv','rU')
jsonfile = open('./small_file_'+sys.argv[1]+'.json', 'w')

fieldnames = ("id","text", "location", "link","title")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')



