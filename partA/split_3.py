import csv
import os
 
path = './res.txt' 
workspace = '.'
 
with open(path, 'r', newline='') as file:
    csvreader = csv.reader(file)
    a = next(csvreader)
    print(a)
    i = j = 0
    for row in csvreader:
        print(row)
        print(f'i is {i}, j is {j}')
        # every 2700 rows in one file and give it a new file name
        if i % 2700 == 0:
            j += 1
            print(f"csv {j} generates successfully")
        csv_path = os.path.join(workspace, 'part_{}.txt'.format(j))
        print(csv_path)
        # If the file does not exist, then create a new one
        if not os.path.exists(os.path.dirname(csv_path)):
            os.makedirs(os.path.dirname(csv_path))
            with open(csv_path, 'w', newline='') as file:
                csvwriter = csv.writer(file)
                #csvwriter.writerow(['image_url'])
                csvwriter.writerow(row)
            i += 1
        # If the file exists, then add data in it
        else:
            with open(csv_path, 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(row)
            i += 1