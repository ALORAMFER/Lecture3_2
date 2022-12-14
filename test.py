import unittest

from library import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
        

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(" M22", l[1][1])
        

    def test_read3(self):
        try:
            printer = CSVPrinter("Alonso")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except (FileNotFoundError, IOError) as e:
            print('File not found, try again')
