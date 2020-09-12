## Task 0: The greeting string issued to the client upon connecting is "ECE Senior Capstone IoT simulator"
## Task 1: Code I added is in sp_iotsim.client folder in client.py file
## Task 2: 
## Task 3: 
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

According to the [SensoScientific](https://www.sensoscientific.com/blog-maintain-laboratory-temperature-humidity/#:~:text=In%20the%20United%20States%2C%20the,Other%20standards%20exist.) the optimum temperature in the office setting is 22.5C with an acceptable range of 20C-25C

## Task 4
**How is this simulation a reflection of the real world?**

This simulation is a great representation of the real world because in many circumstances we may have data with hundreds of data points which are outliers to the data set. There are also cases where data might be off a few unit values - for example a sensor might be transmitting data that tells us room temp is 27 degrees C when room temp may be 20 degrees C in reality. Therefore it's only a matter of skewing the data and it's mean to get a more accurate staticstical representation. This simulation gives us a glimpse into the massive amounts of data that may be coming in during a short time frame. This is crutial in devising methods that sort through all data in an efficient manner. 

**How is this simulation deficient? What factors does it fail to account for?**

This simulation is deficient in a couple ways. The first is that packages are streamed endlessly to the server. The second way which this simulation is deficient is there may be other clients from different locations around the world that need to connect to the same server which means data comes in at different times and frequencies. Multi-formatting is a factor that this simulation fails to account for. It may be most efficient for some sensors to send data in one format and other sensors to send data in another format, so having a server that is able to process and analyze these different formats and into a single format is adventageous. 

**How is the difficulty of initially using this Python websockets library as comapared to a compiled language e.g. C++**

dad

**Would it be better to have the server poll the sensors, or the sensors reach out to the server when they have data?**

Perhaps the most efficient method would be to have the server poll the sensor at some frequency so that the server is at less risk of crashing from too much data back to back. If the server polls the sensors then there is a set frequency at which the server polls the sensors. The downsides to this is that the sensors will need larger memory capacity and the server is at risk of being flooded with data if say there was a fluctuation of data. If the sensors reach out to the servers when they have data then there would be constant communication with the server which means that there is more eneergy consumed and the server is constantly running analysis on the data. 
