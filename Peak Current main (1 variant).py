import matplotlib.pyplot as plt
import FunctionsPeakCurrent as fcpc

current = input('What drug areyou testing? 1 for Amiodarone, 2 for Mexiletine. ')
comp = input('personal or lab computer? 1 for personal 2 for lab. ')
num = input('How many cells are you analyzing? ')
i = 0
k = 0
mat_files = []
cell_nums = []
legend_titles = []
while i < int(num):
    file = input('Input MATLAB file name: ')
    if comp == 1:
        file = 'Data\\' + file
    else
        file = 'Analysis Files\\' + file
    cell = int(input('Which cell? '))
    mat_files.append(file)
    cell_nums.append(cell)
    i = i+1
print(mat_files)
print(cell_nums)
for f in mat_files:
    title = f + ', cell ' + str(cell_nums[k])
    k = k + 1
    legend_titles.append(title)
print(legend_titles)

#obtain 0Hz peak current
i = 0
peakcurrents0 = []
if current == 1:
    doses = [0, 1e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5]
else
    doses = [0, 0.000001, 0.000005, 0.00001, 0.0001, 0.0005, 0.001, 0.002]
plt.figure()
while i < int(num):
    output = fcpc.doseresponse0(mat_files[i], cell_nums[i])
    peakcurrent0 = output[0]
    peakcurrents0.append(peakcurrent0)
    plt.plot(doses, peakcurrent0)
    i = i+1
plt.legend(legend_titles)
plt.title('UDB: 0 Hz')
plt.xlabel('Concentration (M)')
plt.ylabel('Normalized Peak Current')
plt.show()

#obtain 10Hz late current
i = 0
latecurrents10 = []
peakcurrents10 = []
if current == 1:
    doses = [0, 1e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5]
else
    doses = [0, 0.000001, 0.000005, 0.00001, 0.0001, 0.0005, 0.001, 0.002]
plt.figure()
while i < int(num):
    output = fcpc.doseresponse10(mat_files[i], cell_nums[i])
    peakcurrent10 = output[0]
    peakcurrents10.append(peakcurrent10)
    plt.plot(doses, peakcurrent10)
    i = i+1
plt.legend(legend_titles)
plt.title('UDB: 10 Hz')
plt.xlabel('Concentration (M)')
plt.ylabel('Normalized Peak Current')
plt.show()

#obtain 20Hz late current
i = 0
latecurrents20 = []
peakcurrents20 = []

if current == 1:
    doses = [0, 1e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5]
else
    doses = [0, 0.000001, 0.000005, 0.00001, 0.0001, 0.0005, 0.001, 0.002]
plt.figure()
while i < int(num):
    output = fcpc.doseresponse20(mat_files[i], cell_nums[i])
    peakcurrent20 = output[0]
    peakcurrents20.append(peakcurrent20)
    plt.plot(doses, peakcurrent20)
    i = i+1
plt.legend(legend_titles)
plt.title('UDB: 20 Hz')
plt.xlabel('Concentration (M)')
plt.ylabel('Normalized Peak Current')
plt.show()

print(peakcurrents0)
print(peakcurrents10)
print(peakcurrents20)

avgpeak0 = sum(peakcurrents0)/len(peakcurrents0)
avgpeak10 = sum(peakcurrents10)/len(peakcurrents10)
avgpeak20 = sum(peakcurrents20)/len(peakcurrents20)

plt.figure()
plt.plot(doses,avgpeak0)
plt.plot(doses,avgpeak10)
plt.plot(doses,avgpeak20)
plt.show()
