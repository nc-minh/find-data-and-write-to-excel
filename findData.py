import csv
import os
from fnmatch import fnmatch

root = './src'
pattern = '*.ts'
startWith = 'logger.'
endWith = ');'

file_excel = open("test.ods", "w", encoding="utf-8-sig")

def solve(path):
    file = open(path, "r", encoding="utf-8-sig")

    # define string line you want to find
    line = 1

    row = file.readline() # a line(row) of the file
    while row != "": #untill file end
        row_start = row.find(startWith)
        row_end = row.find(endWith)
        if row_start != -1:
            current_line = line
            res = row[row_start:]
            while True:
                if row_end != -1:
                    break
                row = file.readline()
                line+=1
                row_end = row.find(endWith)
                res += row[row_start:]
            print(res)

            w = csv.writer(file_excel)
            w.writerow([res.replace('\n', '\015'), path, current_line])
            #default end of string readline() is \n, in excel file with \n cursor will jump to next row to write, should we use \015 like ctrl+enter
        row = file.readline()
        line+=1

if __name__ == '__main__':
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                solve(os.path.join(path, name))
