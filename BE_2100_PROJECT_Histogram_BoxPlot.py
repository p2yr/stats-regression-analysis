from matplotlib import pyplot as plt
import numpy as np
import csv

with open("project data sets- v2 11-09-23.xlsx - ECU.csv") as csv_file:
    timeout = []
    ecu1 = []
    ecu2 = []
    ecu3 = []
    timeout1 = []
    ecu11 = []
    ecu21 = []
    ecu31 = []
    csv_reader= csv.reader(csv_file)
    header = next(csv_reader)
    row_index = 0
    for row in csv_reader:
        if(row_index < 26):
            timeout.append(row[1])
            ecu1.append(row[2])
            ecu2.append(row[3])
            ecu3.append(row[4])
            row_index += 1
        else:
            timeout1.append(row[1])
            ecu11.append(row[2])
            ecu21.append(row[3])
            ecu31.append(row[4])
    ecu1 = [float(x) for x in ecu1]
    ecu2 = [float(x) for x in ecu2]
    ecu3 = [float(x) for x in ecu3]
    timeout = [float(x) for x in timeout]

    ecu11 = [float(x) for x in ecu11]
    ecu21 = [float(x) for x in ecu21]
    ecu31 = [float(x) for x in ecu31]
    timeout1 = [float(x) for x in timeout1]

    data = [ecu3, ecu31]
    plt.boxplot(data)
    plt.show()

    binst = [7,9,11,13,15,17,19,21,23,25]
    bins1 = [0,1,2,3,4,5,6,7,8]
    bins2 = [.9,.92,.94,.96,.98,1,1.02,1.04]
    bins3 = [1,2,3,4,5,6,7,8,9]
    
    plt.hist(timeout, bins=binst, alpha=0.65, color='black', edgecolor='white')
    plt.hist(timeout1, bins=binst, alpha=0.45, color='blue', edgecolor='white')
    #plt.hist(ecu1, bins=bins1, alpha=0.45, color='black', edgecolor='black')
    #plt.hist(ecu11, bins=bins1, alpha=0.45, color='magenta', edgecolor='black')
    #plt.hist(ecu2, bins=bins2, alpha=0.45, color='black', edgecolor='black')
    #plt.hist(ecu21, bins=bins2, alpha=0.45, color='cyan', edgecolor='black')
    #plt.hist(ecu3, bins=bins3, alpha=0.45, color='black', edgecolor='black')
    #plt.hist(ecu31, bins=bins3, alpha=0.45, color='yellow', edgecolor='black')
    
    plt.title('Timeout Error')
    plt.xlabel('Time (sec)')
    plt.ylabel('Frequency')

    plt.show()
