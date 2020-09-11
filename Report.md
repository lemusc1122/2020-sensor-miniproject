## Task 0: The greeting string issued to the client upon connecting is "ECE Senior Capstone IoT simulator"
## Task 1: Code I added is in sp_iotsim.client folder in client.py file
## Task 2: 
## Task 3: 
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
Does a persistent change in temperature always indicate a failed sensor? 

    No. There may be some instances where a sensor just needs to be recalibrated. However once there are changes that are a 
    standard deviation or more away from the mean then it should be worrysome. 

What are possible bounds on temperature for each room type?

   According to the [Canadian Centre for Occupational Health and Safety] (https://www.google.com/search?rlz=1C5CHFA_enUS806US806&sxsrf=ALeKk012lAJgZbobkG26_-zwjrgepGooEg%3A1599788293932&ei=BdVaX6nHOPyKytMP28WykAE&q=room+temp+for+office+in+c&oq=room+temp+for+office+in+c&gs_lcp=CgZwc3ktYWIQAzIICCEQFhAdEB4yCAghEBYQHRAeMggIIRAWEB0QHjIICCEQFhAdEB46BAgAEEc6BQghEKABOgYIABAWEB46BQghEJIDUIscWIkoYNUqaABwAXgAgAF7iAGTBJIBAzEuNJgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwjp3ebn-9_rAhV8hXIEHduiDBIQ4dUDCA0&uact=5)
## Task 4: 
