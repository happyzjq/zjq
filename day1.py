import xlrd
data = xlrd.open_workbook('12.xls')
# data.sheet_names()
# print(str(data.sheet_names()))

table = data.sheets()[0]
nrow = table.nrows
ncol = table.ncols

for i in range(nrow):
    for j in range(ncol):
        print(table.cell(i,j).value,end='\t')
    print()