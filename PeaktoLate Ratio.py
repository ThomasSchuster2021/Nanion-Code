import matplotlib.pyplot as plt
import numpy as np

import FunctionsLateCurrent as fclc
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('% Block of Peak Current')
sheet2 = wb.add_sheet('% Block of Late Current')
sheet3 = wb.add_sheet('Peak to Late Block Ratio')

#Take in user inputs for how many variants, how many cells for each variant, and what cells to use
comp = input('personal or lab computer? 1 for personal 2 for lab. ')
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
            #file = "C:\\Users\\thoma\\OneDrive\\Documents\\Research Code\\Data\\" + file
            file = "Data\\" + file
        else:
            file = 'Analysis Files\\' + file
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
row = 0
col = 0
for x in variant_list:
    sheet1.write(row, col, str(x))
    sheet2.write(row, col, str(x))
    sheet3.write(row, col, str(x))
    col = col + 1
col = 0

i = 0
all_peakchange_0 = []
all_percent_blocks_late = []
all_percent_blocks_peak = []
all_peaktolates = []
all_peaktolate_0 = []
#extract peak and late current for each drug concentration for each cell
for var in variant_list:
    var_files = files[i]
    cells = nums[i]
    j = 0
    peakchanges_0 = []
    percent_blocks_late = []
    peak_to_lates = []
    percent_blocks_peak = []
    peaktolates_0 = []
    peakchange0sum = 0
    latechange0sum = 0
    peaktolate0sum = 0
    # peaktolate20sum = 0
    #for x in var_files: #why not cells?
    for x in cells: #Changed
        output0 = fclc.doseresponse0(x, cells[j])
        peakcurrent = output0[0]
        latecurrent = output0[1]
        latecurrent100 = latecurrent[0]
        latecurrent0 = latecurrent[6]
        latecurrentdrug = latecurrent[3]
        peakcurrent100 = peakcurrent[0]
        peakcurrent0 = peakcurrent[6]
        peakcurrentdrug = peakcurrent[3]
        total_block_late = latecurrent100 - latecurrent0
        partial_block_late = latecurrent100 - latecurrentdrug
        percent_block_late = partial_block_late / total_block_late
        percent_blocks_late.append(percent_block_late)
        total_block_peak = peakcurrent100 - peakcurrent0
        partial_block_peak = peakcurrent100 - peakcurrentdrug
        percent_block_peak = partial_block_peak / total_block_peak
        percent_blocks_peak.append(percent_block_peak)
        peak_to_late = percent_block_peak / percent_block_late
        peak_to_lates.append(peak_to_late)
        j = j + 1

   #Only one input so only one data value. Ask what other data should be here.
    all_percent_blocks_late.append(percent_blocks_late)
    all_percent_blocks_peak.append(percent_blocks_peak)
    all_peaktolates.append(peak_to_lates)
    all_peaktolate_0.append(peaktolates_0)

    i = i + 1

# var = 0
# col = 0
# for v in all_peakchange_0:
#     row = 1
#     for v1 in v:
#         sheet1.write(row, col, v1)
#         row = row + 1
#     var = var + 1
#     col = col + 1

#write results to Excel sheet
var = 0
col = 0
for v in all_percent_blocks_peak:
    row = 1
    for v1 in v:
        sheet1.write(row, col, v1)
        row = row + 1
    var = var + 1
    col = col + 1

var = 0
col = 0
for v in all_percent_blocks_late:
    row = 1
    for v1 in v:
        sheet2.write(row, col, v1)
        row = row + 1
    var = var + 1
    col = col + 1

var = 0
col = 0
for v in all_peaktolates:
    row = 1
    for v1 in v:
        sheet3.write(row, col, v1)
        row = row + 1
    var = var + 1
    col = col + 1

# var = 0
# col = 0
# for v in all_peaktolate_0:
#     row = 1
#     for v1 in v:
#         sheet3.write(row, col, v1)
#         row = row + 1
#     var = var + 1
#     col = col + 1
# x = np.array([0,1,2,3,4])
# plt.figure()
# plt.xticks(x, variant_list)
# plt.bar(x, all_peakchange_0)
# plt.title('Percent Difference in Peak Current Between Variants')
# plt.xlabel('Variant')
# plt.ylabel('Percent Difference (%)')
# plt.show()
#
# plt.figure()
# plt.xticks(x, variant_list)
# plt.bar(x, all_latechange_0)
# plt.title('Percent Difference in Late Current Between Variants')
# plt.xlabel('Variant')
# plt.ylabel('Percent Difference (%)')
# plt.show()
#
# plt.figure()
# plt.xticks(x, variant_list)
# plt.bar(x, all_peaktolate_0)
# plt.title('Change in Peak to Late Current Ratio')
# plt.xlabel('Variant')
# plt.ylabel('Peak Current / Late Current')
# plt.show()


wb.save('Current Analysis.xls')
