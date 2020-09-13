## Task 0: The greeting string issued to the client upon connecting is "ECE Senior Capstone IoT simulator"

## Task 1: Code I added is in sp_iotsim.client folder in client.py file

## Task 2: 

## Task 3
**Code to detect anomalies in original data file:**

The code below if a function which takes three inputs - officetemps, lab1temps and class1temps. New variables were created to store the means and standard deviations of the officetemps, lab1temps and class1temps - which was created in the 'processing.py' file. Afterwards, a new list of temperatures was created using the '[i for i in <file> if i<(value) and i>(value)] which would keep any values that were between the mean minus standard deviation and mean plus standard deviation. The code proceeds by printing out the number of data points in the new room list as well as calculating what the new mean, median and variance of each room is with the anomalies gone. Finally the anomalies are written to a txt file and classified as either office,lab1 or class1 anomalies. 
    
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
``` 
The following is the output of this code:

```sh
Number of data for new office 1835
Numbeer of data for new lab1 1811
Number of data for new class1 1703

New office temperature mean 22.995211006465887
New office temperature median 23.008154513832533
New office temperature variance 0.7132245582323415

New lab1 temperature mean 20.999487545983147
New lab1 temperaturee median 21.009796569886706
New lab1 temperature variance 0.2480754103110963

New class1 temperature mean 26.929264736469342
New class1 temperature median 27.017781630081224
New class1 temperature variance 5.6935895199010504
```

**Does a persistent change in temperature always indicate a failed sensor?**

No. There may be some instances where a sensor just needs to be recalibrated. Keeping track of means over time to see if its drifting is the best way to tell if recallibration is needed or if some factors are not accounted for. 

**What are possible bounds on temperature for each room type?** 
use our mean and standard deviaiton
According to the [Canadian Centre for Occupational Health and Safety](https://www.ccohs.ca/oshanswers/phys_agents/thermal_comfort.html#:~:text=Recommendations%20provided%20by%20CSA%20Z412,of%2020%2D23.5%C2%B0C) the optimum temperature in the office setting is 24.5C with an acceptable range of 23C-26C. In this case the office mean is 22.99C - or about 23C - with a standard deviation of 0.8 so our bounds would be from 22.2C to 23.8C.

According to the [SensoScientific](https://www.sensoscientific.com/blog-maintain-laboratory-temperature-humidity/#:~:text=In%20the%20United%20States%2C%20the,Other%20standards%20exist.) the optimum temperature in the lab setting is 22.5C with an acceptable range of 20C-25C. In this case the new lab1 mean is 20.99C - or about 21C - with a standard deviation of 0.5C so our bounds would be from 20.5C to 21.5C.

According to the [Wikipedia-Temperature and Pharmaceutical Science](https://en.wikipedia.org/wiki/Talk%3ARoom_temperature#:~:text=20%C2%B0C%20to%2025,listed%20on%20many%20pharmaceutical%20products.) the optimum temperature in the room setting is 22.5C with an acceptable range of 20C-25C. In this case the new class1 mean is 26.9C with a standard deviation of 2.4C so our bounds would be from 24.5C to 29.3C.


## Task 4
**How is this simulation a reflection of the real world?**

This simulation is an intermediate representation of the real world because not often is data streaming all in at once. Establishing a connection to the client(s) and being able to store the data is essential. In many circumstances there may be data sets with hundreds of data points which are outliers to the set and figuring out how to filter those out is a great advantage. Also knowing what those anomalies signify gives some insight on what may be going wrong or right in the experiment. Overall this was a valuable simulation that enabled us to learn the crutial operations to process and analyze data in Python. 

**How is this simulation deficient? What factors does it fail to account for?**

This simulation is deficient in a couple ways. The first is that packages are streamed endlessly to the server. The second way which this simulation is deficient is there may be other clients from different locations around the world that need to connect to the same server which means data comes in at different times and frequencies. Multi-formatting is a factor that this simulation fails to account for. It may be most efficient for some sensors to send data in one format and other sensors to send data in another format, so having a server that is able to process and analyze these different formats and into a single format is adventageous.  

**How is the difficulty of initially using this Python websockets library as comapared to a compiled language e.g. C++**

Reading and interpreting the Python websockets code is much easier than C++. Working on Python saved a lot of time and gave us the ability to traceback errors. My partner and I aren't too familiar with Python but we knew enough to get by and not have to deal with problems that C++ would've given us if we were familiarizing ourselves for the first time. 

**Would it be better to have the server poll the sensors, or the sensors reach out to the server when they have data?**

Perhaps the most efficient method would be to have the server poll the sensor at some frequency so that the server is at less risk of crashing from too much data back to back. If the server polls the sensors then there is a set frequency at which the server polls the sensors. The downsides to this is that the sensors will need larger memory capacity and the server is at risk of being flooded with data if say there was a fluctuation of data. If the sensors reach out to the servers when they have data then there would be constant communication with the server which means that there is more eneergy consumed and the server is constantly running analysis on the data. 
