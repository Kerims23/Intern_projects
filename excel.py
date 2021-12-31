import openpyxl as xl
from openpyxl.chart import bar_chart, Reference

def process_workbook(filename):
    wb=xl.load_workbook(filename)
    sheet=wb['sheet1']