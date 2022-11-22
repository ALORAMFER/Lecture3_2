import csv


class CSVPrinter():
    def __init__(self, file_name):
        self.file_name = file_name
        
    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines


""""
q = CSVPrinter("C:/Users/alofu/OneDrive/NAIST 1/Special Lecture/Software Design/Report 2/Lecture2/sample.csv")
f = q.read()
print(f)
"""
    
    