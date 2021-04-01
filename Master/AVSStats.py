# -*- coding: utf-8 -*-
import statistics
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot_2samples
############################################################################################################
#   Eastern Michigan University
#   Backues Lab  
#   Author: Payton Dunning
#   Last Date Modified: March 31st, 2021
#
#   DESCRIPTION
############################################################################################################
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
############################################################################################################

def main():
    print("Please select a statistical script to run from the following 3 options: ")
    print("[1]: Find average body size")
    print("[2]: Q-Q (quantile-quantile) plot")
    print("[3]: Perform KS (Kolmogorov-Smirnov test)")
    print("[4]: Violin Plot")
    print("[0]: Exit Script")
    
    userSelection = input()
    if(userSelection == "1"):
        findAverage()
    elif(userSelection == "2"):
        qqPlot()
    elif(userSelection == "3"):
        ksTest()
    elif(userSelection == "4"):
        violinPlot()
    elif(userSelection == "0"):
        raise SystemExit
    
def findAverage():
    print("Select an option for file input:")
    print("[0]: Use default input file '../sliceData/sliceDefault.txt'")
    print("[1]: Use alternate input file.")
    userSelection = input()
    inputFile = "sliceData/sliceDefault.txt"
    
    if(userSelection == "1"):
        print("Please enter alternate input file: ")
        inputFile = input()
        
    numDataSets = 0 #Number of data sets read in from input file. Data sets are seperated by a -
    numOfBodies = 0
    areaAverage = 0
    areaMean = 0
    areaTotal = 0
    bodyValueArray = []
    largestArea = -1
    smallestArea = 1000000 #Should find a more systematic max value to use.
    
    inStream = open(inputFile, "r")
    inStreamLines = inStream.readlines()
    
    for line in inStreamLines:
        blackLine = line.strip() #current line with whitespace removed.
        if(blackLine == "-"):
            numDataSets += 1
        else:
            bodyAreas = blackLine.split(",")
            for value in bodyAreas:
                if(value == ""):
                    break;
                #print("\n%s" %(value))
                numValue = int(value)
                bodyValueArray.append(int(value))
                areaTotal += numValue
                numOfBodies += 1
                
                if(numValue < smallestArea):
                    smallestArea = numValue
                if(numValue > largestArea):
                    largestArea = numValue
    
    areaAverage = (float(areaTotal)) / (float(numOfBodies))
    #Finds SAMPLE standard deviation of body data.
    stdDev = statistics.stdev(bodyValueArray)
    
    print("\nAverage Body Slice Area = %d" %(areaAverage))
    print("\nLargest Body Slice Area = %d" %(largestArea))
    print("\nSmallest Body Slice Area = %d" %(smallestArea))
    print("\nNumber of data sets used = %d" %(numDataSets))
    print("\nStandard Deviation of data set = %d" %(stdDev))
    
def qqPlot():
    print("\nQQ")
    print("Select an option for file input:")
    print("[0]: Use default input file '../sliceData/sliceDefault.txt'")
    print("[1]: Use alternate input file.")
    
    userSelection = input()
    inputFile = "sliceData/sliceDefault.txt"
    
    if(userSelection == "1"):
        print("Please enter alternate input file: ")
        inputFile = input()
    
    bodyValueList = []
    
    inStream = open(inputFile, "r")
    inStreamLines = inStream.readlines()
    
    for line in inStreamLines:
        blackLine = line.strip() #current line with whitespace removed.
        if(blackLine == "-"):
            print("Check")
        else:
            bodyAreas = blackLine.split(",")
            for value in bodyAreas:
                if(value == ""):
                    break;
                #print("\n%s" %(value))
                numValue = int(value)
                bodyValueList.append(int(value))
          
    inStream.close()
    listSize = len(bodyValueList)
    
    aArray = np.array(bodyValueList)
    bArray = np.random.normal(loc=8.0, scale=3.0, size=listSize)
    
    #statsmodels.graphics.gofplots.qqplot_2samples(statsA, statsB, xlabel=None, ylabel=None)
    plotA = sm.ProbPlot(aArray)
    plotB = sm.ProbPlot(bArray)
    qqplot_2samples(plotA,plotB, line='r')
    
    plt.show()

#END OF qqPlot
def ksTest():
    print("\nKS")

def violinPlot():
    print("Select an option for file input:")
    print("[0]: Use default input file '../sliceData/sliceDefault.txt'")
    print("[1]: Use alternate input file.")
    userSelection = input()
    inputFile = "sliceData/sliceDefault.txt"
    
    if(userSelection == "1"):
        print("Please enter alternate input file: ")
        inputFile = input()
        
    bodyValueList = []
    
    inStream = open(inputFile, "r")
    inStreamLines = inStream.readlines()
    
    for line in inStreamLines:
        blackLine = line.strip() #current line with whitespace removed.
        #Change to if !="-": do stuff
        if(blackLine == "-"):
            print("Check")
        else:
            bodyAreas = blackLine.split(",")
            for value in bodyAreas:
                if(value == ""):
                    break;
                #print("\n%s" %(value))
                numValue = int(value)
                bodyValueList.append(int(value))
          
    inStream.close()
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
    #TEMPORARY secondary dataset for testing purposes:
    bodyList2 = [5075, 6001, 3275, 4500, 2309, 2399, 2680, 2900, 3800, 5765]
    data = [bodyValueList, bodyList2]
    
    sm.graphics.violinplot(data, ax=ax, labels=["Simulated Data", "Test Data"])
    
    ax.set_xlabel("Data Sets")
    ax.set_ylabel("Body Area (units)")
#main()