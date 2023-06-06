import os

import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import functions as fc

filename = 'UDB/220714_003.mat'
cell_num = 6
data_type = 3
t_num = filename.split('_')[0]
r_num = filename.split('.')[0]
traces = fc.get_traces(filename)

excel_filename = '%s/%s_1NaPharmUDB.xls' % (os.getcwd(),r_num)
xlsx_name = fc.xls_to_xlsx(excel_filename)
wb = openpyxl.load_workbook(xlsx_name)
sht_name = wb.sheetnames[0]
sht = wb[sht_name]
pharm_data = fc.read_pharm(sht,cell_num)
sweep_vals = []
for a, s, c in zip(pharm_data['Age'], pharm_data['Sweep'], pharm_data['Concentration']):
    sweep_vals.append(['Trace_' + s + '_%d' % (cell_num), int(a), c])

#find transition points
t_2pts = []
t_pt = []
ct = 0
l = len(sweep_vals)
for i, s in enumerate(sweep_vals):
    if i > 3 and s[1] < sweep_vals[i - 1][1]:
        prev_s = sweep_vals[i - 1]
        pt = [prev_s]
        pts = [prev_s] if i == 1 else [sweep_vals[i - 2], prev_s]
        t_pt.append(pt)
        t_2pts.append(pts)
    if i == l - 1:
        pt = sweep_vals[i]
        pts = [prev_s] if i == 1 else [sweep_vals[i - 1], pt]
        t_pt.append(pt)
        t_2pts.append(pts)
    ct = ct + 1
print(t_pt)
print(t_2pts)

#plot trace for each dose
j = 0
peakcurrent0 = []
peakcurrent10 = []
peakcurrent20 = []
peak_locs0 = []
peak_locs10 = []
peak_locs20 = []
peak_locu = 0
#to use 2 traces for each dose
for p in t_2pts:
    print(j)
    sum0 = 0
    sum10 = 0
    sum20 = 0
    for x in p:
        k = 1
        i = 0
        z = 0
        ysinrange = []
        xsinrange_time = []
        xsinrange_points = []
        xs0 = []
        ys0 = []
        trace_num = x[0]
        if trace_num in traces:
            trace = traces[trace_num]
        else:
            ct = ct - 1
            trace_num = 'Trace_' + str(1) + '_' + str(data_type) + '_' + str(ct) + '_' + str(cell_num)
            trace = traces[trace_num]
        # print(t_pt[1][0][1],trace)
        xs = [x[0] for x in trace]
        ys = [x[1] for x in trace]
        # plt.plot(xs, ys)
        # plt.title(p)
        # plt.show()
        xcount = len(xs)

        # 0 Hz peak calculation
        k = 0
        i = 0
        z = 0
        for y in ys:
            if k >= 0:
                if k < 2500:   #2500 data points per spike (10 Hz = 0.1 sec/spike) (25000 points/sec * 0.1 sec/spike = 2500 points/spike)
                    xsinrange_time.append(xs[k])
                    xsinrange_points.append(k)
                    ysinrange.append(y)
            k = k + 1
        peak = min(ysinrange)
        sum0 = sum0 + peak
        # plt.figure()
        # plt.plot(xsinrange_points,ysinrange)
        # plt.show()

        #find the x location of the peak
        i = 0
        if j < 4:
            for x1 in xsinrange_points:
                if ysinrange[i] == peak:
                    peak_loc = x1
                    peak_locs0.append(peak_loc)
                i = i + 1
        if j > 3:
            np.array(peak_locs0)
            peak_locu = sum(peak_locs0) / len(peak_locs0)
            peak_loc = int(peak_locu)
            peak_locs0.append(peak_loc)

        # 10 Hz peak calculation
        k = 0
        i = 0
        z = 0
        ysinrange = []
        xsinrange_time = []
        xsinrange_points = []
        xs10 = []
        ys10 = []
        for y in ys:
            if k >= 125000:
                if k < 127500:  # 2500 data points per spike (10 Hz = 0.1 sec/spike) (25000 points/sec * 0.1 sec/spike = 2500 points/spike)
                    xsinrange_time.append(xs[k])
                    xsinrange_points.append(k)
                    ysinrange.append(y)
            k = k + 1
        peak = min(ysinrange)
        sum10 = sum10 + peak
        # plt.figure()
        # plt.plot(xsinrange_points, ysinrange)
        # plt.show()

        # find the x location of the peak
        i = 0
        if j < 4:
            for x1 in xsinrange_points:
                if ysinrange[i] == peak:
                    peak_loc = i
                    peak_locs10.append(peak_loc)
                i = i + 1
        if j > 3:
            np.array(peak_locs10)
            peak_locu = sum(peak_locs10) / len(peak_locs10)
            peak_loc = int(peak_locu)
            peak_locs10.append(peak_loc)

        # 20 Hz peak calculation
        k = 0
        i = 0
        z = 0
        ysinrange = []
        xsinrange_time = []
        xsinrange_points = []
        xs20 = []
        ys20 = []
        for y in ys:
            if k >= 195000:
                if k < 196250:  # 2500 data points per spike (10 Hz = 0.1 sec/spike) (25000 points/sec * 0.1 sec/spike = 2500 points/spike)
                    xsinrange_time.append(xs[k])
                    xsinrange_points.append(k)
                    ysinrange.append(y)
            k = k + 1
        peak = min(ysinrange)
        sum20 = sum20 + peak
        # plt.figure()
        # plt.plot(xsinrange_points, ysinrange)
        # plt.show()

        # find the x location of the peak
        i = 0
        if j < 4:
            for x1 in xsinrange_points:
                if ysinrange[i] == peak:
                    peak_loc = i
                    peak_locs20.append(peak_loc)
                i = i + 1
        if j > 3:
            np.array(peak_locs20)
            peak_locu = sum(peak_locs20) / len(peak_locs20)
            peak_loc = int(peak_locu)
            peak_locs10.append(peak_loc)

    sum0 = sum0 / 2
    sum10 = sum10 / 2
    sum20 = sum20 / 2
    peakcurrent0.append(sum0)
    peakcurrent10.append(sum10)
    peakcurrent20.append(sum20)

    j = j + 1

peakcurrent0f = peakcurrent0 / min(peakcurrent0)
peakcurrent10f = peakcurrent10 / min(peakcurrent10)
peakcurrent20f = peakcurrent20 / min(peakcurrent20)
print(peakcurrent0)
print(peakcurrent0f)
print(peakcurrent10)
print(peakcurrent10f)
print(peakcurrent20)
print(peakcurrent20f)

if current == 1:
    doses = [0, 1e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5]
else
    doses = [0, 0.000001, 0.000005, 0.00001, 0.0001, 0.0005, 0.001, 0.002]

plt.plot(doses, peakcurrent0f)
plt.show()
plt.plot(doses, peakcurrent10f)
plt.show()
plt.plot(doses, peakcurrent20f)
plt.show()
