import matplotlib.pyplot as plt
import FunctionsPeakCurrent as fcpc
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Peak Currents')
row = 0
col = 2
rowupdated = 0
comp = input('personal or lab computer? 1 for personal 2 for lab. ')
doses = ['0 M', '1 uM', '5 uM', '10 uM', '100 uM', '500 uM', '1 mM', '2 mM']

#Take in user inputs for how many variants, how many cells for each variant, and what cells to use
num_variants = input('How many variants are you analyzing? ')
i = 0
variant_list = []
files = []
nums = []
legend_titles = []
while i < int(num_variants):
    j = 0
    mat_files = []
    cell_nums = []
    variant = input('What is the variant name? ')
    num_cells = input('How many cells for this variant? ')
    variant_list.append(variant)
    while j < int(num_cells):
        file = input('Input MATLAB file name: ')
        if comp == 1:
            file = 'Data/' + file
        else
            file = 'Analysis Files/' + file
        cell = int(input('Which cell? '))
        mat_files.append(file)
        cell_nums.append(cell)
        j = j+1
    files.append(mat_files)
    nums.append(cell_nums)
    i = i + 1
# print(files)
# print(nums)
# print(variant_list)

for var in variant_list:
    title = var
    legend_titles.append(title)
# print(legend_titles)

i = 0
all_peak_currents0 = []
all_peak_currents10 = []
all_peak_currents20 = []
#for each variant, extract the peak current at each drug concentration for each cell
for var in variant_list:
    var_files = files[i]
    cells = nums[i]
    j = 0
    peakcurrents0 = []
    peakcurrents10 = []
    peakcurrents20 = []
    print(var)
    for x in var_files:
        output0 = fcpc.doseresponse0(x, cells[j])
        peakcurrent0 = output0[0]
        peakcurrents0.append(peakcurrent0)
        output10 = fcpc.doseresponse10(x, cells[j])
        peakcurrent10 = output10[0]
        peakcurrents10.append(peakcurrent10)
        output20 = fcpc.doseresponse20(x, cells[j])
        peakcurrent20 = output20[0]
        peakcurrents20.append(peakcurrent20)
        j = j + 1
    print('0 Hz')
    print(peakcurrents0)
    print('10 Hz')
    print(peakcurrents10)
    print('20 Hz')
    print(peakcurrents20)

#write peak current values to Excel sheet
    sheet1.write(rowupdated, 0, str(var))
    row_doses = rowupdated + 1
    rowupdated = rowupdated + 1
    for d in doses:
        sheet1.write(int(row_doses), 0, d)
        row_doses = row_doses + 1

    for x in peakcurrents0:
        row = rowupdated
        for y in x:
            sheet1.write(row, col, y)
            row = row + 1
        col = col + 1

    row = rowupdated
    col = col + 1

    for x in peakcurrents10:
        row = rowupdated
        for y in x:
            sheet1.write(row, col, y)
            row = row + 1
        col = col + 1

    row = rowupdated
    col = col + 1

    for x in peakcurrents20:
        row = rowupdated
        for y in x:
            sheet1.write(row, col, y)
            row = row + 1
        col = col + 1

    col = 2
    rowupdated = rowupdated + len(doses) + 1
    print(rowupdated)

    # avgpeak0 = sum(peakcurrents0)/len(peakcurrents0)
    # all_peak_currents0.append(avgpeak0)
    # avgpeak10 = sum(peakcurrents10) / len(peakcurrents10)
    # all_peak_currents10.append(avgpeak10)
    # avgpeak20 = sum(peakcurrents20) / len(peakcurrents20)
    # all_peak_currents20.append(avgpeak20)
    i = i + 1
# print(all_peak_currents0)
# print(all_peak_currents10)
# print(all_peak_currents20)

# wb = Workbook()
# sheet1 = wb.add_sheet('Peak Currents')
# i = 0
# j = 0
# for x in peakcurrents0:
#     i = 0
#     for y in x:
#         sheet1.write(i, j, y)
#         i = i + 1
#     j = j + 1
#
# i = 0
# j = j + 1
#
# for x in peakcurrents10:
#     i = 0
#     for y in x:
#         sheet1.write(i, j, y)
#         i = i + 1
#     j = j + 1
#
# i = 0
# j = j + 1
#
# for x in peakcurrents20:
#     i = 0
#     for y in x:
#         sheet1.write(i, j, y)
#         i = i + 1
#     j = j + 1
#
wb.save('Peak Currents.xls')
