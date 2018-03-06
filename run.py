#coding:utf-8
__author__ = "langtuteng"
import unittest
from interface.Dtt_case import Ddt_case
from public import gene_report

def main():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Ddt_case))
    # unittest.TextTestRunner().run(suite)
    gene_report.gene_report(suite)

if __name__ == '__main__':
    main()
