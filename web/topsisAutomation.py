import pandas as pd
from topsis import topsis
import numpy as np
import csv
import operator


class TopsisAutomation:
    resultTuples = []
    values = []
    alternatives = []
    def __init__(self, data, weight, benefit):
        print("initiating!")
        file = open(data)
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        rows.pop(0)
        # print(rows)
        self.data = rows
        self.weight = weight
        self.benefit = benefit

    def printData(self):
        print(self.data)

    def setData(self, path):
        self.data = pd.read_csv(path)

    def appendData(self, path):
        newData = pd.read_csv(path)
        self.data.append(newData)
    
    def seperateValues(self):
        # print(self.data)
        for row in self.data:
            temp = row
            self.alternatives.append(temp.pop(0))
            for i in range (len(temp)):
                temp[i] = float(temp[i])
            self.values.append(temp)
        
        print("here")
        # print(self.values)

        # return self.values

    def calculateTopsis(self):
        self.seperateValues()
        print(self.data)
        decision = topsis(self.values, self.weight, self.benefit)
        decision.calc()

        for i in range (len(decision.C)):
            self.resultTuples.append((self.alternatives[i], decision.C[i]))

        self.resultTuples = sorted(self.resultTuples, key=operator.itemgetter(1), reverse=True)

    def showRanks(self):
        if self.resultTuples.count == 0:
            print("There are no previous results")
            return

        
        for i in range (len(self.resultTuples)):
            print(f"{i + 1}. {self.resultTuples[i][0]} = {self.resultTuples[i][1]}")

        