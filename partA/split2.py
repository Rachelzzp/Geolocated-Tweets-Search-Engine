#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

originalFileName='parse_data2.csv'
header=''

chunkSize = 1e7

smallFileIdx=0
smallFileName = 'small_file_0.csv'
smallFile = open(smallFileName, "w")

lineSize=0

start=time.time()

with open(originalFileName) as bigFile:
    
    for lineno, line in enumerate(bigFile):
        if lineno==0:
            header=line
        lineSize+=len(line)
        if smallFile.closed:
            smallFileName = 'small_file_{}.csv'.format(smallFileIdx)
            smallFile = open(smallFileName, "w")
            smallFile.write(header)
        smallFile.write(line)
        if lineSize>chunkSize:
            smallFileIdx+=1
            lineSize=0
            smallFile.close()
    if smallFile:
        smallFile.close()
end = time.time()
print(end - start)