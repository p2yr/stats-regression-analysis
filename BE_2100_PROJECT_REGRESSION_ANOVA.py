import numpy as np
import scipy.stats as stats
import csv
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

def avg(data):
    return np.mean(data)

def getSS(x, y):
    ssxx = (sum(((x - avg(x))**2)))
    ssyy = (sum(((y - avg(y))**2)))
    ssxy = (sum(((x - avg(x))*(y - avg(y)))))
    return ssyy, ssxx, ssxy    
    
def slr(x, y):
    ssyy, ssxx, ssxy = getSS(x, y)
    b1 = ssxy/ssxx
    b0 = avg(y) - (b1*avg(x))
    print('y = ', b0, ' + ', b1, 'x')
    return b0, b1

def getSSE(x, y):
    sse = 0
    model = LinearRegression().fit(x, y)
    b0 = model.intercept_
    b0 = b0[0]
    b1 = model.coef_
    b1 = b1[0][0]
    print('sse: y = ', b0, ' + ', b1, 'x')
    ybar = b0 + (x * b1)
    sse = sum((y.values - ybar.values)**2)
    return sse[0]

def anova_slr(x, y, data, a):
    X = data[['ECU1']]
    X.values.reshape(-1, 1)
    Y = data[['Timeout']]
    Y.values.reshape(-1, 1)
    df_r= 1 
    df_e= len(x)-1 - df_r
    ssyy, ssxx, ssxy = getSS(x, y)
    sse = getSSE(X, Y)
    ssr = ssyy - sse
    msr = ssr / df_r
    mse = sse / df_e
    mst = ssyy / (len(x) - 1)
    f_val = stats.f.ppf(q=1-a, dfn=df_r, dfd=df_e)
    F = msr/mse

    print("-------ANOVA TABLE-------")
    print(df_r, "     ", df_e, "     ", (len(x) - 1))
    print(round(ssr,3), round(sse,3), " ", round(ssyy,3))
    print(round(msr,3), round(mse,3), "  ", round(mst,3))
    print("Fcrit: ", f_val)
    print("F:    ", F)
    return F

def anova_mlr(x, y, data, a):
    X = data[['ECU1', 'ECU3']]
    y = data['Timeout']
    X.values.reshape(-1, 1)
    y.values.reshape(-1, 1)
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary())

def loss_function(m, b, data):
    ## IGNORE THIS FUNCTION ##
    total_error = 0
    for i in range(len(data)):
        x = data.iloc[i].ECU1
        y = data.iloc[i].Timeout
        total_error += (y - (m * x + b))**2
    total_error / float(len(data))
def gradient_descent(m_now, b_now, data, L):
    ## IGNORE THIS FUNCTION; USED IT TO CHECK VALIDITY OF SLR ##
    ## PASTE THIS IN MAIN TO RUN: ##
##    m = 0
##    b = 0
##    L = 0.0001
##    epochs = 1000
##    for i in range(epochs):
##        if i % 50 == 0:
##            print(f"Epoch:{i}")
##        m, b = gradient_descent(m, b, d_1, L)
##
##    print(m, b)
    ## this is me experimenting with the partial derivative equations. please ignore.
    m_gradient = 0
    b_gradient = 0

    n = len(data)

    for i in range(n):
        x = data.iloc[i].ECU3
        y = data.iloc[i].Timeout

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

def main():
    data = pd.read_csv("project data sets- v2 11-09-23.xlsx - ECU.csv")
    d_1 = data.iloc[:25,:]
    d_2 = data.iloc[25:,:]
    #print(d_2)

    b, m = slr(d_1.ECU1, d_1.Timeout)
    b, m = slr(d_1.ECU2, d_1.Timeout)
    b, m = slr(d_1.ECU3, d_1.Timeout)
    b, m = slr(d_2.ECU1, d_2.Timeout)
    b, m = slr(d_2.ECU2, d_2.Timeout)
    b, m = slr(d_2.ECU3, d_2.Timeout)
    
    anova_slr(d_1.ECU1, d_1.Timeout, d_1, 0.05)
    anova_mlr([d_1.ECU1, d_1.ECU3], d_1.Timeout, d_1, 0.05)
    
    plt.scatter(d_1.ECU3, d_1.Timeout, color='black')
    plt.plot(list(range(0,10)), [m * x + b for x in range(0,10)], color='red')
    plt.title('Linear Regression of Timeout w.r.t ECU3, Supplier 1')
    plt.xlabel('ECU3')
    plt.ylabel('Timeout')
    plt.show()
        
if __name__ == "__main__":
    main()
