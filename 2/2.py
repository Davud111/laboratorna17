import pandas as pd
import math

series = pd.read_json("2/cords.txt", typ='series', orient='records')

def calcSideLength(A, B):
    return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

def parsePointValue(point, index):
    return int(point.split(",")[index])

def lengthBetweenTwoPointsByName(name1, name2):
    point1 = [parsePointValue(points[name1], 0), parsePointValue(points[name1], 1)]
    point2 = [parsePointValue(points[name2], 0), parsePointValue(points[name2], 1)]
    return calcSideLength(point1, point2)

points = dict()
for tup in series.items():
    points[tup[0]] = tup[1]
    
rectangleParams = dict()
rectangleParams["side AB"] = lengthBetweenTwoPointsByName("A","B")
rectangleParams["side BC"] = lengthBetweenTwoPointsByName("B","C")
rectangleParams["side CD"] = lengthBetweenTwoPointsByName("C","D")
rectangleParams["side DA"] = lengthBetweenTwoPointsByName("D","A")
rectangleParams["diagonal AC"] = lengthBetweenTwoPointsByName("A","C")
rectangleParams["diagonal BD"] = lengthBetweenTwoPointsByName("B","D")
    
yearSeries = pd.Series(rectangleParams)
yearSeries.to_json("2/rectangleParams.json")
