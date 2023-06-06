import os

import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import FunctionsLateCurrent as fc

filename = 'UDB/230127_001.mat'
cell_num = 5
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
    if i > 4 and s[1] < sweep_vals[i - 1][1]:
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
peakcurrent = []
latecurrent0 = []
latecurrent10 = []
latecurrent20 = []
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
    pcount = 0
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

        # plt.figure()
        # plt.plot(xsinrange_time,ysinrange)
        # plt.show()
        # plt.figure()
        # plt.plot(xsinrange_time,ysinrange)
        # plt.title('Time, 0Hz, ' + str(x))
        # plt.show()
        # plt.figure()
        # plt.plot(xsinrange_points,ysinrange)
        # plt.title('Data point, 0Hz, ' + str(x))
        # plt.xlim(450,1035)
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
        # print(peak_loc)
        #specify which points to include for late current and compute late current
        z = 0
        start_loc = peak_loc + 325
        # start_loc = peak_loc + 50
        end_loc = peak_loc + 475
        for y1 in ysinrange:
            if z > start_loc:
                if z < end_loc:
                    xs0.append(xsinrange_points[z])
                    ys0.append(ysinrange[z])
                    sum0 = sum0 + ysinrange[z]
            z = z + 1
        if pcount == 1:
            if j < 5:
                plt.figure()
                plt.plot(ysinrange, "blue")
                plt.plot(xs0, ys0, "red")
                plt.plot(peak_loc, ysinrange[peak_loc], "o-")
                plt.plot(start_loc, ysinrange[start_loc], "o-")
                plt.plot(end_loc, ysinrange[end_loc], "o-")
                plt.title(str(x) + ', 0 Hz')
                plt.title('Representative Sodium Current Trace')
                plt.xlabel('Data Point')
                plt.ylabel('Sodium Current (A)')
                plt.xlim(400, 1035)
                plt.show()


        # # 10 Hz peak calculation
        # k = 0
        # i = 0
        # z = 0
        # ysinrange = []
        # xsinrange_time = []
        # xsinrange_points = []
        # xs10 = []
        # ys10 = []
        # for y in ys:
        #     if k >= 125000:
        #         if k < 127500:  # 2500 data points per spike (10 Hz = 0.1 sec/spike) (25000 points/sec * 0.1 sec/spike = 2500 points/spike)
        #             xsinrange_time.append(xs[k])
        #             xsinrange_points.append(k)
        #             ysinrange.append(y)
        #     k = k + 1
        # peak = min(ysinrange)
        # # plt.figure()
        # # plt.plot(xsinrange_points, ysinrange)
        # # plt.show()
        #
        # # find the x location of the peak
        # i = 0
        # if j < 4:
        #     for x1 in xsinrange_points:
        #         if ysinrange[i] == peak:
        #             peak_loc = i
        #             peak_locs10.append(peak_loc)
        #         i = i + 1
        # if j > 3:
        #     np.array(peak_locs10)
        #     peak_locu = sum(peak_locs10) / len(peak_locs10)
        #     peak_loc = int(peak_locu)
        #
        # # specify which points to include for late current and compute late current
        # z = 0
        # start_loc = peak_loc + 350
        # end_loc = peak_loc + 475
        # for y1 in ysinrange:
        #     if z > start_loc:
        #         if z < end_loc:
        #             xs10.append(xsinrange_points[z])
        #             ys10.append(ysinrange[z])
        #             sum10 = sum10 + ysinrange[z]
        #     z = z + 1
        # # plt.figure()
        # # plt.plot(xs10, ys10)
        # # plt.title(str(x) + ', 10 Hz')
        # # plt.show()
        # # if pcount == 1:
        # #     if j < 5:
        #         # plt.figure()
        #         # plt.plot(ysinrange, "blue")
        #         # plt.plot(xs10, ys10, "red")
        #         # plt.plot(start_loc, ysinrange[start_loc], "o-")
        #         # plt.plot(end_loc, ysinrange[end_loc], "o-")
        #         # plt.title(str(x) + ', 10 Hz')
        #         # plt.xlim(450, 1035)
        #         # plt.show()
        #
        # # 20 Hz peak calculation
        # k = 0
        # i = 0
        # z = 0
        # ysinrange = []
        # xsinrange_time = []
        # xsinrange_points = []
        # xs20 = []
        # ys20 = []
        # for y in ys:
        #     if k >= 195000:
        #         if k < 196250:  # 2500 data points per spike (10 Hz = 0.1 sec/spike) (25000 points/sec * 0.1 sec/spike = 2500 points/spike)
        #             xsinrange_time.append(xs[k])
        #             xsinrange_points.append(k)
        #             ysinrange.append(y)
        #     k = k + 1
        # peak = min(ysinrange)
        # # plt.figure()
        # # plt.plot(xsinrange_points, ysinrange)
        # # plt.show()
        #
        # # find the x location of the peak
        # i = 0
        # if j < 4:
        #     for x1 in xsinrange_points:
        #         if ysinrange[i] == peak:
        #             peak_loc = i
        #             peak_locs20.append(peak_loc)
        #         i = i + 1
        # if j > 3:
        #     np.array(peak_locs20)
        #     peak_locu = sum(peak_locs20) / len(peak_locs20)
        #     peak_loc = int(peak_locu)
        # # print(peak_locs20)
        # # print(peak_loc)
        #
        # # specify which points to include for late current and compute late current
        # z = 0
        # start_loc = peak_loc + 230
        # end_loc = peak_loc + 480
        # for y1 in ysinrange:
        #     if z > start_loc:
        #         if z < end_loc:
        #             xs20.append(xsinrange_points[z])
        #             ys20.append(ysinrange[z])
        #             sum20 = sum20 + ysinrange[z]
        #     z = z + 1
        # # plt.figure()
        # # plt.plot(xs20, ys20)
        # # plt.title(str(x) + ', 20 Hz')
        # # plt.show()
        pcount = pcount + 1

    sum0 = sum0 / 2
    sum10 = sum10 / 2
    sum20 = sum20 / 2
    latecurrent0.append(sum0)
    latecurrent10.append(sum10)
    latecurrent20.append(sum20)

    j = j + 1

# latecurrent0f = latecurrent0 / min(latecurrent0)
# latecurrent10f = latecurrent10 / min(latecurrent10)
# latecurrent20f = latecurrent20 / min(latecurrent20)
print(latecurrent0)
# print(latecurrent0f)
# print(latecurrent10)
# print(latecurrent10f)
# print(latecurrent20)
# print(latecurrent20f)

doses = [0, 0.000001, 0.000005, 0.00001, 0.0001, 0.0005, 0.001, 0.002]

plt.plot(doses, latecurrent0)
plt.show()
plt.plot(doses, latecurrent10)
plt.show()
# plt.plot(doses, latecurrent20f)
# plt.show()

#plotting code to insert above
    # plt.figure()
    # plt.plot(xs, ys)
    # plt.title(p)
    # plt.show()
    # j = j+1
    # plt.figure()
    # plt.plot(xs, ys)
    # plt.xlim(0.11, 0.145)
    # plt.show()
    # plt.figure()
    # plt.plot(xs, ys)
    # plt.xlim(6.16, 6.185)
    # plt.show()
    # wb.close()
