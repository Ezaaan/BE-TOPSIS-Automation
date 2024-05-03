import pandas as pd
from topsis import topsis
import numpy as np
import csv
import operator
import json
from web.models import TopsisResult


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

    def printData(self) -> None:
        print(self.data)

    def setData(self, path) -> None:
        self.data = pd.read_csv(path)

    def appendData(self, path) -> None:
        newData = pd.read_csv(path)
        self.data.append(newData)
    
    def seperateValues(self) -> None:
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

    def calculateTopsis(self) -> None:
        self.seperateValues()
        print(self.data)
        decision = topsis(self.values, self.weight, self.benefit)
        decision.calc()

        for i in range (len(decision.C)):
            self.resultTuples.append((self.alternatives[i], decision.C[i]))

        self.resultTuples = sorted(self.resultTuples, key=operator.itemgetter(1), reverse=True)

    def dump(self) -> dict[str, list[dict[str, any]]]:
        res = {}
        res['social_media'] = []
        for i in range (len(self.resultTuples)):
            res['social_media'].append({'rank': i+1, 'name': self.resultTuples[i][0], 'score': self.resultTuples[i][1]})
        return json.dumps(res)

    def persist(self) -> None:
        for i in range(len(self.resultTuples)):
            TopsisResult.objects.create(rank=i+1, name=self.resultTuples[i][0], score=self.resultTuples[i][1])
