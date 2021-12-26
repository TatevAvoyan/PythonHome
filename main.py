import os
import csv


# os.rmdir('dir')
if not os.path.isdir("dir"):
    os.mkdir("dir")


with open('dir/test.csv', 'a+', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['John', 'Smith', 24])
