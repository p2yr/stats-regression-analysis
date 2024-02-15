import numpy as np
import scipy.stats as stats
import csv

def CI(data):
    n = len(data)
    mean= np.mean(data)
    sem = stats.sem(data)
    z = stats.t.ppf((1 + 0.95)/2, n-1)
    h = sem*z
    return(mean - h, mean + h)

def chi(data):
    n = len(data) - 2
    var = np.var(data)
    ns = n * var
    x1,x2 = stats.chi2.ppf(0.025, n), stats.chi2.ppf(0.975, n)
    return (ns/x1, ns/x2)

def testmeans(data1, data2):
    print(stats.ttest_ind(a=data1, b=data2, equal_var=True))

def testvars(data1, data2):
    fval = np.var(data1) / np.var(data2)
    return(stats.f.cdf(fval, len(data1) - 1, len(data2) - 1))

def main():
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
        ecu1 = np.array([float(x) for x in ecu1])
        ecu2 = np.array([float(x) for x in ecu2])
        ecu3 = np.array([float(x) for x in ecu3])
        timeout = np.array([float(x) for x in timeout])
        ecu11 = np.array([float(x) for x in ecu11])
        ecu21 = np.array([float(x) for x in ecu21])
        ecu31 = np.array([float(x) for x in ecu31])
        timeout1 = np.array([float(x) for x in timeout1])

        #print(chi(ecu31))
        #testmeans(ecu1, ecu11)
        print(testvars(ecu3, ecu31))
        


if __name__ == "__main__":
    main()
