#! python
# readCensusExcel.py - 统计人口普查数据

import openpyxl

wb = openpyxl.load_workbook('automate_online-materials/censuspopdata.xls')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}  # 用来存储县对应的普查区数目和人口数目

print("Reading rows...")
for row in range(2, sheet.get_highest_row() + 1):
    State =  sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop =    sheet['D' + str(row)].value


