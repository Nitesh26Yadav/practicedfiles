import csv


with open("C:\\Users\\rsa-l\\Desktop\\vs py code\\file1.csv", 'r') as file:
    with open("C:\\Users\\rsa-l\\Desktop\\vs py code\\FTP.csv", 'w') as csv_file:
        for line in file:
            if line is dict:
                csv_writer = csv.DictWriter()
