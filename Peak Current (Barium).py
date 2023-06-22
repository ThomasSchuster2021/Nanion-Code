import matplotlib.pyplot as plt
import FunctionsPeakCurrent_Ba as fcpc
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Peak Currents')
row = 0
col = 2
rowupdated = 0

doses = ['0 M', '1 uM', '5 uM', '10 uM', '100 uM', '500 uM', '1 mM', '2 mM']

#Take in user inputs for how many variants, how many cells for each variant, and what cells to use
num_variants = input('How many variants are you analyzing? ')
i = 0
variant_list = []
files = []
nums = []
legend_titles = []
cell_names = []
while i < int(num_variants):
    j = 0
    mat_files = []
    cell_nums = []
    variant = input('What is the variant name? ')
    num_cells = input('How many cells for this variant? ')
    variant_list.append(variant)
    while j < int(num_cells):
        #file = input('Input MATLAB file name: ')
        run = input('Input Run name: ')
        file = run
        #file = run + '.mat'
        #file = 'UDB/' + file
        # file = "C:\\Users\\thoma\\OneDrive\\Documents\\Research Code\\Data\\" + file
        file = "Data\\" + file
        cell = int(input('Which cell? '))
        mat_files.append(file)
        cell_nums.append(cell)
        cell_names.append(str(cell) + ' ' + str(run))
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
all_peak_currents = []
cell_column = 2

#for each variant, extract the peak current at each drug concentration for each cell
for var in variant_list:
    var_files = files[i]
    cells = nums[i]
    j = 0
    peakcurrents = []
    print(var)
    for x in var_files:
        output = fcpc.doseresponse(x, cells[j])
        peakcurrent = output0[0]
        peakcurrents.append(peakcurrent)

        j = j + 1
    print(peakcurrents)


#write peak current values to Excel sheet
    sheet1.write(rowupdated, 0, str(var))
    row_doses = rowupdated + 1
    rowupdated = rowupdated + 1
    for d in doses:
        sheet1.write(int(row_doses), 0, d)
        row_doses = row_doses + 1
   # for c in cell_names:
   #     sheet1.write(0, int(cell_column0), c)
   #     cell_column0 = cell_column0 + 1
   # for c in cell_names:
   #     sheet1.write(0, int(cell_column10), c)
   #     cell_column10 = cell_column10 + 1
   # for c in cell_names:
   #     sheet1.write(0, int(cell_column20), c)
   #     cell_column20 = cell_column20 + 1
    q=2
    for x in peakcurrents:
        row = rowupdated
        sheet1.write(0,col, cell_names[q])
        for y in x:
            sheet1.write(row, col, y)
            row = row + 1
        col = col + 1
        q = q + 1
    row = rowupdated
    col = col + 1
  
    
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

