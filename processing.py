from pathlib import Path
import argparse
import asyncio
import websockets
import zlib
import json
from datetime import datetime as dt
import numpy
import matplotlib.pyplot as plt
import seaborn as sbn
import pandas

# DEFINE FUNCTIONS TO PROCESS DATA

temperature = {}; occupancy = {}; co2 = {}; timeInterval = [];

def loadData():
    file = open("data.txt", mode = "r")
    for l in file:
        jsonData = json.loads(l)
        room = list(jsonData.keys())[0]
        time = dt.fromisoformat(jsonData[room]["time"])
        timeInterval.append(dt.strptime(jsonData[room]["time"][11:], "%H:%M:%S.%f")) #- dt.strptime("00:00:00.00000", "%H:%M:%S.%f")
        temperature[time] = {room: jsonData[room]["temperature"][0]}
        occupancy[time]   = {room: jsonData[room]["occupancy"][0]}
        co2[time]         = {room: jsonData[room]["co2"][0]}
   # print(temperature)
    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data
    
  

def printResults(officetemps, lab1temps, class1temps, officeocc, lab1occ, class1occ, officeco2, lab1co2, class1co2):
    print("")
    print("Office Temperature Mean: " + str(numpy.mean(officetemps)))
    print("Office Temperature Median: " + str(numpy.median(officetemps)))
    print("Office Temperature Variance: " + str(numpy.var(officetemps)))
    print("Lab1 Temperature Mean: " + str(numpy.mean(lab1temps)))
    print("Lab1 Temperature Median: " + str(numpy.median(lab1temps)))
    print("Lab1 Temperature Variance: " + str(numpy.var(lab1temps)))
    print("Class1 Temperature Mean: " + str(numpy.mean(class1temps)))
    print("Class1 Temperature Median: " + str(numpy.median(class1temps)))
    print("Class1 Temperature Variance: " + str(numpy.var(class1temps)))
    print("")
    print("Office Occupancy Mean: " + str(numpy.mean(officeocc)))
    print("Office Occupancy Median: " + str(numpy.median(officeocc)))
    print("Office Occupancy Variance: " + str(numpy.var(officeocc)))
    print("Lab1 Occupancy Mean: " + str(numpy.mean(lab1occ)))
    print("Lab1 Occupancy Median: " + str(numpy.median(lab1occ)))
    print("Lab1 Occupancy Variance: " + str(numpy.var(lab1occ)))
    print("Class1 Occupancy Mean: " + str(numpy.mean(class1occ)))
    print("Class1 Occupancy Median: " + str(numpy.median(class1occ)))
    print("Class1 Occupancy Variance: " + str(numpy.var(class1occ)))
    print("")
    print("Office CO2 Mean: " + str(numpy.mean(officeco2)))
    print("Office CO2 Median: " + str(numpy.median(officeco2)))
    print("Office CO2 Variance: " + str(numpy.var(officeco2)))
    print("Lab1 CO2 Mean: " + str(numpy.mean(lab1co2)))
    print("Lab1 CO2 Median: " + str(numpy.median(lab1co2)))
    print("Lab1 CO2 Variance: " + str(numpy.var(lab1co2)))
    print("Class1 CO2 Mean: " + str(numpy.mean(class1co2)))
    print("Class1 CO2 Median: " + str(numpy.median(class1co2)))
    print("Class1 CO2 Variance: " + str(numpy.var(class1co2)))



def removeNaN(data, sensor, room):
    return [x for x in data[sensor][room].to_numpy() if str(x) != ("nan" or "NaN")]


   
def processData(data):
    for i in range(len(temperature) - 1):
        timeInterval[i] = timeInterval[i + 1] - timeInterval[i]
        timeInterval[i] = float(timeInterval[i].seconds + round(timeInterval[i].microseconds * 0.000001, 5))
    timeInterval.pop(); timeInterval.pop(); timeInterval.pop();
    
    officetemps = removeNaN(data, "temperature", "office")
    lab1temps = removeNaN(data, "temperature", "lab1")
    class1temps = removeNaN(data, "temperature", "class1")
    officeocc = removeNaN(data, "occupancy", "office")
    lab1occ = removeNaN(data, "occupancy", "lab1")
    class1occ = removeNaN(data, "occupancy", "class1")
    officeco2 = removeNaN(data, "co2", "office")
    lab1co2 = removeNaN(data, "co2", "lab1")
    class1co2 = removeNaN(data, "co2", "class1")

    printResults(officetemps, lab1temps, class1temps, officeocc, lab1occ, class1occ, officeco2, lab1co2, class1co2)
    anomalyAlgorithm(officetemps, lab1temps, class1temps)
 
# runs through lists to detect what values are in appropriate range
def anomalyAlgorithm(officetemps, lab1temps, class1temps):
    
    #means from original data
    officetempsMean = numpy.mean(officetemps)
    lab1tempsMean = numpy.mean(lab1temps)
    class1tempsMean = numpy.mean(class1temps)
    #std dev from original data
    officetempsStd = numpy.std(officetemps)
    lab1tempsStd = numpy.std(lab1temps)
    class1tempsStd = numpy.std(class1temps)
    #new list of room temps
    newofficetemps = [i for i in officetemps if i<(officetempsMean + officetempsStd)  and i>(officetempsMean - officetempsStd)]
    newlab1temps = [i for i in lab1temps if i<(lab1tempsMean + lab1tempsStd) and i>(lab1tempsMean - lab1tempsStd)]
    newclass1temps = [i for i in class1temps if i<(class1tempsMean + class1tempsStd) and i>(class1tempsMean - class1tempsStd)]
    
    officetempanomalies = [i for i in officetemps if i >= (officetempsMean + officetempsStd) or i <=(officetempsMean - officetempsStd)]
    lab1tempanomalies = [i for i in lab1temps if i >= (lab1tempsMean + lab1tempsStd) or i <= (lab1tempsMean - lab1tempsStd)]
    class1tempanomalies = [i for i in class1temps if i >= (class1tempsMean + class1tempsStd) or i <= (class1tempsMean - class1tempsStd)]
    
    print("Number of data for new office list " + str(len(newofficetemps)))
    print("Numbeer of data for new lab1 list " + str(len(newlab1temps)))
    print("Number of data for new class1 list " + str(len(newclass1temps)))
    print("")
    print("New office temperature mean " + str(numpy.mean(newofficetemps)))
    print("New office temperature median " + str(numpy.median(newofficetemps)))
    print("New office temperature variance " + str(numpy.var(newofficetemps)))
    print("")
    print("New lab1 temperature mean " + str(numpy.mean(newlab1temps)))
    print("New lab1 temperaturee median " + str(numpy.median(newlab1temps)))
    print("New lab1 temperature variance " + str(numpy.var(newlab1temps)))
    print("")
    print("New class1 temperature mean " + str(numpy.mean(newclass1temps)))
    print("New class1 temperature median " + str(numpy.median(newclass1temps)))
    print("New class1 temperature variance " + str(numpy.var(newclass1temps)))
    print("")
    print('Anomalous data written to "anomalies.txt"')
    
    file = open("anomalies.txt", mode = "w")
    file.write("Office:\n")
    for l in officetempanomalies:
        file.write(str(l) + "\n")
    file.write("Lab1:\n")
    for l in lab1tempanomalies:
        file.write(str(l) + "\n")
    file.write("Class1:\n")
    for l in class1tempanomalies:
        file.write(str(l) + "\n")
    file.close()
    

def plotData(data, sensor, room, col, x_label):
    points = []
    if sensor == "temperature" or sensor == "occupancy" or sensor == "co2":
        points = removeNaN(data, sensor, room)
    elif sensor == "time interval":
        points = timeInterval
    else:
        print("Invalid sensor type: choose from temperature, occupancy, co2, or time interval")
        return
    
    plt.figure()
    sbn.distplot(points, hist = True, bins = int(max(points)-min(points)), kde = True, color = col, kde_kws = {'linewidth': 3})
    plt.xlabel(x_label)
    plt.ylabel("Experimental Probability") 
    plt.title(room + " " + sensor)
    plt.show()
    

# CALL FUNCTIONS TO PROCESS DATA

data = loadData()
processData(data)
plotData(data, "temperature", "office", "blue", "Temperature (Degrees C)")
plotData(data, "occupancy", "office", "blue", "People")
plotData(data, "co2", "office", "blue", "Carbon Dioxide Concentration")
plotData(data, "temperature", "lab1", "red", "Temperature (Degrees C)")
plotData(data, "occupancy", "lab1", "red", "People")
plotData(data, "co2", "lab1", "red", "Carbon Dioxide Concentration")
plotData(data, "temperature", "class1", "green", "Temperature (Degrees C)")
plotData(data, "occupancy", "class1", "green", "People")
plotData(data, "co2", "class1", "green", "Carbon Dioxide Concentration")
plotData(data, "time interval", "", "black", "Time Interval (s)")







    
