# Ben Livney and Chris Lemus
## EC 463 Sensor Miniproject Report
## 9/17/2020


## Task 0
Welcome message: ECE Senior Capstone IoT simulator


## Task 1
Code to complete task 1:
```python
file = open("data.txt", mode = "w")
for i in range(max_packets):
    data = await websocket.recv()
    if i % 5 == 0:
        print(f"{i} total messages received")
    print(data) 
    file.write(data + "\n")
    file.flush()
file.close();
```


## Task 2
Terminal output for task 2
```sh
Office Temperature Mean: 22.885091366881266
Office Temperature Median: 22.988913098215388
Office Temperature Variance: 8.727166420366977
Lab1 Temperature Mean: 20.85145474841695
Lab1 Temperature Median: 20.991450295513076
Lab1 Temperature Variance: 6.508854145981514
Class1 Temperature Mean: 26.63444829610562
Class1 Temperature Median: 26.99484254031796
Class1 Temperature Variance: 168.39296941160802

Office Occupancy Mean: 1.9432515337423313
Office Occupancy Median: 2.0
Office Occupancy Variance: 2.0842029244608375
Lab1 Occupancy Mean: 4.94574780058651
Lab1 Occupancy Median: 5.0
Lab1 Occupancy Variance: 4.992657871879326
Class1 Occupancy Mean: 19.13855421686747
Class1 Occupancy Median: 19.0
Class1 Occupancy Variance: 19.08020031934969

Office CO2 Mean: 5.150816517713231
Office CO2 Median: 4.743238348731594
Office CO2 Variance: 5.461811572746369
Lab1 CO2 Mean: 9.803131512927326
Lab1 CO2 Median: 9.430643709425162
Lab1 CO2 Variance: 9.526253203605721
Class1 CO2 Mean: 30.124508334457154
Class1 CO2 Median: 29.68571855988014
Class1 CO2 Variance: 29.763965249291942
```

Graphs:

![office temperature](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/office%20temperature.png)
![office occupancy](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/office%20occupancy.png)
![office co2](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/office%20co2.png)
![lab1 temperature](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/lab1%20temperature.png)
![lab1 occupancy](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/lab1%20occupancy.png)
![lab1 co2](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/lab1%20co2.png)
![class1 temperature](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/class1%20temperature.png)
![class1 occupancy](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/class1%20occupancy.png)
![class1 co2](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/class1%20co2.png)
![time interval](https://github.com/blivney/2020-sensor-miniproject/blob/master/images/time%20interval.png)



## Task 3
**Code to detect anomalies in original data file:**
```python 
def anomalyAlgorithm(officetemps, lab1temps, class1temps):
    #means from original data
    officetempsMean = numpy.mean(officetemps)
    lab1tempsMean = numpy.mean(lab1temps)
    class1tempsMean = numpy.mean(class1temps)
    #std dev from original data
    officetempsStd = numpy.std(officetemps)
    lab1tempsStd = numpy.std(lab1temps)
    class1tempsStd = numpy.std(class1temps)
    
    newofficetemps = [i for i in officetemps if i<(officetempsMean + officetempsStd)  and i>(officetempsMean - officetempsStd)]
    
    newlab1temps = [i for i in lab1temps if i<(lab1tempsMean + lab1tempsStd) and i>(lab1tempsMean - lab1tempsStd)]
    
    newclass1temps = [i for i in class1temps if i<(class1tempsMean + class1tempsStd) and i>(class1tempsMean - class1tempsStd)]
    
    print("Number of data for new office " + str(len(newofficetemps)))
    print("Numbeer of data for new lab1 " + str(len(newlab1temps)))
    print("Number of data for new class1 " + str(len(newclass1temps)))
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
``` 
**Does a persistent change in temperature always indicate a failed sensor?**

No. There may be some instances where a sensor just needs to be recalibrated. However once there are changes that are a 
standard deviation or more away from the mean then it should be worrysome. 

**What are possible bounds on temperature for each room type?** 

According to the [Canadian Centre for Occupational Health and Safety](https://www.ccohs.ca/oshanswers/phys_agents/thermal_comfort.html#:~:text=Recommendations%20provided%20by%20CSA%20Z412,of%2020%2D23.5%C2%B0C) the optimum temperature in the office setting is 24.5C with an acceptable range of 23C-26C. 
    
According to the [Wikipedia-Temperature and Pharmaceutical Science](https://en.wikipedia.org/wiki/Talk%3ARoom_temperature#:~:text=20%C2%B0C%20to%2025,listed%20on%20many%20pharmaceutical%20products.) the optimum temperature in the room setting is 22.5C with an acceptable range of 20C-25C.
    
According to the [SensoScientific](https://www.sensoscientific.com/blog-maintain-laboratory-temperature-humidity/#:~:text=In%20the%20United%20States%2C%20the,Other%20standards%20exist.) the optimum temperature in the office setting is 22.5C with an acceptable range of 20C-25C.
## Task 4


