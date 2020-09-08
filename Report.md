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
Lab1 Temperature Variance: 168.39296941160802

Office Occupancy Mean: 1.9432515337423313
Office Occupancy Median: 2.0
Office Occupancy Variance: 2.0842029244608375
Lab1 Occupancy Mean: 4.94574780058651
Lab1 Occupancy Median: 5.0
Lab1 Occupancy Variance: 4.992657871879326
Class1 Occupancy Mean: 19.13855421686747
Class1 Occupancy Median: 19.0
Lab1 Occupancy Variance: 19.08020031934969

Office CO2 Mean: 5.150816517713231
Office CO2 Median: 4.743238348731594
Office CO2 Variance: 5.461811572746369
Lab1 CO2 Mean: 9.803131512927326
Lab1 CO2 Median: 9.430643709425162
Lab1 CO2 Variance: 9.526253203605721
Class1 CO2 Mean: 30.124508334457154
Class1 CO2 Median: 29.68571855988014
Lab1 CO2 Variance: 29.763965249291942
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



## Task 4


